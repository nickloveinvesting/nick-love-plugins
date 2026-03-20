---
name: firecrawl-core-workflow-b
description: |
  Execute FireCrawl secondary workflow: Core Workflow B.
  Use when implementing secondary use case,
  or complementing primary workflow.
  Trigger with phrases like "firecrawl secondary workflow",
  "secondary task with firecrawl".
allowed-tools: Read, Write, Edit, Bash(npm:*), Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# FireCrawl Core Workflow B

## Overview
Secondary workflow for FireCrawl. Complements the primary scraping workflow by focusing on structured data extraction and scheduled monitoring use cases. Use this skill when you need to extract specific fields from pages using a defined schema, set up recurring crawls for change detection, or convert an entire documentation site into a searchable knowledge base on a regular cadence.

## Prerequisites
- Completed `firecrawl-install-auth` setup
- Familiarity with `firecrawl-core-workflow-a`
- Valid API credentials configured

## Instructions

### Step 1: Setup
Define the JSON schema describing the fields you want to extract from each page. FireCrawl's structured extraction mode uses this schema to return typed data rather than raw Markdown, which is more reliable for downstream database ingestion. Specify the target URLs or URL patterns and configure the recurrence schedule if monitoring for content changes.

```typescript
// Step 1 implementation
```

### Step 2: Process
Execute the structured extraction job and receive typed JSON responses for each scraped page. Validate the extracted fields against your schema to catch pages where the expected content was absent or malformed. For monitoring jobs, compare the current extraction against the previous snapshot to identify what changed.

```typescript
// Step 2 implementation
```

### Step 3: Complete
Persist the structured results to your database or data pipeline. For change detection scenarios, trigger notifications or downstream workflows when meaningful diffs are detected. Archive historical snapshots for audit purposes and rotate older snapshots according to your retention policy.

```typescript
// Step 3 implementation
```

## Output
- Completed Core Workflow B execution
- Typed JSON records extracted according to your defined schema
- Change diff report for monitoring scenarios
- Success confirmation or error details

## Error Handling
| Aspect | Workflow A | Workflow B |
|--------|------------|------------|
| Use Case | Primary | Secondary |
| Complexity | Medium | Lower |
| Performance | Standard | Optimized |

## Examples

### Complete Workflow
```typescript
// Complete workflow example
```

### Error Recovery
```typescript
// Error handling code
```

## Resources
- [FireCrawl Documentation](https://docs.firecrawl.com)
- [FireCrawl API Reference](https://docs.firecrawl.com/api)

## Next Steps
For common errors, see `firecrawl-common-errors`.