# Recursive Problem-Solver: Workflow Patterns

Concrete examples showing how to apply recursive problem-solving to different scenarios.

## Table of Contents

1. [Pattern 1: Database Optimization (Deep Dive)](#pattern-1-database-optimization)
2. [Pattern 2: System Architecture Decision (Decision Framework)](#pattern-2-system-architecture-decision)
3. [Pattern 3: Code Review (Validation Loop)](#pattern-3-code-review)
4. [Pattern 4: Topic Mastery (Learning Deep Dive)](#pattern-4-topic-mastery)
5. [Pattern 5: API Design (Progressive Deepening)](#pattern-5-api-design)

---

## Pattern 1: Database Optimization (Deep Dive)

**Scenario:** E-commerce platform experiencing slow query performance on product catalog pages.

**Goal:** Identify root cause and implement solution with 85%+ confidence.

### Depth 0: Initial Exploration

**Tool:** `mcp-sequentialthinking-tools:sequentialthinking_tools`

```
Thought 1: The problem is slow product catalog queries. Need to understand current performance.
- Symptoms: Pages taking 3-5 seconds to load
- Affects: Product listing and search results
- Business impact: Likely causing abandonment

Thought 2: Identify constraints and context.
- Database: PostgreSQL 14
- Data size: 500K products, 10M orders
- Traffic: 1000 req/min during peak
- Current indexes: Primary keys only

Thought 3: Measure current state.
- EXPLAIN ANALYZE shows sequential scans on products table
- Most common query: SELECT * FROM products WHERE category_id = X ORDER BY price
- No index on category_id or price columns

Thought 4: Generate initial hypothesis.
- Root cause: Missing indexes on frequently queried columns
- Proposed solution: Add composite index on (category_id, price)

Thought 5: Quick validation check.
- Query accesses ~10K products per category
- Index should reduce from table scan (O(n)) to index scan (O(log n))
- Expected improvement: 80-90% reduction in query time

Thought 6: Initial confidence assessment.
- Have identified clear cause (missing indexes)
- Solution is standard and proven
- However: Haven't checked for other bottlenecks (N+1 queries, connection pool, etc.)
- Haven't tested on production-like data
- Haven't considered write performance impact

Confidence: 55% - Good starting hypothesis but incomplete analysis
```

**Output:** Initial hypothesis formed, confidence too low to implement.

---

### Depth 1: First Critique

**Tool:** `reflection:reflect`

**Prompt:**
```
Claim: "Adding a composite index on (category_id, price) will solve the slow product catalog queries"

Context: E-commerce platform with 500K products, 1000 req/min. Current sequential scans taking 3-5s. No indexes beyond primary keys.
```

**Reflection Output:**
```
Challenges to the claim:

1. **Incomplete problem diagnosis**
   - Have you measured ALL query types, not just category browsing?
   - What about product search queries?
   - Are there N+1 query problems in the ORM layer?

2. **Index design concerns**
   - Will one composite index cover all query patterns?
   - What about queries that filter by brand, price range, or availability?
   - Should you use partial indexes for common filters (e.g., in_stock = true)?

3. **Write performance impact**
   - How many writes per second to products table?
   - Will index maintenance slow down product updates?
   - Have you considered index bloat over time?

4. **Missing validation**
   - Did you test the index on a production copy?
   - What's the actual query plan improvement?
   - Did you measure memory usage impact?

5. **Alternative solutions not considered**
   - Redis caching for popular categories?
   - Materialized views for pre-computed aggregations?
   - Database connection pooling optimization?
   - Query result pagination to reduce data transfer?

Better approach: Run query log analysis to identify ALL slow queries, not just category browsing.
```

**Synthesis (Depth 1):**
```
Refined hypothesis after critique:

1. **Extended diagnosis needed:**
   - Analyze full query log (last 24h) to identify all slow queries
   - Check application code for N+1 queries
   - Measure connection pool utilization

2. **Multi-index strategy:**
   - Composite index on (category_id, price) for category browsing
   - Separate index on name for text search (using GIN with pg_trgm)
   - Partial index on (in_stock = true) for active products

3. **Complementary solutions:**
   - Add Redis cache for top 20 categories (cover 80% of traffic)
   - Implement pagination (LIMIT/OFFSET) to reduce data transfer
   - Review ORM queries for N+1 patterns

4. **Validation plan:**
   - Test indexes on production snapshot
   - Measure query time improvement with EXPLAIN ANALYZE
   - Monitor write performance impact for 1 week

Confidence: 72% - More complete approach but still need validation
```

**Why confidence increased:** More comprehensive solution, but still haven't tested or validated implementation feasibility.

---

### Depth 2: Deep Analysis & Edge Cases

**Tool:** `reflection:reflect`

**Prompt:**
```
Claim: "Multi-index strategy + Redis caching + N+1 fixes will solve performance issues"

Context: Refined solution includes multiple indexes, caching, and query optimization. Need to examine edge cases and potential failure modes.
```

**Reflection Output:**
```
Potential failure modes and edge cases:

1. **Cache stampede risk**
   - When Redis cache expires, all requests hit database simultaneously
   - Could cause worse performance spike than current state
   - Mitigation needed: Cache warming, staggered expiration, or dog-piling prevention

2. **Index selection problems**
   - PostgreSQL query planner might not choose optimal index
   - Especially with multiple indexes on same table
   - Mitigation: May need to force index hints or adjust random_page_cost

3. **Memory constraints**
   - Multiple indexes consume significant RAM (shared_buffers)
   - Did you check current memory utilization?
   - Each index approximately 50-100MB for 500K products

4. **Cache consistency**
   - How to invalidate Redis cache when products updated?
   - Risk of showing stale prices or out-of-stock items
   - Could impact business (wrong pricing, overselling)

5. **Migration risks**
   - Creating indexes on 500K products takes time (locks table?)
   - Concurrent index creation needed to avoid downtime
   - Need rollback plan if indexes hurt more than help

6. **Monitoring blind spots**
   - How will you know if solution works?
   - Need baseline metrics before implementation
   - Define success criteria: P95 query time < 500ms?

Trade-off analysis:
- Indexes: Fast reads vs slower writes vs memory usage
- Caching: Fast response vs stale data risk vs infrastructure complexity
- N+1 fixes: Optimal queries vs code refactoring effort
```

**Synthesis (Depth 2):**
```
Enhanced solution with risk mitigations:

**Phase 1: Baseline & Preparation**
1. Capture current metrics:
   - P50, P95, P99 query times
   - Query frequency by type
   - Write operation frequency
   - Current memory usage

2. Test on staging:
   - Clone production database
   - Create indexes using CREATE INDEX CONCURRENTLY
   - Measure improvement with production-like traffic

**Phase 2: Implementation**
1. Indexes (low risk, high reward):
   - `CREATE INDEX CONCURRENTLY idx_products_category_price ON products(category_id, price)`
   - `CREATE INDEX CONCURRENTLY idx_products_search ON products USING gin(name gin_trgm_ops)`
   - `CREATE INDEX CONCURRENTLY idx_products_active ON products(in_stock) WHERE in_stock = true`

2. Caching (medium risk, high reward):
   - Redis for top 20 categories only (limit blast radius)
   - 5-minute TTL to balance freshness vs performance
   - Probabilistic cache expiration to prevent stampede
   - Cache invalidation on product updates via Rails cache sweeper

3. N+1 fixes (low risk, medium reward):
   - Add `.includes(:category, :brand)` to product queries
   - Review with Bullet gem to identify remaining N+1s

**Phase 3: Validation**
- Deploy indexes first (lowest risk)
- Monitor for 48 hours
- If successful (P95 < 1s), add caching
- If still slow, investigate query plans with pg_stat_statements

**Success criteria:**
- P95 query time < 500ms (from 3-5s baseline)
- No increase in error rate
- Write performance degradation < 10%
- Memory usage increase < 20%

**Rollback plan:**
- Can drop indexes if performance worse
- Can disable Redis cache with feature flag
- Total rollback time: < 5 minutes

Confidence: 86% - Comprehensive solution with validated mitigations
```

**Why confidence increased:** Edge cases addressed, risks quantified, clear implementation plan, rollback strategy defined.

---

### Depth 3: Final Validation

**Tool:** `reflection:reflect`

**Prompt:**
```
Validate this database optimization solution against constraints:
- Must improve P95 latency to < 500ms
- Cannot cause downtime
- Write performance degradation must be < 10%
- Solution must be reversible

Solution: Multi-phase rollout with indexes → caching → N+1 fixes
```

**Reflection Output:**
```
Validation against constraints:

✅ **P95 latency target < 500ms**
- Indexes alone should provide 80-90% improvement (sequential scan → index scan)
- Current 3-5s → Expected 300-500ms with indexes
- Caching layer adds another 80% improvement for cache hits
- High confidence target will be met

✅ **Zero downtime requirement**
- CREATE INDEX CONCURRENTLY prevents table locks
- Caching rollout via feature flag (no code deployment needed)
- N+1 fixes deployed gradually via rolling restart
- Solution meets zero-downtime constraint

✅ **Write performance < 10% degradation**
- Measured on staging: 3 indexes add 8% overhead to INSERT/UPDATE
- Products table has low write volume (100 writes/min vs 1000 reads/min)
- Within acceptable threshold

✅ **Reversibility**
- Indexes can be dropped in seconds
- Redis cache disabled via feature flag
- N+1 fixes don't break existing functionality
- Full rollback possible in < 5 minutes

**Remaining concerns (minor):**
1. Haven't tested cache stampede mitigation (probabilistic expiration)
   - Mitigation: Start with 10-minute TTL to reduce expiration frequency
   
2. PostgreSQL planner behavior with multiple indexes unknown
   - Mitigation: Monitor with pg_stat_statements, adjust random_page_cost if needed

3. Long-term index bloat not measured
   - Mitigation: Set up REINDEX job every 3 months

**Implementation confidence: 91%**

Ready to proceed with phased rollout.
```

---

### Final Recommendation (Depth 3)

**Confidence: 91%** ✅

**Recommendation:** Proceed with implementation using 3-phase rollout.

**Phase 1 (Week 1):** Deploy indexes
- Lowest risk, highest impact
- Expect 80% latency improvement
- Monitor write performance

**Phase 2 (Week 2):** Enable Redis caching
- If indexes insufficient
- Start with 10 categories, expand gradually
- Monitor cache hit rate and invalidation

**Phase 3 (Week 3):** Deploy N+1 fixes
- Code refactoring for remaining queries
- Gradual rollout with monitoring

**Success metrics tracked:**
- P95 query time (target: <500ms)
- Write operation latency
- Error rates
- Memory utilization

**Risks acknowledged:**
- Minor: Index bloat over time (mitigation: quarterly REINDEX)
- Minor: Query planner suboptimal choices (mitigation: manual tuning)

**Total token usage: ~25K** (well under budget)

---

## Pattern 2: System Architecture Decision (Decision Framework)

**Scenario:** Startup needs to choose between monolith vs microservices architecture.

**Goal:** Make informed architectural decision with 85%+ confidence.

### Depth 0: Options Generation

**Tool:** `mcp-sequentialthinking-tools:sequentialthinking_tools`

```
Thought 1: Frame the decision context.
- Company: 6-month-old startup, 5 engineers
- Product: B2B SaaS platform for inventory management
- Current state: MVP built as Rails monolith
- Growth: 50 customers, expecting 10x growth in 12 months
- Question: Continue with monolith or migrate to microservices?

Thought 2: Identify key decision factors.
- Team size and expertise
- Development velocity requirements
- Scalability needs (technical and organizational)
- Operational complexity tolerance
- Time to market pressure
- Budget constraints

Thought 3: Option 1 - Keep monolith.
Pros:
- Faster development (no inter-service communication complexity)
- Simpler deployment (single app)
- Easier debugging (single codebase)
- Lower operational overhead

Cons:
- Scaling limitations (must scale entire app)
- Tight coupling between features
- Longer deployment times as codebase grows
- Team coordination challenges at scale

Thought 4: Option 2 - Microservices.
Pros:
- Independent scaling of services
- Team autonomy (each team owns service)
- Technology flexibility
- Fault isolation

Cons:
- Network latency and complexity
- Distributed tracing/debugging harder
- Data consistency challenges
- Operational overhead (multiple deployments, monitoring)

Thought 5: Option 3 - Modular monolith (hybrid).
Pros:
- Logical separation within monolith
- Easier to extract services later
- Retain monolith simplicity initially
- Clear boundaries between domains

Cons:
- Requires architectural discipline
- Can become entangled if not careful
- Eventually hits monolith scaling limits

Thought 6: Initial assessment.
- Team size (5 engineers) too small for microservices overhead
- No evidence of specific scaling bottlenecks yet
- Development velocity critical for startup survival
- Premature optimization risk

Preliminary ranking:
1. Modular monolith (best of both worlds)
2. Keep simple monolith (focus on speed)
3. Microservices (too complex too early)

Confidence: 48% - Haven't deeply evaluated trade-offs or validated assumptions
```

---

### Depth 1-2: Deep Evaluation of Each Option

**Tool:** `reflection:reflect` (repeated for each option)

**Prompt for Modular Monolith:**
```
Claim: "Modular monolith is the best architecture for a 5-person startup expecting 10x growth"

Context: B2B SaaS, 50 customers, 6 months old, Rails monolith currently. Need to balance development velocity with future scalability.
```

**Reflection Output:**
```
Hidden costs and risks of modular monolith:

1. **Architectural discipline required**
   - 5-person team needs to maintain clear module boundaries
   - Risk: Without senior architect, boundaries erode quickly
   - Reality check: Do you have architectural experience on the team?

2. **Tooling and enforcement**
   - Need tools to enforce module boundaries (e.g., packwerk, rails-zeitwerk)
   - Requires setup time and learning curve
   - May slow initial development

3. **Migration path assumption**
   - Assumption: Can easily extract modules into services later
   - Reality: Shared database makes extraction hard (data migration complex)
   - May end up with worst of both worlds

4. **Scaling characteristics**
   - Still scales as single unit (entire app)
   - If one module needs more resources, must scale all
   - May hit scalability limits sooner than expected with 10x growth

5. **Team growth challenges**
   - At 15-20 engineers (after 10x growth), modular monolith becomes bottleneck
   - Merge conflicts, deployment coordination, testing time all increase
   - May need to re-architect exactly when you're busiest

**Better questions to ask:**
- What specifically needs to scale? (Database? Compute? Specific features?)
- What's the timeline for 10x growth? (3 months vs 18 months matters)
- What's more critical: development velocity today or scalability tomorrow?
- What's the team's operational maturity? (Can you run microservices?)
```

**Synthesis for Modular Monolith:**
```
Revised assessment:

Strengths:
- Good middle ground IF team has architectural discipline
- Provides logical boundaries without operational overhead
- Can work well for 12-18 month horizon

Weaknesses:
- Requires senior architect to maintain boundaries
- Doesn't solve actual scaling problems (still single-unit deployment)
- Adds complexity without proportional near-term benefits

Critical dependencies:
- Team has architectural expertise: YES/NO?
- Growth timeline: <6 months (too fast) or 12+ months (good fit)?

Current confidence: 65% (modular monolith viable IF conditions met)
```

---

### Depth 3: Comparative Analysis & Decision

**Tool:** `reflection:reflect`

**Prompt:**
```
Compare architectural options for 5-person startup considering:
1. Current state: Rails monolith, 50 customers
2. Growth target: 10x in 12 months
3. Team: 5 engineers, no senior architect
4. Business priority: Shipping features fast (survival mode)

Options evaluated:
- Simple monolith (keep current)
- Modular monolith (add structure)
- Microservices (full rewrite)
```

**Reflection Output:**
```
Decision analysis:

**Critical insight:** The real question is not "what's the best architecture?" but "what's the best architecture FOR THIS STAGE?"

**Stage analysis:**
- Pre-product/market fit: Need maximum velocity
- Team size: 5 engineers (below microservices viability threshold)
- Runway: Likely 12-18 months (typical startup)
- Risk profile: Survival > optimization

**Weighted decision factors:**
1. **Development velocity (40% weight):** MOST CRITICAL
   - Monolith: 10/10 (fastest)
   - Modular monolith: 7/10 (added complexity)
   - Microservices: 3/10 (massive slowdown)

2. **Operational simplicity (25% weight):** Important for small team
   - Monolith: 10/10
   - Modular monolith: 8/10
   - Microservices: 2/10

3. **Scalability (20% weight):** Matters but not immediately
   - Monolith: 6/10 (vertical scaling sufficient for 500 customers)
   - Modular monolith: 7/10
   - Microservices: 10/10

4. **Team scaling (15% weight):** Future consideration
   - Monolith: 5/10 (will need re-arch at 20+ engineers)
   - Modular monolith: 7/10
   - Microservices: 9/10

**Weighted scores:**
1. Simple monolith: (10×0.4) + (10×0.25) + (6×0.2) + (5×0.15) = 8.45
2. Modular monolith: (7×0.4) + (8×0.25) + (7×0.2) + (7×0.15) = 7.25
3. Microservices: (3×0.4) + (2×0.25) + (10×0.2) + (9×0.15) = 4.85

**Winner: Simple monolith**

**Why this contradicts conventional wisdom:**
- Industry cargo-culting microservices from FAANG
- Survivorship bias (only successful companies talk about their architecture)
- Premature optimization is the root of all evil

**The real strategy:**
1. Keep simple monolith for next 12 months
2. Focus on product-market fit and revenue
3. Invest in good practices:
   - Clear module boundaries in code (namespacing)
   - Comprehensive test coverage
   - Database indexing and query optimization
4. Re-evaluate architecture at 500 customers OR 15 engineers (whichever comes first)

**This buys you:**
- Maximum development velocity when you need it most
- Time to actually understand where the scaling bottlenecks are (data-driven decision)
- Option to extract services later (with real data on what to extract)
```

---

### Final Recommendation (Depth 3)

**Confidence: 89%** ✅

**Decision: Stick with simple monolith for 12+ months**

**Rationale:**
1. Development velocity is existential priority (company needs to survive)
2. Team too small to operate microservices effectively
3. 10x customer growth (50→500) doesn't require microservices
4. Premature architectural complexity increases failure risk

**Implementation plan:**
- Continue Rails monolith
- Add these safeguards:
  - Namespace code by domain (Users, Inventory, Orders, etc.)
  - Extract shared concerns into engines/gems
  - Maintain >80% test coverage
  - Set up performance monitoring (Scout APM or similar)

**Re-evaluation triggers:**
- Customer count > 500 (actual scaling pressure)
- Team size > 15 engineers (coordination bottleneck)
- Specific performance bottleneck identified (data-driven)
- Funding secured for 24+ month runway (can afford refactor)

**Risks acknowledged:**
- May need to re-architect in 18-24 months (acceptable)
- Technical debt will accumulate (managed with good practices)
- Harder to hire senior engineers who want microservices (recruit for monolith expertise instead)

**Total token usage: ~22K**

---

## Pattern 3: Code Review (Validation Loop)

**Scenario:** Pull request with authentication middleware changes needs review before production.

**Goal:** Identify security and functional issues with >90% confidence.

### Depth 0: Initial Code Analysis

**Tool:** `mcp-sequentialthinking-tools:sequentialthinking_tools`

**Code being reviewed:**
```python
# Authentication middleware for Flask API
def auth_middleware(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token:
            token = token.replace('Bearer ', '')
            user = verify_token(token)
            if user:
                return func(*args, **kwargs, user=user)
        return jsonify({'error': 'Unauthorized'}), 401
    return wrapper

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_id = payload['user_id']
        return db.query(User).filter(User.id == user_id).first()
    except:
        return None
```

**Sequential thinking:**
```
Thought 1: Understand what this code does.
- Authentication decorator for API endpoints
- Extracts token from Authorization header
- Verifies JWT token
- Fetches user from database
- Returns 401 if invalid

Thought 2: Check for obvious security issues.
- Uses HS256 (symmetric) instead of RS256 (asymmetric) - acceptable for internal APIs
- SECRET_KEY not shown - hoping it's securely stored
- Bare except clause catches all exceptions - could hide bugs

Thought 3: Check for functional issues.
- Missing @wraps decorator - will break function metadata
- Token validation occurs on every request - no caching, could be slow
- Database query on every request - N+1 problem potential

Thought 4: Check edge cases.
- What if Authorization header missing? Returns 401 ✓
- What if token malformed? Caught by try/except (silent fail)
- What if user deleted but token still valid? Will return None, then 401 ✓
- What if payload missing 'user_id'? KeyError caught by except

Thought 5: Identify critical issues.
HIGH SEVERITY:
- Bare except clause masks real errors (KeyError, Database errors)
- Missing @wraps means Flask routing might break

MEDIUM SEVERITY:
- No token expiration check (relies on JWT exp claim)
- No rate limiting for failed auth attempts
- Database query on every request (performance)

LOW SEVERITY:
- No logging for auth failures (debugging difficulty)

Thought 6: Initial confidence.
- Found several issues, but is this comprehensive?
- Haven't checked for all JWT vulnerabilities
- Haven't tested concurrent requests
- Haven't checked integration with existing endpoints

Confidence: 58% - Found issues but review incomplete
```

---

### Depth 1: Security-Focused Validation

**Tool:** `reflection:reflect`

**Prompt:**
```
Claim: "This authentication middleware is secure for production use"

Code snippet: [paste code]

Context: Flask API handling user authentication with JWT tokens. Will protect sensitive endpoints.
```

**Reflection Output:**
```
Security vulnerabilities found:

1. **JWT Algorithm Confusion Attack (HIGH)**
   ```python
   jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
   ```
   - Hardcoded to HS256, but doesn't verify algorithm claim
   - Attacker could change alg to "none" and bypass signature verification
   - Fix: Add `options={'verify_signature': True}` or upgrade to newer PyJWT

2. **Timing Attack on Token Verification (MEDIUM)**
   - User lookup happens after token decode
   - Timing difference reveals valid vs invalid tokens
   - Mitigation: Constant-time comparison or rate limiting

3. **No Token Revocation Check (MEDIUM)**
   - Once issued, token is valid until expiration
   - If user logs out or is banned, token still works
   - Need: Token blacklist or session store

4. **Bare Exception Hides Errors (HIGH)**
   ```python
   except:
       return None
   ```
   - Could mask database errors, network issues, or bugs
   - Silent failures make debugging impossible
   - Attacker could exploit specific error conditions

5. **No Rate Limiting (MEDIUM)**
   - Unlimited authentication attempts
   - Enables brute force attacks on tokens
   - Need: Rate limiting per IP or endpoint

6. **Missing HTTPS Enforcement (HIGH if not handled elsewhere)**
   - Token sent in plain text if HTTP
   - Need to verify HTTPS-only in production

7. **SQL Injection Potential (LOW - ORM should protect)**
   ```python
   db.query(User).filter(User.id == user_id).first()
   ```
   - Using ORM (SQLAlchemy) provides protection
   - But should validate user_id is integer

CRITICAL FIX NEEDED: The bare except is a security AND functional bug.
```

---

### Depth 2: Functional & Performance Validation

**Tool:** `reflection:reflect`

**Prompt:**
```
Find functional bugs and performance issues in this authentication middleware:
[paste code]

Consider: concurrent requests, database load, error handling, integration with Flask routing.
```

**Reflection Output:**
```
Functional issues:

1. **Missing @wraps decorator (BREAKS FUNCTIONALITY)**
   ```python
   def auth_middleware(func):
       def wrapper(*args, **kwargs):  # <-- Missing @wraps(func)
   ```
   - Flask relies on __name__ and __module__ for routing
   - This will break if multiple endpoints use the decorator
   - Fix: Add `@wraps(func)` from functools

2. **User parameter name collision (BUG)**
   ```python
   return func(*args, **kwargs, user=user)
   ```
   - If wrapped function already has 'user' parameter, this causes TypeError
   - Fix: Use request context or g.current_user instead

3. **Return type inconsistency (POTENTIAL BUG)**
   ```python
   return jsonify({'error': 'Unauthorized'}), 401
   ```
   - Wrapped function might return different types (could cause issues)
   - Should ensure consistent error response format

Performance issues:

1. **Database query on every request (N+1 PROBLEM)**
   ```python
   db.query(User).filter(User.id == user_id).first()
   ```
   - 1000 req/sec = 1000 DB queries/sec (unnecessary load)
   - Token already contains user_id, no need to fetch full User object
   - Fix: Cache user object or use token claims only

2. **No connection pooling check**
   - Multiple sequential DB queries could exhaust pool
   - Need to verify connection pool configuration

3. **Token decode on every request**
   - JWT decode is cryptographically expensive
   - Could cache decoded tokens with short TTL (30 seconds)

Edge cases not handled:

1. Authorization header format variations:
   - "Bearer <token>" vs "bearer <token>" (case sensitivity)
   - Extra whitespace: "Bearer  <token>"
   - Multiple spaces: "Bearer<token>" (missing space)

2. Multiple Authorization headers (malicious or misconfigured)

3. Empty token string after "Bearer " removal

4. Token with null bytes or special characters
```

---

### Depth 3: Refined Solution

**Synthesis of all findings:**

```python
# IMPROVED VERSION: Authentication middleware for Flask API
from functools import wraps
import jwt
from flask import request, jsonify, g
import logging

# Configuration
TOKEN_CACHE_TTL = 30  # seconds
MAX_AUTH_ATTEMPTS = 5  # per IP per minute

logger = logging.getLogger(__name__)

def auth_middleware(func):
    @wraps(func)  # FIX: Preserve function metadata
    def wrapper(*args, **kwargs):
        # Extract token with proper error handling
        auth_header = request.headers.get('Authorization', '').strip()
        
        if not auth_header.startswith('Bearer '):
            logger.warning(f"Invalid auth header format from {request.remote_addr}")
            return jsonify({'error': 'Invalid authorization header'}), 401
        
        token = auth_header[7:].strip()  # Remove "Bearer " prefix
        
        if not token:
            return jsonify({'error': 'Token missing'}), 401
        
        # Verify token with specific exception handling
        try:
            payload = jwt.decode(
                token,
                SECRET_KEY,
                algorithms=['HS256'],
                options={'verify_signature': True, 'verify_exp': True}
            )
        except jwt.ExpiredSignatureError:
            logger.warning(f"Expired token from {request.remote_addr}")
            return jsonify({'error': 'Token expired'}), 401
        except jwt.InvalidTokenError as e:
            logger.warning(f"Invalid token from {request.remote_addr}: {e}")
            return jsonify({'error': 'Invalid token'}), 401
        except Exception as e:
            logger.error(f"Unexpected error verifying token: {e}")
            return jsonify({'error': 'Authentication error'}), 500
        
        # Check token revocation (blacklist)
        if is_token_revoked(token):
            logger.warning(f"Revoked token attempt from {request.remote_addr}")
            return jsonify({'error': 'Token revoked'}), 401
        
        # Extract and validate user_id
        user_id = payload.get('user_id')
        if not user_id or not isinstance(user_id, int):
            logger.error(f"Invalid user_id in token payload: {user_id}")
            return jsonify({'error': 'Invalid token payload'}), 401
        
        # Use Flask g context instead of passing as parameter
        g.current_user_id = user_id
        
        # Optional: Fetch full user object only if needed
        # Most endpoints can work with just user_id from token
        
        return func(*args, **kwargs)
    
    return wrapper

def is_token_revoked(token):
    """Check if token is in revocation blacklist (Redis cache)"""
    # Implementation depends on your caching strategy
    return redis_client.exists(f"revoked_token:{token}")
```

**Changes made:**
1. âœ… Added @wraps(func) to preserve function metadata
2. âœ… Specific exception handling (no bare except)
3. âœ… Explicit JWT signature and expiration verification
4. âœ… Token revocation check (blacklist)
5. âœ… Proper logging for security events
6. âœ… Input validation (token format, user_id type)
7. âœ… Use Flask 'g' context instead of parameter injection
8. âœ… Removed unnecessary database query (use user_id from token)

**Still need to address (outside middleware):**
- Rate limiting (use Flask-Limiter)
- HTTPS enforcement (nginx/load balancer)
- Token caching strategy (Redis)

---

### Final Validation (Depth 3)

**Tool:** `reflection:reflect`

**Prompt:**
```
Validate this improved authentication middleware against production requirements:
- Must be secure against OWASP Top 10
- Must handle 1000 req/sec
- Must not break existing endpoints
- Must provide clear error messages

Code: [paste improved version]
```

**Reflection Output:**
```
Validation results:

✅ **Security (OWASP Top 10)**
- Injection: Protected (JWT parsing, no SQL queries)
- Broken Auth: Fixed (proper verification, revocation, expiry)
- Sensitive Data: Improved (logging doesn't expose tokens)
- XXE: N/A (no XML parsing)
- Access Control: Improved (token revocation check)
- Security Misconfiguration: Better (explicit options)
- XSS: N/A (API only)
- Insecure Deserialization: Protected (JWT verification)
- Components with Vulnerabilities: Depends on PyJWT version (check)
- Insufficient Logging: Fixed (added security event logging)

✅ **Performance (1000 req/sec)**
- Removed database query (was bottleneck)
- JWT decode is fast (~0.1ms per token)
- Redis blacklist check is fast (<1ms)
- Total overhead: ~1-2ms per request
- Can handle 1000 req/sec easily

✅ **Backward compatibility**
- @wraps preserves function signatures
- Uses g.current_user_id instead of parameter injection (safer)
- Existing endpoints need minor update: g.current_user_id instead of user parameter

⚠️  **Error messages**
- Good: Specific errors for debugging
- Concern: May reveal too much to attackers
- Recommendation: Different messages for dev vs production

**Remaining tasks:**
1. Update existing endpoints to use g.current_user_id
2. Implement Redis-based token blacklist
3. Add rate limiting middleware
4. Verify PyJWT version >= 2.0
5. Add integration tests

Confidence: 94% - Production-ready with minor TODOs
```

---

### Code Review Summary

**Confidence: 94%** ✅

**Verdict:** NEEDS CHANGES before merge

**Critical issues fixed:**
1. Bare except clause → Specific exception handling
2. Missing @wraps → Function metadata preserved
3. Algorithm confusion attack → Explicit verification
4. Database on every request → Removed (use token claims)

**Remaining tasks (blocking):**
- Implement token revocation checking (is_token_revoked function)
- Update existing endpoints to use g.current_user_id
- Add integration tests

**Recommended (non-blocking):**
- Add rate limiting middleware
- Set up security event monitoring
- Document migration guide for endpoints

**Estimated time to fix:** 4-6 hours

**Total token usage: ~20K**

---

## Pattern 4: Topic Mastery (Learning Deep Dive)

**Scenario:** Need to understand "eventual consistency" in distributed systems for an architecture decision.

**Goal:** Reach 85%+ confidence in understanding the concept and its implications.

### Depth 0: Initial Understanding

**Tool:** `mcp-sequentialthinking-tools:sequentialthinking_tools`

```
Thought 1: What is eventual consistency (basic definition)?
- Consistency model in distributed systems
- Data replicas will eventually converge to the same value
- Opposite of strong consistency (immediate synchronization)
- Trade-off: Availability vs consistency (CAP theorem)

Thought 2: Why does it exist?
- Network partitions make strong consistency expensive
- Reduces latency (don't wait for all replicas)
- Enables high availability (system works even if some nodes down)
- Necessary for geo-distributed systems

Thought 3: How does it work (conceptual)?
Example: E-commerce inventory
- User A checks inventory in US datacenter: 5 items available
- User B checks inventory in EU datacenter: 5 items available
- User A buys 1 item (US datacenter updates to 4)
- User B buys 1 item (EU datacenter still shows 5, updates to 4)
- Replication happens asynchronously
- Eventually both datacenters show 3 items
- PROBLEM: Oversold by 1 item (temporary inconsistency)

Thought 4: Real-world examples.
- DNS (eventual consistency of record updates)
- Amazon DynamoDB (configurable consistency levels)
- Cassandra (eventual consistency by default)
- Social media feeds (likes/comments appear with delay)

Thought 5: When to use vs avoid.
Use when:
- High availability > strict consistency
- Geographic distribution needed
- Read-heavy workloads
- Temporary inconsistency acceptable

Avoid when:
- Financial transactions (must be exact)
- Inventory management (can't oversell)
- Access control (security risk)

Thought 6: Self-assessment of understanding.
- Can explain the concept ✓
- Understand basic trade-offs ✓
- Have examples ✓
- BUT: Don't understand resolution mechanisms (CRDTs, vector clocks, etc.)
- BUT: Don't know how to implement in practice
- BUT: Don't understand edge cases and failure modes

Confidence: 62% - Basic understanding but missing depth
```

---

### Depth 1: Gap Identification

**Tool:** `reflection:reflect`

**Prompt:**
```
What am I missing about eventual consistency in distributed systems?

Current understanding:
- Data replicas converge asynchronously
- Trade-off between availability and consistency
- Used in systems like DynamoDB, Cassandra
- Can cause temporary inconsistencies (like overselling)
```

**Reflection Output:**
```
Knowledge gaps identified:

1. **Conflict resolution mechanisms**
   - What happens when two writes conflict?
   - Last-write-wins (LWW): Simple but can lose data
   - Vector clocks: Tracks causality between writes
   - CRDTs: Conflict-free replicated data types (auto-merge)
   - Application-specific resolution

2. **Consistency levels (tunable)**
   - Eventual consistency is not binary (many levels)
   - Quorum reads/writes (R + W > N ensures consistency)
   - Read-your-writes consistency
   - Monotonic read consistency
   - Session consistency

3. **Practical implications**
   - How to design UI for eventual consistency (show staleness indicators)
   - How to test eventually consistent systems
   - How to debug race conditions
   - How to handle user confusion from stale data

4. **CAP theorem nuances**
   - It's not just "pick 2 of 3"
   - Partitions are rare, so it's really CP vs AP when partition happens
   - Modern systems often choose "eventual consistency" during partitions

5. **Specific failure modes**
   - Split-brain scenarios
   - Zombie writes (delayed writes after presumed failure)
   - Clock skew causing incorrect ordering
   - Network delays causing false conflicts

6. **Implementing in practice**
   - Database-specific settings (DynamoDB consistency levels, Cassandra CL)
   - Application-level strategies (version numbers, checksums)
   - Monitoring and observability

Example you didn't consider:
- Banking: Can't use eventual consistency for account balances
- Solution: Strong consistency for critical operations, eventual for everything else (hybrid)
```

---

### Depth 2: Deep Dive on Gaps

**Addressing each major gap:**

#### Gap 1: Conflict Resolution

**Sequential thinking:**
```
Thought 1: Last-Write-Wins (LWW)
- Simplest strategy: Use timestamp, latest write wins
- Problem: Clock skew can cause wrong write to win
- Problem: Lost updates (earlier write discarded completely)
- Example: User A sets profile bio to "Hello", User B sets to "World", LWW keeps "World" based on timestamp
- Lost data: User A's "Hello" never known to exist

Thought 2: Vector Clocks
- Each replica maintains version vector [replica_id: version_num]
- Can detect concurrent writes vs causally ordered writes
- Example:
  * Initial: [A:0, B:0]
  * A writes: [A:1, B:0]
  * B writes: [A:0, B:1]
  * These are concurrent (neither causally ordered)
- Application must resolve conflicts

Thought 3: CRDTs (Conflict-Free Replicated Data Types)
- Data structures that mathematically guarantee convergence
- Operations are commutative (order doesn't matter)
- Examples:
  * G-Counter: Increment-only counter (sum of all replica counters)
  * PN-Counter: Increment + decrement (separate positive/negative counters)
  * OR-Set: Add/remove elements without conflicts
- Limitation: Not all data types have CRDT equivalent

Thought 4: Application-specific resolution
- Merge both writes (e.g., shopping cart: union of items)
- Prompt user to resolve (e.g., Google Docs conflict resolution)
- Use business logic (e.g., inventory: pessimistic "lock" via reservations)

Insight: Conflict resolution is not automatic - requires design choice based on domain.
```

#### Gap 2: Consistency Levels

**Sequential thinking:**
```
Thought 1: Quorum consistency (tunable)
- N = total replicas, R = read replicas, W = write replicas
- If R + W > N: Guaranteed to read your writes (strong consistency)
- If R + W ≤ N: Eventual consistency (faster but may read stale)
- Example: N=3, R=2, W=2 → R+W=4 > N=3 → Strong consistency

Thought 2: Read-your-writes consistency
- Guarantee: You see your own writes immediately
- Others may see stale data (eventual for them)
- Implementation: Sticky sessions or read from write replica
- Use case: User updates profile, immediately refreshes page

Thought 3: Monotonic reads
- Guarantee: Time only moves forward (never see older data)
- Prevents: User seeing a comment, refreshing, comment disappears
- Implementation: Sticky sessions or version tracking
- Use case: Social media feeds

Thought 4: Session consistency
- Guarantee: Strong consistency within a user session
- Eventual consistency across different users/sessions
- Implementation: Route session to same datacenter
- Use case: Shopping cart (user's own cart always consistent)

Insight: Consistency levels are a spectrum, not binary. Choose based on requirements.
```

---

### Depth 3: Integration & Validation

**Tool:** `reflection:reflect`

**Prompt:**
```
Validate my understanding of eventual consistency:

Can I explain:
1. When to use eventual consistency vs strong consistency?
2. How to handle conflicts in eventually consistent systems?
3. What consistency levels exist and when to use each?
4. How to implement eventual consistency in practice?

Can I apply this to a real scenario?
```

**Reflection Output:**
```
Validation test: Design a notification system

Scenario: Multi-region notification system (email, push, SMS)
- Users in US, EU, Asia
- Must be highly available (99.9% uptime)
- Notifications can have slight delay (<5 seconds acceptable)
- Must not send duplicate notifications

Question: Should this use eventual consistency or strong consistency?

Your answer:
"Use eventual consistency because:
1. Availability is critical (99.9% uptime requirement)
2. Notifications can tolerate short delays
3. Multi-region requires replication
4. Strong consistency would add 100-300ms cross-region latency

Conflict resolution strategy:
- Use idempotency tokens (UUID per notification)
- Deduplicate using CRDT OR-Set or similar
- If same notification written to multiple regions, merge by idempotency token

Consistency level:
- Writes: W=1 (write to local region, replicate async)
- Reads: R=1 (read from local region)
- R+W=2, N=3 → R+W < N → Eventual consistency ✓

Failure mode handling:
- Duplicate notifications: Mitigated by idempotency tokens
- Lost notifications: Retry mechanism with exponential backoff
- Delayed notifications: Acceptable per requirements

Implementation:
- Use DynamoDB with global tables (eventual consistency by default)
- Idempotency token as primary key (prevents duplicates)
- TTL for cleanup (notifications expire after 30 days)
- Monitor replication lag (alert if >10 seconds)"

✅ **Validation passed**

You demonstrated:
- Correct application of eventual consistency principles
- Understanding of trade-offs (availability vs consistency)
- Practical conflict resolution strategy
- Awareness of failure modes and mitigations
- Ability to choose appropriate consistency level
- Implementation specifics (idempotency, CRDT concepts)

Minor gaps remaining:
- Didn't mention monitoring/observability details
- Didn't discuss testing strategy for race conditions

Overall understanding: 88% - Strong grasp of concept and application
```

---

### Learning Deep Dive Summary

**Confidence: 88%** ✅

**Learning outcomes:**
1. âœ… Understand eventual consistency concept and CAP theorem trade-offs
2. âœ… Know conflict resolution strategies (LWW, vector clocks, CRDTs)
3. âœ… Understand consistency levels (quorum, read-your-writes, monotonic, session)
4. âœ… Can apply to real-world scenarios (notification system example)
5. âœ… Aware of practical implementation considerations

**Remaining knowledge gaps (12%):**
- Testing strategies for eventually consistent systems
- Monitoring and observability best practices
- Advanced CRDT types and algorithms
- Performance tuning of consistency levels

**Recommendation:** Understanding sufficient for architecture decision-making. Deepen knowledge further only if implementing from scratch.

**Total token usage: ~18K**

---

## Pattern 5: API Design (Progressive Deepening)

**Scenario:** Design a RESTful API for a task management system.

**Goal:** Create API specification with 85%+ confidence.

### Depth 0: Initial Design

**Tool:** `mcp-sequentialthinking-tools:sequentialthinking_tools`

```
Thought 1: Identify core resources.
- Tasks (main entity)
- Users (task owners/assignees)
- Projects (task grouping)
- Comments (task discussions)

Thought 2: Design endpoints (CRUD operations).
Tasks:
- GET /tasks - List all tasks
- GET /tasks/:id - Get single task
- POST /tasks - Create task
- PUT /tasks/:id - Update task
- DELETE /tasks/:id - Delete task

Projects:
- GET /projects - List projects
- GET /projects/:id - Get single project
- POST /projects - Create project

Comments:
- GET /tasks/:id/comments - List comments on task
- POST /tasks/:id/comments - Add comment

Thought 3: Request/response formats.
Example: Create task
Request:
```json
{
  "title": "Fix bug #123",
  "description": "...",
  "assignee_id": 42,
  "due_date": "2024-12-31",
  "priority": "high"
}
```

Response:
```json
{
  "id": 1,
  "title": "Fix bug #123",
  "created_at": "2024-01-01T10:00:00Z",
  ...
}
```

Thought 4: Authentication & authorization.
- Use JWT tokens in Authorization header
- Users can only view/edit tasks they own or are assigned to
- Project owners have full access to project tasks

Thought 5: Pagination & filtering.
- GET /tasks?page=1&per_page=20
- GET /tasks?status=completed&assignee_id=42
- GET /tasks?sort_by=due_date&order=asc

Thought 6: Initial confidence.
- Basic CRUD endpoints defined ✓
- Standard REST conventions followed ✓
- But: Missing error handling, rate limiting, versioning
- But: No consideration for performance (N+1 queries)
- But: Authorization logic not detailed

Confidence: 54% - Basic design but many gaps
```

---

### Depth 1: Design Critique

**Tool:** `reflection:reflect`

**Prompt:**
```
Find design flaws in this API specification:

Endpoints:
- GET /tasks
- POST /tasks
- PUT /tasks/:id
- DELETE /tasks/:id
- GET /tasks/:id/comments
- POST /tasks/:id/comments

Considerations: REST principles, security, scalability, usability
```

**Reflection Output:**
```
Design flaws and missing considerations:

1. **Missing API versioning**
   - No version in URL or headers
   - Future breaking changes will break all clients
   - Fix: Use /v1/tasks or Accept: application/vnd.api.v1+json

2. **Inconsistent nested resources**
   - Comments nested under tasks: /tasks/:id/comments ✓
   - But projects not connected: How to get tasks for a project?
   - Should add: GET /projects/:id/tasks

3. **PUT vs PATCH confusion**
   - PUT /tasks/:id assumes full replacement
   - PATCH /tasks/:id better for partial updates
   - Current design forces clients to send all fields

4. **Missing error handling specification**
   - What error codes returned? (400, 401, 404, 500?)
   - What error format?
   - Example:
   ```json
   {
     "error": {
       "code": "TASK_NOT_FOUND",
       "message": "Task with ID 123 not found",
       "details": {}
     }
   }
   ```

5. **No rate limiting specified**
   - How many requests per user per minute?
   - What happens when exceeded?
   - Should return: 429 Too Many Requests + Retry-After header

6. **Pagination not standardized**
   - Query params (page, per_page) are fine
   - But missing: Total count, next/prev links
   - Should follow RFC 5988 (Link header) or include in response:
   ```json
   {
     "data": [...],
     "pagination": {
       "total": 100,
       "page": 1,
       "per_page": 20,
       "total_pages": 5
     }
   }
   ```

7. **Filtering and search unclear**
   - GET /tasks?status=completed works for simple filters
   - But complex queries (multiple conditions, OR logic)?
   - Consider: Query language or POST /tasks/search

8. **No bulk operations**
   - What if user wants to mark 50 tasks as complete?
   - Should add: PATCH /tasks with array of IDs
   - Or: POST /tasks/bulk-update

9. **Missing relationships in responses**
   - Task response has assignee_id but not assignee details
   - Force client to make N+1 requests
   - Should support: GET /tasks?include=assignee,project

10. **No webhooks or real-time updates**
    - How do clients know when tasks updated?
    - Polling is inefficient
    - Consider: WebSocket endpoint or webhooks

11. **Security concerns**
    - No mention of HTTPS requirement
    - No CORS policy specified
    - No input validation rules (max length, allowed characters)

12. **Performance not addressed**
    - No caching headers (ETag, Last-Modified)
    - No compression (Accept-Encoding: gzip)
    - No field selection (GET /tasks?fields=id,title)
```

---

### Depth 2: Refined Design

**Synthesis of critiques:**

**Improved API Specification v1:**

```yaml
API Version: v1
Base URL: https://api.example.com/v1
Authentication: Bearer token in Authorization header
Rate Limit: 1000 requests/hour per user

Endpoints:

# Tasks
GET /tasks
  Query params:
    - page (int, default: 1)
    - per_page (int, default: 20, max: 100)
    - status (enum: todo|in_progress|completed)
    - assignee_id (int)
    - project_id (int)
    - sort_by (enum: created_at|due_date|priority, default: created_at)
    - order (enum: asc|desc, default: desc)
    - include (comma-separated: assignee,project,comments)
    - fields (comma-separated: id,title,status,...)
  Response:
    200 OK
    {
      "data": [{ task objects }],
      "pagination": {
        "total": 100,
        "page": 1,
        "per_page": 20,
        "total_pages": 5
      },
      "links": {
        "self": "/v1/tasks?page=1",
        "next": "/v1/tasks?page=2",
        "prev": null,
        "first": "/v1/tasks?page=1",
        "last": "/v1/tasks?page=5"
      }
    }
  Headers:
    - Link: RFC 5988 pagination links
    - X-Total-Count: Total number of tasks
    - ETag: Cache validation

GET /tasks/:id
  Query params:
    - include (comma-separated: assignee,project,comments)
  Response:
    200 OK - Task found
    404 NOT FOUND - Task not found
  Headers:
    - ETag: For caching

POST /tasks
  Request:
    {
      "title": "string (required, max 200 chars)",
      "description": "string (optional, max 5000 chars)",
      "assignee_id": "int (optional)",
      "project_id": "int (optional)",
      "due_date": "ISO 8601 date (optional)",
      "priority": "enum: low|medium|high (default: medium)",
      "status": "enum: todo|in_progress|completed (default: todo)"
    }
  Response:
    201 CREATED - Task created
    400 BAD REQUEST - Validation error
    401 UNAUTHORIZED - Invalid token
    403 FORBIDDEN - Insufficient permissions
  Headers:
    - Location: /v1/tasks/:id

PATCH /tasks/:id
  Request: Partial task update (any subset of fields)
  Response:
    200 OK - Task updated
    400 BAD REQUEST - Validation error
    404 NOT FOUND - Task not found
    409 CONFLICT - Concurrent modification (use ETag)

DELETE /tasks/:id
  Response:
    204 NO CONTENT - Task deleted
    404 NOT FOUND - Task not found

POST /tasks/bulk-update
  Request:
    {
      "task_ids": [1, 2, 3],
      "updates": {
        "status": "completed"
      }
    }
  Response:
    200 OK
    {
      "updated": 3,
      "failed": []
    }

# Projects
GET /projects/:id/tasks
  (Same as GET /tasks but filtered by project)

# Comments
GET /tasks/:id/comments
POST /tasks/:id/comments
  (Similar structure to tasks)

# Error format (all error responses)
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Human-readable message",
    "details": {
      "field": "title",
      "issue": "Title cannot be empty"
    }
  }
}

# Error codes
- VALIDATION_ERROR (400)
- UNAUTHORIZED (401)
- FORBIDDEN (403)
- NOT_FOUND (404)
- CONFLICT (409)
- RATE_LIMIT_EXCEEDED (429)
- INTERNAL_ERROR (500)

# Security
- HTTPS only (reject HTTP)
- CORS: Allow specific origins only
- Input validation: Strict limits on all fields
- SQL injection protection: Parameterized queries
- Rate limiting: 1000 req/hour per user

# Performance
- Caching: ETag + Last-Modified headers
- Compression: gzip/brotli support
- Field selection: ?fields=id,title reduces payload
- Include expansion: ?include=assignee avoids N+1 queries
```

**Confidence after refinement: 78%** (improved but still gaps)

---

### Depth 3: Edge Cases & Final Validation

**Tool:** `reflection:reflect`

**Prompt:**
```
Validate this API design against edge cases:

1. What happens when user deletes a task that others are commenting on?
2. How to handle task assignments to non-existent users?
3. What if two clients update same task simultaneously (race condition)?
4. How to handle very large result sets (millions of tasks)?
5. What about data privacy (user A shouldn't see user B's tasks)?
```

**Reflection Output:**
```
Edge case handling:

1. **Cascading deletes**
   - DELETE /tasks/:id should soft-delete (mark as deleted, keep data)
   - Comments remain accessible for audit trail
   - Add: ?permanently=true for hard delete (admin only)

2. **Invalid foreign keys**
   - POST /tasks with invalid assignee_id should return 400 BAD REQUEST
   - Validation: Check user exists before creating task
   - Return specific error: { "error": { "code": "INVALID_ASSIGNEE", "message": "User 123 not found" } }

3. **Concurrent modification**
   - Use ETag for optimistic locking
   - Client sends If-Match: "etag-value" header
   - If ETag changed, return 409 CONFLICT
   - Client must GET latest version and retry

4. **Large result sets**
   - Cursor-based pagination for stable results:
     GET /tasks?cursor=abc123&limit=20
   - Don't allow per_page > 100
   - For analytics/exports, provide separate endpoint:
     POST /tasks/export → Returns async job ID
     GET /export-jobs/:id → Download when ready

5. **Authorization & data privacy**
   - Row-level security: Filter tasks by user permissions
   - GET /tasks only returns tasks where:
     * user is owner, OR
     * user is assignee, OR
     * user is project member
   - Implement via database query filters (don't filter in app layer)
   - Add audit log for sensitive operations

6. **Idempotency for POST requests**
   - POST /tasks should support Idempotency-Key header
   - Prevent duplicate task creation on network retry
   - Cache operation result for 24 hours

7. **Rate limiting edge cases**
   - Burst allowance: 100 req/min + 1000 req/hour
   - Return rate limit headers on all responses:
     X-RateLimit-Limit: 1000
     X-RateLimit-Remaining: 850
     X-RateLimit-Reset: 1640000000
   - On 429 response, return Retry-After header

8. **API deprecation process**
   - When introducing breaking changes in v2:
     * Keep v1 running for 12 months
     * Return Sunset header: Sunset: Sat, 31 Dec 2024 23:59:59 GMT
     * Add deprecation warning header
     * Provide migration guide
```

---

### Final API Specification (Depth 3)

**Confidence: 91%** ✅

**Complete API Design:**

All previous features PLUS:

**Additional specifications:**

1. **Soft delete by default**
   ```
   DELETE /tasks/:id → Marks as deleted (recoverable)
   DELETE /tasks/:id?permanently=true → Hard delete (admin only)
   GET /tasks?include_deleted=true → Include soft-deleted (admin only)
   ```

2. **Optimistic locking**
   ```
   GET /tasks/:id → Returns ETag header
   PATCH /tasks/:id with If-Match: "etag" header
   If ETag mismatch → 409 CONFLICT
   ```

3. **Cursor pagination for stability**
   ```
   GET /tasks?cursor=abc123&limit=20
   Response includes: "next_cursor": "def456"
   ```

4. **Idempotency**
   ```
   POST /tasks with Idempotency-Key: uuid header
   Duplicate requests return cached result (201 or 200)
   ```

5. **Async exports**
   ```
   POST /tasks/export → Returns { "job_id": "abc123" }
   GET /export-jobs/abc123 → Returns status + download URL when ready
   ```

6. **Rate limiting headers**
   ```
   X-RateLimit-Limit: 1000
   X-RateLimit-Remaining: 950
   X-RateLimit-Reset: 1640000000 (Unix timestamp)
   ```

7. **Authorization model**
   ```
   Task visibility rules:
   - Owner: Full access
   - Assignee: Read + update status
   - Project member: Read only
   - Others: No access
   
   Enforcement: Database query filters, not app layer
   ```

8. **Comprehensive error handling**
   ```json
   {
     "error": {
       "code": "VALIDATION_ERROR",
       "message": "Invalid request data",
       "details": [
         {
           "field": "due_date",
           "message": "Must be a future date",
           "value": "2020-01-01"
         }
       ],
       "request_id": "req_abc123",
       "documentation_url": "https://docs.api.example.com/errors/validation"
     }
   }
   ```

9. **Webhooks for real-time updates**
   ```
   POST /webhooks
   {
     "url": "https://client.com/webhook",
     "events": ["task.created", "task.updated", "task.deleted"],
     "secret": "webhook_secret"
   }
   
   Webhook payload:
   {
     "event": "task.updated",
     "task": { task object },
     "timestamp": "2024-01-01T10:00:00Z",
     "signature": "HMAC-SHA256 signature"
   }
   ```

10. **API health & status**
    ```
    GET /health → { "status": "healthy", "version": "1.0.0" }
    GET /status → Detailed system status (admin only)
    ```

**Documentation requirements:**
- OpenAPI 3.0 specification
- Interactive API explorer (Swagger UI)
- Code examples in 3+ languages
- Migration guides for version upgrades

**Monitoring requirements:**
- Log all API requests (request ID, user ID, endpoint, status, latency)
- Alert on error rate > 1%
- Alert on P95 latency > 500ms
- Track rate limit hits

**Testing requirements:**
- Unit tests for all endpoints
- Integration tests for workflows
- Load tests (target: 1000 req/sec)
- Security tests (OWASP Top 10)

**Remaining considerations (9%):**
- GraphQL alternative (if clients request)
- gRPC for internal services
- API gateway vs direct access
- Multi-tenancy isolation

**Recommendation:** API specification is production-ready. Remaining 9% are nice-to-haves or future enhancements.

**Total token usage: ~30K**

---

## Summary: Pattern Selection Guide

**Choose Deep Dive (Pattern 1) when:**
- Complex technical problem with many moving parts
- Need to balance multiple trade-offs
- Solution requires validation before implementation
- Target: 85-92% confidence

**Choose Decision Framework (Pattern 2) when:**
- Multiple viable options exist
- Need to weigh factors systematically
- High-stakes decision with long-term impact
- Target: 85-92% confidence

**Choose Validation Loop (Pattern 3) when:**
- Reviewing code, designs, or solutions
- Need to catch errors before production
- Security or correctness critical
- Target: 90%+ confidence

**Choose Learning Deep Dive (Pattern 4) when:**
- Need to master unfamiliar concept
- Architectural decision requires deep understanding
- Teaching or explaining to others
- Target: 85-92% understanding confidence

**Choose Progressive Deepening (Pattern 5) when:**
- Creating specifications or designs from scratch
- Need comprehensive coverage of edge cases
- Building foundation for team collaboration
- Target: 85-92% confidence

**Token budget awareness:**
- Simple patterns: 15-20K tokens
- Complex patterns: 25-35K tokens
- Multi-pattern workflows: 40-60K tokens
- Critical: Monitor and warn at 80% (152K/190K)

---

## Meta: Using These Patterns

**How to select pattern:**
1. Read problem description
2. Match to pattern characteristics above
3. Follow pattern's depth progression
4. Track confidence at each level
5. Stop when threshold met

**How to adapt patterns:**
- Adjust depth levels based on complexity
- Combine patterns if needed (e.g., Decision + Validation)
- Scale token usage to problem criticality
- Trust the process: Let confidence guide iteration

**Common mistakes:**
- Skipping depth levels (leads to low confidence)
- Over-analyzing (going past threshold)
- Using wrong pattern (slows progress)
- Ignoring token budget (hitting limit)

**Success indicators:**
- Confidence increases steadily (10-20% per depth)
- Insights are specific and actionable
- Edge cases systematically addressed
- Clear implementation path emerges

---

End of patterns.md
