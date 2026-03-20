---
name: make-com
description: "Expert-level Make.com automation platform guidance covering scenario design, API integration, AI agents, Make Bridge, error resilience, performance optimization, enterprise observability, and Blueprint JSON structure for scenario recreation. Use for any workflow automation, integration, or orchestration challenge including fix-and-flip property analysis and scenario programmatic building."
license: MIT
metadata:
  version: "2.2"
  lastUpdated: "October 2025"
---

# Make.com: Enterprise Automation & Integration Expert Skill

## Introduction

Make.com (formerly Integromat) is the most comprehensive iPaaS for scenario automation, AI orchestration, and real-time integrations. It evolved from a visual workflow builder into a complete enterprise automation platform supporting:

- **Scenario Automation**: Connect 3,000+ applications via native modules, HTTP APIs, and webhooks
- **AI-Powered Orchestration**: Native agents, content extraction (OCR/PDF/audio), and LLM integrations
- **Real-Time Event Processing**: Instant triggers via webhooks, with webhook queue management and replay capabilities
- **Enterprise Observability**: Make Grid for visualization, incomplete execution tracking (DLQ), and credit monitoring
- **Embedded Integrations**: Make Bridge for white-label automation and custom app development
- **Programmatic Control**: Complete REST API for scenario management, webhook orchestration, and DevOps automation

As of 2025, Make transitioned from "operations" to "credits" billing (1 operation = 1 credit, with complex operations consuming multiple credits). The platform now offers enterprise features including Make Grid (3D workflow visualization), AI Agents with tool integration, and Make Bridge for embedded automation.

## When to Use This Skill

Consult this skill for: scenario architecture and troubleshooting, API integration patterns, webhook security and reliability, AI agent design, error handling and resilience, performance optimization, Make API programmatic access, Make Bridge embedded integrations, incomplete execution recovery, Make Grid ecosystem analysis, data transformation logic, credit optimization, and production operations management.

## Prerequisites & Setup

**Account Configuration**: Create a Make account, connect applications via OAuth or API authentication. For production, use dedicated connections per environment (DEV, STAGING, PROD) to prevent data leaks. Generate API keys from User Profile → API tokens for Make API access and MCP integrations.

**Regional Endpoints**: Make operates from multiple zones (EU1, EU2, US1, US2, AU1). Specify zone-appropriate endpoints:
- EU1: `https://eu1.make.com/api/v2/`
- US1: `https://us1.make.com/api/v2/`
- Check your account region under Account Settings → Region.

**Critical URLs**:
- **Dashboard**: https://make.com/
- **Help Center**: https://help.make.com/
- **Developer Hub**: https://developers.make.com/ (API, Bridge, custom apps)
- **API Reference**: https://developers.make.com/api-documentation/
- **Community**: https://community.make.com/
- **Status Page**: https://status.make.com/
- **Academy**: https://academy.make.com/

**Billing Model (2025)**:
- **Credits**: Unified billing unit; 1 operation = 1 credit (approximately)
- **Complex Operations**: AI modules, batch functions, and transformations consume multiple credits
- **Monitoring**: Use Credit Dashboard for real-time tracking; set team budgets via Operations per Team (Enterprise)
- **Optimization**: Filter data early, batch process large datasets, cache results, use Data Stores for lookups

## Core Concepts

**Scenarios**: Automation workflows consisting of trigger(s), modules, routers/filters, and error handlers. Execute on schedule, webhook trigger, app event, or manual invocation. Each scenario execution can process multiple bundles (data items).

**Modules**: Discrete actions interacting with apps or data. Types: triggers (Webhook, Scheduled), actions (Create/Update records), search/iterators, transformers (JSON, text parsing), flow control (Router, Filter), error handlers, and AI modules.

**Connections**: Secured credentials linking scenarios to external apps. Environment-scoped (DEV/STAGING/PROD). Token expiry requires re-authorization. Use unique connections per sensitive integration to prevent cascading failures.

**Bundles & Cycles**: A bundle is the data packet passed between modules. An iterator creates multiple cycles (executions of downstream modules per item), each processing one bundle at a time.

**Routers & Filters**: Routers create conditional branches; filters gate execution. Router outputs only ONE bundle per execution to the matching branch; filters continue or halt execution sequentially.

**Iterators & Aggregators**: Iterator expands arrays into individual cycles; Aggregator consolidates results back into single array. Essential for efficient batch processing (10,000+ items).

**Webhooks**: Real-time triggers via HTTP POST to unique HTTPS URLs. Support instant delivery, API keys, IP whitelisting, and payload validation. Queue overflow protection via async patterns and batch processing.

**Data Stores**: Native Make key-value storage for caching, lookups, and inter-scenario state. 10-100x faster than external APIs for small data; credit-based pricing. No size limits within org quotas.

**Make Grid** (June 2025+): Real-time 3D visualization of scenario ecosystem showing all scenarios, webhooks, data stores, and interconnections. Filters by team, status, app, or custom properties. Overlays credit consumption for optimization. Essential for enterprise impact analysis and dependency tracking.

**Make Bridge**: White-label integration platform allowing embedding Make automation into your applications. Provides API for managing integrations, users, and configurations programmatically. Uses JWT authentication with short-lived tokens.

**AI Agents** (2025+): Goal-driven LLM entities equipped with tools for autonomous reasoning and execution. Unlike scenarios (fixed-path logic), agents dynamically determine execution based on LLM reasoning. Can use tools from toolset (Salesforce lookup, CRM query, etc.) and integrate with external MCP servers.

**Make API**: RESTful API for programmatic scenario management, webhook orchestration, execution monitoring, and integration with external systems. Supports API key and OAuth authentication. Used for DevOps automation, CI/CD integration, and custom dashboard building.

**Incomplete Executions (DLQ)**: Dead Letter Queue storing scenarios that failed to complete. Accessible via API (`GET /dlqs`) for retrieval and analysis. Enables error recovery and operational alerting.

**MCP (Model Context Protocol)**: Bidirectional protocol enabling: (1) Make scenarios exposed as tools to external AI systems (e.g., Claude, other AI models), and (2) Make AI Agents connecting to external MCP servers for advanced tool capabilities.

## Module Categories & Functions

**HTTP & API Modules**:
- `Make a Request`: Custom HTTP calls (GET/POST/PUT/PATCH/DELETE) with headers, auth, body, timeouts
- `Make an OAuth 2.0 Request`: OAuth 2.0 flows for APIs without native Make connections
- `Get a File`: Download and process files from URLs or external storage

**Triggers**:
- `Webhooks > Custom Webhook`: Real-time HTTP POST with optional API key, IP whitelist, payload validation
- `Scheduled`: Cron-like execution on daily/weekly/monthly/custom schedules in UTC (convert timezones carefully)
- `Watch field for changes`: Monitor app records for field-level updates

**Flow Control**:
- `Router`: Conditional branching; evaluates routes sequentially; only ONE route executes per bundle
- `Filter`: Single-condition gate; stops if false, continues if true
- `Iterator`: Processes arrays one item per cycle; downstream modules repeat per item
- `Aggregator`: Consolidates multiple cycles back into single array; place after iterators for batch operations
- `Break/Continue/Commit`: Loop control and transactional markers

**Data Transformation**:
- `Text Parser > Match Pattern`: Regex extraction with named capture groups
- `JSON`: Parse, create, stringify JSON data
- `Array functions`: `map()`, `length()`, `flatten()`, `deduplicate()`, `slice()`
- `Date/Time`: `formatDate()`, `parseDate()`, `addMonths()`, timezone-aware conversions
- `String functions`: `split()`, `trim()`, `capitalize()`, `replace()`
- `Math`: `add()`, `multiply()`, `round()`, `min()`, `max()`

**Error Handling Routes**:
- `Ignore`: Skip failed module, continue (⚠️ data loss risk; use rarely)
- `Resume`: Use fallback data; downstream receives fallback instead of output
- `Rollback`: Undo transactional operations (database modules)
- `Break`: Retry with exponential backoff (1s, 2s, 4s, 8s...); configurable count and interval
- `Commit`: Save partial progress before stopping

**AI Modules**:
- `Run an Agent`: Execute LLM-powered agent with tools and autonomous reasoning
- `Completion` (OpenAI/Claude/Gemini): Call external LLMs with system/user messages, temperature, max tokens
- `AI Content Extractor`: OCR, PDF text extraction, audio transcription, document parsing

**Data Stores**:
- `Add/Replace Record`: Insert or update key-value data (auto-creates store if needed)
- `Get/Search Records`: Retrieve by key or search by field conditions

**Utility**:
- `Set Variable/Set Multiple Variables`: Store values for reuse in downstream modules
- `Sleep`: Pause execution (useful for rate-limit avoidance, waiting for async operations)
- `Webhooks > Webhook Response`: Send synchronous response back to webhook caller

## Essential Patterns

**1. Basic Trigger-Action Flow**
```
Webhook Trigger → HTTP Make Request → Webhook Response
```
Minimal synchronous API integration. Caller waits for response.

**2. Batch Data Processing Pipeline**
```
Trigger (new data) 
  → Iterator (per item)
    → Transform (Text Parser, JSON)
    → Filter (validate)
    → Aggregator (collect results)
  → Batch API call (Google Sheets Add Rows, bulk database insert)
  → Error handler: Break (retry) → Resume (partial commit)
```
Processes 10,000+ items in 2-3 credits vs. 10,000+ with one-by-one approach.

**3. Conditional Multi-Branch Routing**
```
Trigger
  → Router
    ├── Route 1: [Status = "Premium"] → VIP flow (priority, expedited)
    ├── Route 2: [Status = "Standard"] → Standard flow
    └── Route 3: (fallback) → Default flow
  → Consolidate → Final action
```
Each bundle executes ONE matching branch.

**4. Error Resilience with Exponential Backoff**
```
HTTP Module (critical API)
  ├── Success → continue
  └── Error Handler: Break
      └── Retry: count=5, interval=1 (doubles each retry)
          └── Max retries exceeded: Resume (use default/fallback data)
```
Handles transient failures (429 rate limits, 503 temporarily unavailable).

**5. Webhook Chaining for Multi-Scenario Workflows**
```
Scenario A (processes data)
  → HTTP Make Request to Scenario B's webhook URL (passes data in body)
  → Scenario B triggered immediately
  → B completes → (optional) Calls back to A via callback webhook
```
Sequential multi-scenario orchestration. Enable async pattern to avoid timeout.

**6. Caching with Data Stores**
```
Check Data Store for key
  ├── Found: Use cached value → continue
  └── Not found: API call → Save to Data Store → Use result
```
Prevents redundant expensive API calls. 10-100x faster than external API for lookups.

**7. Webhook Queue Management**
```
Incoming webhooks → Immediately save to Data Store
  → Scheduled scenario (every 5 min) processes Data Store records in batches
  → Clear processed records
```
Prevents queue overflow; enables batch optimization.

**8. AI Agent with Tool Integration**
```
Run AI Agent with goal: "Analyze lead and route to appropriate sales team"
  ├── Agent's tools: [Salesforce Lead lookup, Team availability API, CRM update]
  ├── Agent reasoning: "Lead is high-value + Team A available → route to A"
  → Router (based on agent output): Team assignment → Slack notify
```
Autonomous, reasoning-based task execution vs. fixed logic flows.

## API-First Automation: Make API Integration

### Make API Authentication

**API Key Authentication** (Simpler, for server-to-server):
```bash
curl -H "Authorization: YOUR_API_KEY" \
  https://eu1.make.com/api/v2/scenarios/112
```

**JWT Authentication** (For Make Bridge and custom integrations):
```javascript
const jwt = require('jsonwebtoken');
const crypto = require('crypto');

const SECRET_KEY = '04XXXXXXXXXXXXXXXXXXXX'; // from Make Account
const KEY_ID = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX';
const userId = 'user@company.com'; // unique user identifier

const token = jwt.sign(
  { sub: userId, jti: crypto.randomUUID() },
  SECRET_KEY,
  { expiresIn: '2m', keyid: KEY_ID }
);

// Use token in Authorization header: Bearer {token}
```

### Scenario Management API

**Activate Scenario**:
```bash
POST https://eu1.make.com/api/v2/scenarios/{scenarioId}/start
Authorization: YOUR_API_KEY
Response: { scenario: { id: 5, isActive: true, islinked: true } }
```

**Deactivate Scenario**:
```bash
POST https://eu1.make.com/api/v2/scenarios/{scenarioId}/stop
Authorization: YOUR_API_KEY
Response: { scenario: { id: 5, isActive: false } }
```

**Get Scenario Details** (includes blueprint, status, execution history):
```bash
GET https://eu1.make.com/api/v2/scenarios/{scenarioId}
Authorization: YOUR_API_KEY
Response: { scenario: { id: 112, name: "Sync Leads", blueprint: {...}, isActive: true } }
```

**Update Scenario Interface** (modify scenario inputs for programmatic calls):
```bash
PATCH https://eu1.make.com/api/v2/scenarios/{scenarioId}/interface
Authorization: YOUR_API_KEY
Content-Type: application/json

{
  "interface": {
    "input": [
      { "name": "email", "type": "text", "required": true },
      { "name": "priority", "type": "text", "default": "medium" }
    ]
  }
}
```

### Webhook API Management

**Get All Webhooks** (list registered webhooks):
```bash
GET https://eu1.make.com/api/v2/hooks
Authorization: YOUR_API_KEY
Response: { hooks: [ { id: 654, label: "New Lead", url: "https://..." } ] }
```

**Get Webhook Logs** (retrieve execution history; 3 days retention, 30 days Enterprise):
```bash
GET https://eu1.make.com/api/v2/hooks/{hookId}/logs?from=1234567890&to=1234567899
Authorization: YOUR_API_KEY
Response: {
  hookLogs: [
    { statusId: 1, parser: "gateway-webhook", loggedAt: "2025-01-15T10:30:00Z", data: {...} },
    { statusId: 3, parser: "gateway-webhook", loggedAt: "2025-01-15T10:25:00Z" }
  ]
}
```
`statusId: 1` = success, `statusId: 3` = failed. Use `data` field to inspect request/response.

**Get Specific Webhook Log**:
```bash
GET https://eu1.make.com/api/v2/hooks/{hookId}/logs/{logId}
Authorization: YOUR_API_KEY
Response: {
  hookLog: {
    statusId: 1,
    data: { request: { headers: {...}, body: {...} }, response: { status: 200, body: "..." } },
    loggedAt: "2025-01-15T10:30:00Z"
  }
}
```

### Incomplete Executions (DLQ) Recovery

**List Incomplete Executions** (scenarios that failed to complete):
```bash
GET https://eu1.make.com/api/v2/dlqs?scenarioId={scenarioId}
Authorization: YOUR_API_KEY
Response: {
  dlqs: [
    { id: "a07e16f2ad134bf49cf83a00aa95c0a5", reason: "Rate limit exceeded", timestamp: "2025-01-15T10:30:00Z" }
  ]
}
```

**Get Failed Scenario Blueprint** (retrieve exact state at failure):
```bash
GET https://eu1.make.com/api/v2/dlqs/{dlqId}/blueprint
Authorization: YOUR_API_KEY
Response: {
  blueprint: {
    flow: [ { id: 1, module: "http:ActionSendData", mapper: {...}, onerror: [...] } ],
    metadata: {...}
  }
}
```

Use this to understand failure context, replay with fixes, or alert operations.

## Make Bridge: Embedded Integrations

Make Bridge enables white-label automation by embedding Make into your applications. Users create integrations through your interface without accessing Make directly.

**Key Concepts**:
- **Portal**: User-facing interface embedded in your app for integration setup
- **API**: Manage integrations, users, configurations programmatically
- **JWT Authentication**: Each user gets unique JWT for secure authentication
- **Organizations**: Multi-tenant support; each org has isolated integrations

**Bridge API Example** (list user's integrations):
```javascript
async function getBridgeIntegrations(userId) {
  const token = generateMakeBridgeJwt(userId);
  const response = await fetch('https://eu2.make.com/portal/api/bridge/integrations', {
    method: 'GET',
    headers: { Authorization: `Bearer ${token}` }
  });
  return response.json();
}
```

**Use Cases**:
- SaaS product: Embed integration marketplace in your dashboard
- Enterprise app: Allow custom automation without coding
- No-code workflow builder: Layer Make automation without exposing Make UI

## Make Grid: Enterprise Visualization & Optimization

**Accessing Make Grid**: Organization section in top menu; provides 3D visualization of entire scenario ecosystem.

**What Grid Shows**:
- All scenarios (nodes) with status (active/inactive/failed)
- All webhooks (entry points) and their execution status
- All data stores (state repositories) and usage
- Interconnections: scenario→scenario calls, webhook→scenario triggers
- Real-time status indicators: red (failed), green (active), yellow (queued)

**Grid Features**:
- **Filters**: By team, status (active/inactive/failed), connected app, custom properties
- **Credit Overlay**: Visual representation of credit consumption per scenario (helps identify expensive paths)
- **Dependency Analysis**: Instantly see impact of disabling/modifying scenario (what downstream breaks?)
- **Search**: Find scenarios by name, tag, or connected app
- **Snapshots**: Save configuration snapshots for incident analysis and documentation

**Optimization Workflow**:
1. Enable credit overlay on Grid
2. Sort scenarios by cost
3. Identify expensive modules (AI Agents, batch transforms, nested iterators)
4. Apply optimization: batch processing, data store caching, filter early
5. Compare before/after credit consumption
6. Document savings in incident post-mortem

## Best Practices

**Scenario Architecture**:
- Name descriptively: e.g., "Salesforce_to_GoogleSheets_DailySync_Prod"
- Organize by business process AND environment (folder structure: Process → Environment → Scenario)
- One responsibility per scenario; break complex workflows into subscenarios
- Document integration requirements, API dependencies, and failure modes inline

**Performance & Credit Optimization**:
- Process 100+ item batches using Aggregator + bulk API calls, not one-by-one iterators
- Use Data Stores for lookup-heavy logic (replace external API calls for each lookup)
- Filter data early to prevent unnecessary module executions
- Profile scenarios with sample data before production activation
- Use Make Grid credit overlay to identify optimization opportunities
- Implement caching with short TTL (e.g., 1 hour) for slowly-changing reference data

**Error Handling Strategy**:
- Always attach error handlers to critical/external API modules
- Use `Ignore` only for truly optional operations
- Use `Resume` with sensible defaults for non-critical API failures
- Use `Break` for transient errors (rate limits, timeouts); configure exponential backoff
- Use `Commit` for batch scenarios to preserve partial progress on error
- Log errors to Data Stores or external services (Datadog, Splunk) for visibility

**Security Best Practices**:
- Use dedicated API connections per environment to prevent cross-environment data leaks
- Restrict webhook access: enable API key requirement, IP whitelist if caller IP is static
- Validate webhook payload structure and data types before processing
- Minimize data exposure: filter/redact PII before passing to non-secure systems
- Never hardcode credentials; use Connections exclusively
- Rotate API keys quarterly; monitor unused connections for removal
- Use TLS 1.2+ for all external API calls; reject self-signed certificates by default

**Monitoring & Observability**:
- Dashboard analytics: KPIs for success/fail rates, credit consumption, execution latency
- Export execution history regularly for long-term trend analysis
- Integrate external monitoring: Datadog, Splunk, or custom webhook to log critical events
- Build meta-scenarios: automated checks that ensure scenarios are running within SLA
- Set team credit budgets using Operations per Team (Enterprise feature)
- Alert on: incomplete executions, webhook queue backlog, connection auth failures, credit budget overages

**Testing & Validation**:
- Test with "Run once" before scheduling production scenarios
- Use Set Multiple Variables module to inject static test data for reproducible runs
- Verify all data mappings by inspecting module output; check for null/type mismatches
- Test edge cases: empty arrays, null values, special characters in strings
- Clone scenarios before major modifications; use versioning via git or scenario export

**Maintainability**:
- Use descriptive variable names: `{{customer_first_name}}` not `{{var1}}`
- Add comments explaining non-obvious logic (e.g., regex patterns, complex conditionals)
- Document integration contracts: expected data format, required fields, rate limits
- Maintain scenarios as code: export → git commit → code review → import to production
- Create reusable subscenarios for common operations (data validation, formatting, logging)

## Common Issues & Solutions

**Connection Failures (401/403)**:
- Root Cause: Token expiry, credential rotation, or scope insufficiency
- Solution: Re-authorize connection in Connections panel. Check if provider rotated credentials. Verify OAuth scopes grant required permissions. For enterprise SSO, ensure user has adequate role.

**Data Type Mismatches**:
- Root Cause: Module outputs array but downstream expects text; null values unchecked
- Solution: Use `ifempty()` for optional fields. Convert types: `toString()`, `toNumber()`, `toJSON()`. Use Text Parser for extracting typed data from unstructured input.

**Timeout Errors (54xx)**:
- Root Cause: External API slow, network latency, or request payload too large
- Solution: Increase module timeout in advanced settings (max 300s). For >300s operations, redesign with async pattern: initiate via API → receive callback webhook later. Check provider status page.

**Rate Limiting (429)**:
- Root Cause: Exceeded API rate limit (e.g., 100 req/min)
- Solution: Add Break error handler with exponential backoff (retry 3-5 times, 1-16s delays). Batch requests where possible. Schedule high-volume jobs during off-peak hours. Contact provider for rate limit increase. Consider Data Store caching to reduce API calls.

**Webhook Queue Backlog**:
- Root Cause: Receiving scenario slow; more webhooks arriving than processing speed
- Solution: Optimize receiving scenario (immediately save to Data Store, skip heavy processing). Process queued items via separate batch scenario. Scale webhook processing (Enterprise: dedicated webhook server).

**Make Grid Unavailable**:
- Root Cause: Grid is separate AWS service from Make platform; possible regional outage
- Solution: Check https://status.make.com/ for Grid service status. Use Grid filters to isolate failing scenarios. Take snapshots for documentation. Fall back to scenario execution logs if Grid unavailable.

**AI Agent Hallucination/Incorrect Output**:
- Root Cause: Agent's LLM generated plausible but incorrect output; insufficient tool constraints
- Solution: Implement validation after agent: Router → Check output against schema → On error, use fallback or escalate. Curate tools carefully (don't expose sensitive tools to low-confidence agents). Monitor agent reasoning trace for red flags.

## Real-World Enterprise Examples

**Example 1: Salesforce Lead Enrichment Pipeline**
- Trigger: Salesforce New Contact
- Router: If Contact from Target Account → Enrichment flow; else → Standard flow
- Enrichment: HTTP call third-party enrichment API
- Error handler: Resume with default fields if enrichment fails
- Update: Salesforce Update Contact with enriched data
- Log: Data Store record enrichment result for analytics
- Result: Auto-enriches 500 leads/day with fallback handling

**Example 2: Multi-Scenario Batch Report Generation**
- Scenario A (trigger): Scheduled daily 2 AM
- A: Google Sheets Get All Rows (10K customers)
- A: Iterator per customer
- A: Transform (Text Parser): Clean names, emails
- A: Aggregator: Collect all transformed customers
- A: HTTP call to Scenario B's webhook (passes customer array)
- Scenario B (triggered by A):
  - B: Iterator per customer
  - B: OpenAI Generate sales summary
  - B: Aggregator: Collect summaries
  - B: Google Docs Create document with all summaries
  - B: Email send report link
- Result: 10K customer summaries generated in 50 credits vs. 10K+ one-by-one

**Example 3: Real-Time Customer Support Routing with AI Agent**
- Trigger: Zendesk New Ticket
- Run AI Agent: "Analyze ticket sentiment, priority, and assign to appropriate team"
- Agent tools: [Zendesk ticket lookup, Team availability API, Customer history]
- Agent outputs: priority (high/medium/low), assigned_team
- Router: Route by priority
- High: Slack notify urgent + create Asana task
- Medium: Email team lead
- Low: Auto-response + queue for next business day
- Error handler: On agent failure, Resume with default (medium, general support team)

**Example 4: Data Warehouse Sync with Incomplete Execution Recovery**
- Scenario: Salesforce → Snowflake nightly sync (100K records)
- Batch process via Aggregator: 1000 records per batch API call
- Break error handler: Retry failed batches with exponential backoff
- Commit: Save successfully synced records before stopping
- Operations monitoring:
  - Scheduled: Check API `/dlqs` for incomplete executions
  - If DLQ has entries: Get failed blueprint via `/dlqs/{dlqId}/blueprint`
  - Analyze failure, fix (e.g., data type issue), re-run failed batch
  - Alert if >5% of batches failed (SLA breach)

**Example 5: Embedded Integration Platform (Make Bridge)**
- SaaS product user logs into your dashboard
- Your app calls Make Bridge API with user's JWT
- Bridge Portal opens, user creates integration: "Sync my Salesforce leads to Google Sheets"
- Your app monitors integration status via Bridge API
- On integration completion, notifies user and pulls sync status
- User never touches Make UI; all automation transparent

**Example 6: Make Grid Dependency Impact Analysis**
- Production incident: "Salesforce update failing"
- Open Make Grid; identify Salesforce module
- Grid shows: This scenario feeds to 3 downstream scenarios (Customer sync, Report generation, Analytics)
- Filter Grid to show credit consumption: Customer sync consuming 10x baseline
- Conclusion: Salesforce outage cascaded; prioritize Salesforce fix and notify affected teams
- Post-incident: Document dependency in Grid snapshot for playbook

## Advanced Topics

### Making Scenarios Programmatic with API

**Use Make API to Trigger Scenarios from External Systems**:
1. Create scenario with webhook trigger
2. External system makes HTTP POST to scenario's webhook URL (found in webhook module)
3. Pass data in JSON body
4. Scenario executes immediately

**Use Case**: CI/CD pipeline triggers Make scenario for deployment automation, data migration, or report generation.

### Bidirectional AI with MCP

**Make AI Agents as Tools for External LLMs** (e.g., Claude, ChatGPT):
- Make scenario exposed as "Run Make Workflow" tool
- External AI model can call Make scenario with natural language input
- Make executes scenario, returns result to external AI
- External AI uses result to inform next action

**External MCP Servers in Make AI Agents**:
- Make AI Agent equipped with connections to external MCP servers
- Agent can call external tools (e.g., web search, image generation, database query)
- Expands agent capabilities beyond native Make tools

### Performance at Enterprise Scale (10,000+ items)

1. **Batch Processing**: Iterator → Aggregator → Bulk API call (1 credit vs. 10,000+)
2. **Data Store Caching**: Cache reference data; 10-100x faster than API calls
3. **Filtering Early**: Remove invalid items before expensive transformations
4. **Parallel Routes**: Use routers with independent branches (can execute concurrently)
5. **Async Patterns**: Initiate long operation → Receive callback webhook later (vs. timeout)
6. **Credit Overlay on Make Grid**: Identify highest-cost scenarios; prioritize optimization

### Managing Multiple Environments (DEV/STAGING/PROD)

**Strategy**:
- Use dedicated Make Team or Organization per environment
- Create separate connections for each environment (prevents data contamination)
- Use naming convention: scenario name includes environment suffix (e.g., "Lead_Sync_PROD")
- Version control: Export scenarios → Git repo → Review → Import to target environment
- Use Set Variable module to inject environment-specific config (API base URL, feature flags)

### Make.com Blueprint JSON Structure & Scenario Building

This section provides the JSON schema and patterns for building, exporting, and reconstructing Make.com scenarios programmatically. Understanding JSON structure enables automation, version control, and scenario cloning.

### Core Scenario JSON Structure

Every Make scenario exports as JSON containing metadata, modules, connections, and flow logic:

```json
{
  "name": "Lead_Enrichment_Pipeline_PROD",
  "description": "Enriches Salesforce leads with third-party data, routes by score",
  "flow": [
    { "id": 1, "module": "webhooks:ActionCustomWebhook", "mapper": {}, "enabled": true },
    { "id": 2, "module": "http:ActionSendData", "mapper": { "url": "https://api.enrichment.com/enrich", "method": "POST" }, "onerror": [ { "type": "break", "count": 3, "interval": 1 } ] },
    { "id": 3, "module": "router:ActionRouter", "routes": [ { "condition": "{{2.score > 80}}", "path": [4, 5] }, { "condition": "{{2.score <= 80}}", "path": [6] } ] },
    { "id": 4, "module": "salesforce:ActionCreateRecord", "mapper": { "table": "Lead", "data": { "Score__c": "{{2.score}}", "Status": "Hot" } } },
    { "id": 5, "module": "slack:ActionSendMessage", "mapper": { "channel": "#sales", "text": "High-value lead: {{1.email}}" } },
    { "id": 6, "module": "dataStore:ActionAddRecord", "mapper": { "storeId": "lead_queue", "key": "{{1.id}}", "data": "{{1}}" } }
  ],
  "connections": [
    { "from": 1, "to": 2 },
    { "from": 2, "to": 3 },
    { "from": 3, "to": [4, 5, 6] }
  ],
  "metadata": {
    "version": "1.0.0",
    "team": "sales-automation",
    "tags": ["lead-enrichment", "production"],
    "createdAt": "2025-01-15T10:30:00Z",
    "lastModified": "2025-01-20T14:45:00Z"
  }
}
```

**Key Fields**: `flow` array with module objects (id, module name, mapper config), `onerror` handlers, `routes` for conditional branching, `connections` for data flow, `metadata` for versioning/documentation.

### Module JSON Patterns: HTTP, Iterator, Aggregator, Router, Filters, AI

**HTTP Request with Retries**:
```json
{ "id": 2, "module": "http:ActionSendData", "mapper": { "url": "https://api.example.com/enrich", "method": "POST", "body": { "email": "{{1.email}}" }, "timeout": 30 }, "onerror": [{ "type": "break", "count": 5, "interval": 1, "exponentialBackoff": true }, { "type": "resume", "fallback": { "score": 0 } }] }
```

**Iterator (Array Processing)**:
```json
{ "id": 3, "module": "arrayIterator:ActionArrayIterator", "mapper": { "array": "{{1.customers}}" } }
```
Repeats downstream modules per array item. Reference current: `{{3.firstName}}`

**Aggregator (Collect Results)**:
```json
{ "id": 5, "module": "arrayAggregator:ActionAggregator", "mapper": { "targetArray": "results" } }
```
Consolidates multiple cycles back into array. Place after iterator's dependent modules.

**Router (Conditional Branching)**:
```json
{ "id": 6, "module": "router:ActionRouter", "routes": [ { "label": "Premium", "condition": "{{2.tier}} == 'premium'", "path": [7, 8] }, { "label": "Standard", "condition": "{{2.tier}} == 'standard'", "path": [9] }, { "label": "Default", "condition": "", "path": [10] } ] }
```
Evaluated top-to-bottom; first TRUE executes. Empty condition = fallback (always matches).

**Filter (Gate Execution)**:
```json
{ "id": 7, "module": "filter:ActionFilter", "mapper": { "condition": "{{1.amount}} > 1000" } }
```
TRUE: continue. FALSE: halt for this bundle.

**AI Completion Module**:
```json
{ "id": 8, "module": "openai:ActionCompletion", "mapper": { "model": "gpt-4", "systemMessage": "You are a real estate analyst.", "userMessage": "Analyze: {{1.property}}. Return JSON.", "temperature": 0.7, "maxTokens": 1000, "responseFormat": "json" } }
```
Output: `{{8.response}}`. Use `responseFormat: "json"` for structured output.

**AI Agent Module (Autonomous Reasoning)**:
```json
{ "id": 9, "module": "makeAI:ActionAgent", "mapper": { "goal": "Route lead to appropriate team", "tools": [{ "name": "Get Lead", "type": "rest", "endpoint": "https://salesforce.api/leads/{{1.leadId}}" }], "maxIterations": 5, "temperature": 0.5 } }
```
Output: `{{9.reasoning}}`, `{{9.result}}` (agent's decision + thought process).

**Data Store (Cache/Lookup)**:
```json
{ "id": 10, "module": "dataStore:ActionAddRecord", "mapper": { "storeId": "lead_cache", "key": "lead_{{1.id}}", "data": { "email": "{{1.email}}", "score": "{{2.score}}" }, "ttl": 3600 } }
```
Retrieve: `{ "id": 11, "module": "dataStore:ActionSearchRecord", "mapper": { "storeId": "lead_cache", "key": "lead_{{1.id}}" } }`

**Set Variable (Reuse Values)**:
```json
{ "id": 12, "module": "util:ActionSetVariable", "mapper": { "name": "enriched_lead", "value": { "id": "{{1.id}}", "score": "{{2.score}}" } } }
```
Reference: `{{12.enriched_lead}}`

### Error Handler Patterns in JSON

**Break + Exponential Backoff**:
```json
"onerror": [{ "type": "break", "count": 5, "interval": 1, "exponentialBackoff": true }]
```
Retries: 1s, 2s, 4s, 8s, 16s. Use for transient errors (429, 503).

**Resume with Fallback** (Non-critical operations):
```json
"onerror": [{ "type": "resume", "fallback": { "status": "error", "data": null } }]
```
Downstream gets fallback; execution continues.

**Chained: Retry then Fallback**:
```json
"onerror": [{ "type": "break", "count": 3, "interval": 1 }, { "type": "resume", "fallback": { "status": "retry_failed" } }]
```

### Complete Example: Property Fix-and-Flip Analysis

Webhook (property data) → Market enrichment API → AI scoring → Router by score tier → Notifications + DB storage.

```json
{
  "name": "Property_DealAnalysis_FixAndFlip",
  "flow": [
    { "id": 1, "module": "webhooks:ActionCustomWebhook", "mapper": { "label": "New Property", "api_key": true }, "enabled": true },
    { "id": 2, "module": "http:ActionSendData", "mapper": { "url": "https://realestateapi.com/search", "method": "POST", "body": { "address": "{{1.address}}", "zipCode": "{{1.zipCode}}" } }, "onerror": [{ "type": "break", "count": 3 }, { "type": "resume", "fallback": { "marketData": null } }] },
    { "id": 3, "module": "openai:ActionCompletion", "mapper": { "model": "gpt-4", "systemMessage": "Real estate investment analyst. Return JSON: {score, arv, repairs, buyerProfile}", "userMessage": "Address: {{1.address}}\nPrice: ${{1.purchasePrice}}\nBeds: {{1.beds}}\nBaths: {{1.baths}}\nMarket: {{2.comps}}", "responseFormat": "json" } },
    { "id": 4, "module": "router:ActionRouter", "routes": [ { "label": "High (>75)", "condition": "{{3.score}} > 75", "path": [5, 6, 7] }, { "label": "Medium (50-75)", "condition": "{{3.score}} > 50", "path": [8, 9] }, { "label": "Low", "condition": "", "path": [10] } ] },
    { "id": 5, "module": "slack:ActionSendMessage", "mapper": { "channel": "#premium-deals", "text": "🔥 HIGH: {{1.address}} | Score: {{3.score}}/100 | ARV: ${{3.arv}}" } },
    { "id": 6, "module": "salesforce:ActionCreateRecord", "mapper": { "table": "Deal__c", "data": { "Address__c": "{{1.address}}", "Score__c": "{{3.score}}", "ARV__c": "{{3.arv}}", "Status__c": "Qualified" } } },
    { "id": 7, "module": "gmail:ActionSendEmail", "mapper": { "to": "buyers@company.com", "subject": "Deal: {{1.address}}", "body": "Score: {{3.score}}/100 | ARV: ${{3.arv}} | Repairs: ${{3.repairs}} | Profile: {{3.buyerProfile}}" } },
    { "id": 8, "module": "slack:ActionSendMessage", "mapper": { "channel": "#standard-deals", "text": "📋 STANDARD: {{1.address}} | Score: {{3.score}}" } },
    { "id": 9, "module": "dataStore:ActionAddRecord", "mapper": { "storeId": "deals_queue", "key": "deal_{{1.id}}", "data": { "address": "{{1.address}}", "score": "{{3.score}}", "tier": "standard" }, "ttl": 86400 } },
    { "id": 10, "module": "dataStore:ActionAddRecord", "mapper": { "storeId": "deals_archive", "key": "deal_{{1.id}}", "data": { "address": "{{1.address}}", "score": "{{3.score}}", "reason": "Below threshold" }, "ttl": 604800 } }
  ],
  "connections": [ { "from": 1, "to": 2 }, { "from": 2, "to": 3 }, { "from": 3, "to": 4 }, { "from": 4, "to": [5, 6, 7, 8, 9, 10] } ],
  "metadata": { "version": "2.0.0", "tags": ["real-estate", "fix-flip", "ai-scoring", "prod"], "environment": "PROD" }
}
```

### Export, Rebuild, & Programmatic Generation

**Export**: Make Dashboard → Scenario → Download a Copy (JSON includes flow, connections, config).

**Rebuild**: Import JSON blueprint via Make UI or Make API: `POST /api/v2/scenarios` with blueprint.

**Programmatic**:
```bash
curl -X POST https://eu1.make.com/api/v2/scenarios -H "Authorization: KEY" -d '{"name": "Deal_Analysis", "blueprint": {"flow": [...], "connections": [...]}}'
```

**Key Patterns for JSON**:
- Module IDs = sequential integers; used in data refs: `{{id.field}}`
- Connections = flow topology; multiple outputs possible (Router, Iterator)
- Error handlers = Break (retry), Resume (fallback), Rollback, Ignore
- Mapper = module-specific config + template expressions
- Routes = top-to-bottom evaluation; first TRUE executes
- TTL = Data Store cache expiration (seconds)

This structure enables version control (git), scenario cloning, and accurate recreation. When you ask me to build or recreate scenarios, provide JSON examples or describe architecture—I'll use these patterns.

## Incident Response & DLQ Handling

**On Production Alert** (scenario failed):
1. Check webhook logs via API: `GET /api/v2/hooks/{hookId}/logs`
2. If webhook queue > threshold, check incomplete executions: `GET /api/v2/dlqs?scenarioId=X`
3. Retrieve failed blueprint: `GET /api/v2/dlqs/{dlqId}/blueprint` (see exact failure state)
4. Analyze failure reason; implement fix in DEV
5. Test fix thoroughly
6. Deploy to PROD
7. Manually replay failed executions if needed (export data, re-process)

## Quick Reference

**Most-Used Formulas**:
- `{{now}}` - Current Unix timestamp
- `{{formatDate(date; "YYYY-MM-DD HH:mm:ss")}}` - Format date
- `{{ifempty(value; "default")}}` - Null coalesce
- `{{map(array; "fieldName")}}` - Extract field from array items
- `{{split(text; ",")}}` - String to array
- `{{join(array; ", ")}}` - Array to comma-separated string
- `{{length(array)}}` - Count items
- `{{add(1; 2; 3)}}` - Sum values
- `{{toJSON(object)}}` - Object to JSON string
- `{{parseDate(date_string; "YYYY-MM-DD"; "America/New_York")}}` - Parse with timezone

**Common HTTP Status Codes**:
- 200 OK, 201 Created
- 400 Bad Request (malformed), 401 Unauthorized (auth failed), 403 Forbidden (permissions), 404 Not Found
- 429 Too Many Requests (rate limited) - Handle with Break error handler
- 500 Internal Server Error, 503 Service Unavailable - Use Break with retry logic

**Make API Base URLs by Region**:
- EU1: `https://eu1.make.com/api/v2/`
- EU2: `https://eu2.make.com/api/v2/`
- US1: `https://us1.make.com/api/v2/`
- US2: `https://us2.make.com/api/v2/`
- AU1: `https://au1.make.com/api/v2/`

**Module Output Inspection**:
After scenario run, click "bubble" above connection → see exact data passed. Essential for debugging data type mismatches and mapping errors.

## Resources

- **Official Docs**: https://help.make.com/
- **Developer Hub**: https://developers.make.com/ (API, Bridge, custom apps, MCP)
- **API Reference**: https://developers.make.com/api-documentation/
- **Community Forums**: https://community.make.com/ (peer support, solutions)
- **Academy**: https://academy.make.com/ (certifications, courses)
- **Status Page**: https://status.make.com/ (incidents, maintenance)

For advanced challenges not covered in this skill, consult the official API documentation, community forums, or Make support. This skill prioritizes production-grade patterns; edge cases are handled via documented resources.

---

**Skill Version**: 2.2 | **Last Updated**: October 2025 (Blueprint JSON Structure Added) | **Context7 Sources**: Make API Documentation, Make Developer Hub, Make Custom Apps, Real Estate Automation Examples

