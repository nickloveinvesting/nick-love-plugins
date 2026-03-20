---
name: firecrawl-core-workflow-a
description: |
  Execute FireCrawl primary workflow: Core Workflow A.
  Use when implementing primary use case,
  building main features, or core integration tasks.
  Trigger with phrases like "firecrawl main workflow",
  "primary task with firecrawl".
allowed-tools: Read, Write, Edit, Bash(npm:*), Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# FireCrawl Core Workflow A

## Overview
Primary money-path workflow for FireCrawl. This is the most common use case. FireCrawl is a web scraping and crawling API that converts any website into clean, LLM-ready Markdown or structured data. It handles JavaScript rendering, login-gated pages, and pagination automatically, which removes the need for custom browser automation scripts when you need to extract content from modern web applications.

## Prerequisites
- Completed `firecrawl-install-auth` setup
- Understanding of FireCrawl core concepts
- Valid API credentials configured

## Instructions

### Step 1: Initialize
Connect to the FireCrawl API with your API key and specify the target URL you want to scrape. Choose between single-page scrape mode for individual URLs and full-crawl mode for entire sites. Configure output format preferences (Markdown, HTML, or structured JSON) and set any include or exclude URL path patterns to focus the crawl scope.

```typescript
// Step 1 implementation
```

### Step 2: Execute
Submit the scrape or crawl job and monitor its progress via the job status endpoint. FireCrawl queues the work asynchronously for multi-page crawls. Poll for completion or set up a webhook callback. Once complete, retrieve the extracted content and validate that it covers the pages you intended, checking for any blocked or failed URLs.

```typescript
// Step 2 implementation
```

### Step 3: Finalize
Post-process the extracted Markdown or JSON: strip navigation boilerplate if present, split long documents into chunks suitable for embedding, and store the results in your vector database or knowledge base. Record the crawl metadata (URLs visited, extraction timestamp, token count) for provenance tracking.

```typescript
// Step 3 implementation
```

## Output
- Completed Core Workflow A execution
- Clean Markdown or structured JSON extracted from the target URL(s)
- Crawl summary listing pages visited and any failures
- Success confirmation or error details

## Error Handling
| Error | Cause | Solution |
|-------|-------|----------|
| Error 1 | Cause | Solution |
| Error 2 | Cause | Solution |

## Examples

### Complete Workflow
```typescript
// Complete workflow example
```

### Common Variations
- Variation 1: Description
- Variation 2: Description

## Resources
- [FireCrawl Documentation](https://docs.firecrawl.com)
- [FireCrawl API Reference](https://docs.firecrawl.com/api)

## Next Steps
For secondary workflow, see `firecrawl-core-workflow-b`.