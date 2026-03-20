---
name: MODULE-REFERENCE
description: Comprehensive module reference for Make.com covering configuration, parameters, input/output structures, patterns, troubleshooting, and API integration examples.
context7_sources:
  - /websites/developers_make_com-api-documentation
---

# Make.com Module Reference Guide (v2.1)

## HTTP & API Modules

### Make a Request

**Purpose**: Execute custom HTTP requests (GET/POST/PUT/PATCH/DELETE) to any API endpoint.

**Configuration**:
- **URL**: Target endpoint; supports variables `{{baseURL}}/users/{{userId}}`
- **Method**: GET, HEAD, POST, PUT, PATCH, DELETE
- **Headers**: Authorization, Content-Type, custom headers. Use `Bearer {{connection.apiToken}}` for OAuth
- **Query String**: Key-value pairs appended to URL
- **Body**: Raw, JSON, Form data (x-www-form-urlencoded), Multipart (file uploads)
- **Authentication**: Use Connections for OAuth/API keys (preferred over hardcoding)
- **Request Timeout**: Default 40 minutes for Pro; max 300 seconds for advanced settings
- **Parse Response**: Auto-parse JSON/XML into mappable fields
- **Handle Errors**: Evaluate all non-2xx/3xx as errors (optional toggle)

**Input/Output**: Maps from previous modules. Output is response body + status code, headers, timing metadata.

**Common Patterns**:
```
// Chain multiple requests
1. GET https://api.example.com/users/{{userId}}  → Extract customerId
2. POST https://api.example.com/orders with body { "customerId": "{{customerId}}" }

// Add authorization header
Header: Authorization = Bearer {{connection.apiToken}}

// Handle large payloads
Set timeout to 300s, use async pattern (initiate → callback webhook)
```

**Error Handling**:
- 401 Unauthorized: Token expired/invalid; re-authorize connection
- 429 Too Many Requests: Add Break error handler with exponential backoff
- 500 Internal Server: Add Break handler; service likely recovering
- Timeout: Increase request timeout or redesign with async webhook callback

**API Configuration Example** (from Make API docs):
```json
{
  "url": "https://eu1.make.com/api/v2/scenarios/112",
  "method": "get",
  "headers": [
    { "name": "Authorization", "value": "YOUR_API_KEY" }
  ],
  "parseResponse": true,
  "timeout": "40",
  "followRedirect": true,
  "rejectUnauthorized": true
}
```

### Make an OAuth 2.0 Request

**Purpose**: Interact with OAuth 2.0 protected APIs when native Make connection doesn't exist.

**Configuration**:
- Authorization URL: Where user logs in
- Token URL: Endpoint that issues tokens
- Client ID / Client Secret: From app registration
- Scopes: What permissions to request (e.g., `openid profile email`)
- Make handles token refresh automatically; re-authorize on expiry

**When to Use**: For integrating with less common APIs or requiring granular OAuth control.

**Example**:
```
Authorization URL: https://oauth.example.com/authorize
Token URL: https://oauth.example.com/token
Client ID: your_client_id
Client Secret: your_client_secret (from Connections)
Scopes: openid profile email
```

---

## Flow Control Modules

### Router

**Purpose**: Conditional branching; split scenario into multiple paths based on conditions.

**Configuration**:
- Create multiple routes (branches)
- Each route checked sequentially in creation order
- Attach filters to each connection defining conditions
- Set final route as fallback (catches unmatched cases)
- Order matters: most specific first

**Input/Output**: Single input bundle → multiple possible outputs (ONE per route).

**Example**:
```
Router
├── Route 1: Filter [{{order.total}} > 100] → Premium flow → Send to Priority
├── Route 2: Filter [{{order.total}} > 0] → Standard flow → Send to Standard Queue
└── Route 3: (Fallback, no filter) → Error flow → Send to Manual Review
```

**Key Points**:
- A single bundle only triggers ONE route (it doesn't split into parallel executions)
- Routes evaluated sequentially; if Route 1 matches, Routes 2/3 don't execute
- No fallback + no matches = scenario continues silently (likely bug)
- Performance: 10+ routes slow down; prefer single Router or nested Routers

**Best Practice**: Always set a fallback route to catch unexpected cases.

### Filter

**Purpose**: Single-condition gate; stops execution if false, continues if true.

**Operators**: 
- `Equals`, `Not equals`
- `Greater than`, `Less than`, `Between`
- `Contains` (text search), `Not contains`
- `Matches pattern` (regex)
- `Exists` (null check), `Is empty`
- `In array`, `Not in array`

**Pattern Example**:
```
IF {{order.status}} == "completed" THEN continue
ELSE stop
```

**Advanced Technique**: Use filters as manual breakpoints during debugging—set condition to always false (e.g., `1 = 2`), run scenario, inspect execution up to that point.

### Iterator

**Purpose**: Process array items one-by-one; downstream modules execute once per item.

**Configuration**: Input array from previous module. Iterator creates separate cycles (executions) for each item.

**Example**:
```
Iterator over {{array_of_customers}}
  → Downstream modules execute once per customer
  → Each cycle processes one customer independently
  → Total operations = (array length) × (downstream modules)
```

**Cost Consideration**: 
- Array of 100 items × 10 modules = 1000 operations minimum
- Solution: Use Aggregator after Iterator to consolidate, then bulk API call

**Gotcha**: Iterator doesn't create parallel execution; cycles run sequentially (one-by-one).

### Aggregator

**Purpose**: Consolidate multiple iterator cycles back into single array.

**Configuration**: 
- Specify target structure (fields to collect)
- For each cycle, map data into aggregator fields
- After iterator completes, aggregator outputs consolidated array

**Pattern**: `Iterator → Aggregator → Batch API call`

**Example**:
```
Iterator (1000 customers)
  → Transform customer data
  → Aggregator collects all transformed customers
  → Google Sheets Add Rows (bulk) adds 1000 at once
  
Result: 1-3 credits vs. 1000+ one-by-one
```

**Key Difference**: Iterator splits; Aggregator consolidates. Together = efficient batch processing.

---

## Triggers

### Webhooks > Custom Webhook

**Purpose**: Real-time trigger from external systems or other scenarios.

**Configuration**:
- Generates unique HTTPS URL specific to scenario
- Optional: Require API key, IP whitelist, payload validation
- Supports synchronous (caller waits) and asynchronous (fire-and-forget) patterns

**Security Best Practices**:
- Always use HTTPS (Make default)
- Enable API key requirement for public webhooks
- IP whitelist if caller has static IP
- Validate payload structure before processing
- Rotate keys regularly

**Webhook Response Module**: For synchronous patterns, send response back to caller with custom status/body.

**API Example** (Make API to manage webhooks):
```bash
# Get all webhooks
GET https://eu1.make.com/api/v2/hooks
Authorization: YOUR_API_KEY

# Get webhook logs (execution history)
GET https://eu1.make.com/api/v2/hooks/{hookId}/logs
Authorization: YOUR_API_KEY
Response: { hookLogs: [ { statusId: 1, loggedAt: "...", data: {...} } ] }
```

### Scheduled Trigger

**Purpose**: Trigger scenario on a schedule.

**Frequencies**: 
- Once daily
- Multiple times per day (every 30 min, every 2 hours, etc.)
- Weekly (specific day/time)
- Monthly (specific date/time)
- Custom cron expression

**Time Zone**: Defaults to UTC; be explicit when scheduling for specific regions.

**Example**: "Run every Monday at 9 AM Eastern Time" → Convert to UTC (1 PM UTC) → Set in Make with UTC timezone.

### Watch Field for Changes

**Purpose**: Monitor app records for field-level updates (instant trigger).

**Use Case**: Trigger when Salesforce Lead Status changes, or Airtable field updated.

**Example**: Watch Salesforce → Trigger when Status field = "Qualified" → Start follow-up workflow.

---

## Data Transformation

### Text Parser > Match Pattern

**Purpose**: Extract structured data from unstructured text using regex.

**Configuration**: 
- Define regex pattern with capture groups
- Parser outputs each capture group as separate field

**Example** (extract phone number):
```
Pattern: \+?1?\s?(\d{3})\s?(\d{3})\s?(\d{4})
Input: "+1 (234) 567-8901"
Output: area_code=234, exchange=567, number=8901
```

**Common Patterns**:
- Email: `([a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,})`
- URL: `(https?:\/\/[^\s]+)`
- JSON key: `"name":\s*"([^"]+)"`

### JSON Operations

**Parse JSON**: Convert JSON string to mappable object/array.
```
Input: '{"user": {"name": "Alice", "email": "[email protected]"}}'
Output: {{body.user.name}} = "Alice"
```

**Create JSON**: Visually build JSON structure by mapping fields.

**Stringify**: Convert object/array back to JSON string for APIs expecting JSON payload.

**Pattern**: API returns nested JSON → Parse → Router checks status → Aggregator rebuilds.

### Array Functions

| Function | Example | Result |
|----------|---------|--------|
| `map()` | `{{map(users; "email")}}` | Extract email field from array |
| `length()` | `{{length(array)}}` | Count array items (100) |
| `flatten()` | `{{flatten(nestedArray)}}` | Collapse nested arrays |
| `deduplicate()` | `{{deduplicate(emails)}}` | Remove duplicate values |
| `slice()` | `{{slice(array; 5; 10)}}` | Extract items 5-10 |
| `join()` | `{{join(array; ", ")}}` | Array to comma-separated string |
| `unique()` | `{{unique(array)}}` | Unique values only |

### Date/Time Functions

| Function | Example | Result |
|----------|---------|--------|
| `formatDate()` | `{{formatDate(now; "YYYY-MM-DD")}}` | Format current date as 2025-01-15 |
| `parseDate()` | `{{parseDate("2025-01-15"; "YYYY-MM-DD")}}` | Parse string to date |
| `addMonths()` | `{{addMonths(now; -1)}}` | One month ago |
| `addDays()` | `{{addDays(now; 7)}}` | One week from now |
| `now` | `{{now}}` | Current Unix timestamp |
| `formatDate() with timezone` | `{{formatDate(date; "YYYY-MM-DD HH:mm"; "America/New_York")}}` | Format with timezone |

**Timezone Handling**: Always specify timezone when parsing or formatting:
```
Parse: {{parseDate(date_string; "YYYY-MM-DD"; "America/New_York")}}
Format: {{formatDate(timestamp; "YYYY-MM-DD HH:mm"; "America/New_York")}}
```

### String Functions

| Function | Example |
|----------|---------|
| `split()` | `{{split("a,b,c"; ",")}}` → `["a", "b", "c"]` |
| `trim()` | `{{trim("  hello  ")}}` → `"hello"` |
| `capitalize()` | `{{capitalize("hello")}}` → `"Hello"` |
| `lower()` | `{{lower("HELLO")}}` → `"hello"` |
| `upper()` | `{{upper("hello")}}` → `"HELLO"` |
| `replace()` | `{{replace("hello"; "l"; "L")}}` → `"heLLo"` |
| `substring()` | `{{substring("hello"; 1; 3)}}` → `"el"` |
| `contains()` | `{{contains("hello"; "ell")}}` → `true` |
| `startsWith()` | `{{startsWith("hello"; "he")}}` → `true` |

### Math Functions

| Function | Example |
|----------|---------|
| `add()` | `{{add(5; 3; 2)}}` → `10` |
| `subtract()` | `{{subtract(10; 3)}}` → `7` |
| `multiply()` | `{{multiply(4; 5)}}` → `20` |
| `divide()` | `{{divide(20; 4)}}` → `5` |
| `round()` | `{{round(3.7)}}` → `4` |
| `floor()` | `{{floor(3.7)}}` → `3` |
| `ceil()` | `{{ceil(3.2)}}` → `4` |
| `min()` | `{{min(5; 2; 8)}}` → `2` |
| `max()` | `{{max(5; 2; 8)}}` → `8` |

---

## Error Handling Modules

### Error Handler Routes

Attach to critical modules to define failure behavior.

**Ignore**: Skip failed module, continue to next.
- ⚠️ Use rarely—data loss risk
- Exception: Optional operations where failure is acceptable

**Resume**: Use fallback data; downstream receives fallback.
```
HTTP Call to enrichment API
  ├── Success: Use enriched data
  └── Error Handler (Resume): Use {{message: "Enrichment unavailable"}}
      → Downstream modules process fallback
```

**Rollback**: Undo transactional operations (database modules only).
```
Salesforce Update Contact
  ├── Success: Record updated
  └── Error Handler (Rollback): Undo update, scenario stops
```

**Break**: Retry with exponential backoff; ideal for transient errors.
```
HTTP Call (rate limited)
  └── Error Handler (Break)
      ├── Retry count: 5
      ├── Interval: 1 second (doubles: 1→2→4→8→16)
      └── Max retries exceeded: Continue with Resume (default data)
```

**Commit**: Save completed operations before stopping.
```
Batch Insert 10K records (Aggregator)
  └── Error Handler (Commit)
      ├── Success: All 10K inserted
      └── Fail after 8K: Commit 8K, stop (vs. lose all)
```

**Configuration Example** (from Make API docs):
```json
{
  "module": "builtin:Break",
  "mapper": {
    "count": "5",
    "retry": true,
    "interval": "1"
  },
  "version": 1
}
```

---

## Data Stores

### Add/Replace Record

**Purpose**: Store key-value data locally in Make.

**Configuration**:
- **Data Store Name**: Auto-created if doesn't exist
- **Key**: Unique identifier (e.g., user_id, email, API_response_id)
- **Value**: Single or multiple fields (Name, Email, Timestamp, etc.)

**Use Cases**:
- Cache API responses (check before calling, save result)
- Maintain state between scenario executions
- Lookup tables (customer tiers, product codes)
- Inter-scenario communication (one scenario writes, another reads)

**Performance**: 10-100x faster than external API calls for small data.

**Example**:
```
Data Store: "customer_enrichment_cache"
Key: {{leadId}}
Fields:
  - enriched_email: {{enrichedEmail}}
  - company: {{company}}
  - last_updated: {{now}}
```

### Get/Search Records

**Purpose**: Retrieve data from Data Store.

**Options**:
- **Get by Key**: Exact match; returns single record
- **Search**: Field conditions (Equals, Contains, Greater than); returns array

**Pattern** (Caching with TTL):
```
1. Get from Data Store by key
2. If found && timestamp < 1 hour old: Use cached value
3. Else: API call → Save to Data Store → Use result
```

---

## AI Modules (2025 Native)

### Run an Agent

**Purpose**: Execute LLM-powered agent that reasons and uses tools autonomously.

**Configuration**:
- **Agent**: Select from Agents section (pre-configured with tools)
- **Input**: Natural language goal/prompt
- **Output**: Final result + execution trace (shows reasoning steps)

**When to Use**: Complex decision-making, multi-step research, unstructured input analysis.

**Example**:
```
Agent Goal: "Analyze this support ticket and route to appropriate team"
Agent Tools: [Zendesk lookup, Team availability API, Customer history]
Agent Reasoning: "Ticket is urgent + Customer is VIP + Team A available → Route to A, escalate immediately"
Output: { team: "Team A", priority: "urgent", action: "escalate" }
```

**Gotchas**:
- Higher operation cost (LLM inference)
- Slower than direct module calls
- Subject to hallucination—validate outputs with Router before action
- Curate tools carefully; don't expose sensitive/irreversible tools

### OpenAI > Create a Completion

**Purpose**: Call GPT models (GPT-5, GPT-4.5, GPT-4o, GPT-4o-mini).

**Configuration**:
- **Model**: Select version (GPT-5, GPT-4.5, o3, GPT-4o, GPT-4o-mini)
- **Temperature**: 0 (deterministic) to 1 (creative); default 0.7
- **Max Tokens**: Output limit (e.g., 1000)
- **System/User/Assistant Messages**: Conversation history

**Multimodal**:
- DALL-E: Generate image from description
- Vision: Analyze image content (GPT-4o)
- Whisper: Transcribe audio

**Cost Optimization**: Use GPT-4o-mini for high-volume tasks; reserve GPT-5/o3 for complex reasoning.

### AI Content Extractor

**Purpose**: Extract structured data from images, PDFs, audio.

**Modules**:
- Extract text from image (OCR)
- Extract information from invoice (structured fields)
- Extract text from document (PDFs)
- Transcribe audio file
- Describe image / Generate caption

**Example** (Invoice Processing):
```
Input: PDF invoice file
Output: {
  invoice_number: "INV-001",
  date: "2025-01-15",
  vendor: "Acme Corp",
  total: 1000.00,
  items: [{ description: "...", qty: 1, price: 500 }]
}
```

---

## Webhooks & Inter-Scenario Communication

### Webhook Response

**Purpose**: Send synchronous response back to webhook caller.

**Configuration**:
- **Status Code**: 200 (success), 201 (created), 400 (error), 404, etc.
- **Response Body**: JSON, text, or HTML

**Pattern** (Synchronous):
```
Caller POSTs data to webhook → 
Scenario processes → 
Webhook Response returns result → 
Caller receives response immediately
```

### Webhook Chaining

**Purpose**: Trigger another scenario from current scenario.

**Implementation**: HTTP Make Request to target scenario's webhook URL.

**Sequential Workflow**:
```
Scenario A:
  → Process data
  → HTTP POST to Scenario B's webhook URL
  → Scenario B starts immediately
  → Scenario B completes
```

---

## Advanced Patterns & Architectures

### Batch Processing Pipeline (Efficient)

```
Trigger (new data) 
  → Iterator (per item)
    → Transform (Text Parser, JSON)
    → Filter (validate)
    → Aggregator (collect ALL transformed items)
  → Batch API call (Google Sheets Add Rows: add 1000+ rows in ONE call)
  → Error handler: Break (retry) → Commit (save partial progress)

Cost: 1000 items = 3-5 credits vs. 1000+ one-by-one
```

### Multi-Level Routing (Complex Logic)

```
Router 1 (by country)
  ├── US → Router 2 (by state)
  │   ├── CA → California-specific logic
  │   └── TX → Texas-specific logic
  └── EU → Router 3 (by regulation)
      ├── GDPR compliance (Europe)
      └── Local storage requirements
```

### AI-Powered Conditional Routing

```
Run AI Agent: "Analyze sentiment, route to appropriate queue"
  → Agent's tools: [NLP sentiment analysis, CRM lookup]
  → Agent outputs: sentiment (positive/negative), team (support/sales/product)
  → Router based on agent output
    ├── Positive + Sales opportunity → Sales queue
    ├── Negative + Urgent → Support queue
    └── Neutral → General queue
```

### Real-Time Observability with Make Grid

```
Make Grid shows:
  ├── All scenarios (nodes) with real-time status
  ├── All webhooks (entry points)
  ├── All data stores (state)
  └── Interconnections (scenario→scenario calls, dependencies)

Optimize:
  1. Enable credit overlay
  2. Find expensive scenarios (red nodes)
  3. Identify bottlenecks (AI agents, nested iterators)
  4. Apply optimization (batch, cache, filter early)
  5. Compare before/after credit consumption
```

---

## Debugging Techniques

**Inspect Module Output**: After scenario run, click bubble above connection to see exact data passed. Step through data flow to locate corruption/mismatches.

**Execution History Deep Dive**: View complete HTTP request/response for API modules. Inspect both input and output bundles per module.

**Static Test Data**: Use "Set multiple variables" at start with hardcoded test data. Enables reproducible, isolated testing.

**Data Store Logging**: Insert Data Store Add module at key points to log variable state. Creates execution trace for post-run analysis.

**Regex Breakpoint**: Insert filter with always-false condition (`1 = 2`) to manually stop execution and inspect state at that point.

**Module Cloning**: Clone failing module, use router to test old vs. new config side-by-side, compare outcomes.

---

## Performance Optimization

**High-Volume Scenarios (1000+ items)**:
1. Batch process via Aggregator + bulk API calls (NOT one-by-one)
2. Filter early to prevent wasted module executions
3. Use Data Stores for lookups instead of external API calls
4. Consolidate logic into functions/regex rather than multiple Set Variable modules

**Credit Consumption Reduction**:
- Replace 10 modules with 1 HTTP call (batch operation)
- Cache externally fetched data in Data Stores
- Use cheaper models (GPT-4o-mini vs. GPT-5)
- Filter non-matching bundles before expensive modules (AI agents)

**Execution Time Optimization**:
- Parallel routes (multiple branches in router can run concurrently)
- Async patterns for long operations (initiate + webhook callback)
- Offload to batch API (OpenAI Batch API: 24 hours, 50% discount)

---

## Common Module Combinations

**Salesforce + Google Sheets**:
```
Salesforce Watch trigger → Router by record type → 
Google Sheets Add Row + Salesforce Update → 
Error resume
```

**Email + Data Processing**:
```
Gmail New Email trigger → 
AI Content Extractor extract attachment → 
Parse extracted data → 
Route to appropriate handler → 
Slack notify
```

**Webhook + Batch**:
```
Custom Webhook receive data → 
Data Store Add → 
Scheduled scenario (every 5 min) processes Data Store records in batches → 
Clear Data Store
```

**API Chain with Fallback**:
```
HTTP call API1 → 
Error Resume (default data) → 
HTTP call API2 with fallback → 
Final aggregation
```

---

## Module Configuration Checklist

- ✓ Every external API call has error handler (Ignore/Resume/Break/Commit)
- ✓ Sensitive data not logged or exposed
- ✓ Large datasets use batch operations, not one-by-one
- ✓ Rate limits handled with exponential backoff (Break handler)
- ✓ Webhook URLs secured with API keys and IP whitelisting
- ✓ Data transformations validated before downstream consumption
- ✓ Database operations use transactions with Rollback on error
- ✓ Router has fallback route for unmatched cases
- ✓ Iterator + Aggregator used for array processing
- ✓ Data Stores used for caching, not external API calls for every lookup

---

**Reference Version**: 2.1 | **Last Updated**: October 2025
