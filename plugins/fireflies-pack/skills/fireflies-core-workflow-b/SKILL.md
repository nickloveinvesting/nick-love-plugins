---
name: fireflies-core-workflow-b
description: |
  Execute Fireflies.ai secondary workflow: Core Workflow B.
  Use when implementing secondary use case,
  or complementing primary workflow.
  Trigger with phrases like "fireflies secondary workflow",
  "secondary task with fireflies".
allowed-tools: Read, Write, Edit, Bash(npm:*), Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Fireflies.ai Core Workflow B

## Overview
Secondary workflow for Fireflies.ai. Complements the transcript retrieval workflow by focusing on search, analytics, and bulk processing across your meeting history. Use this skill when you need to search across all past transcripts for a specific topic, generate trend reports on meeting frequency or action item completion, or bulk-export meeting data for compliance archiving.

## Prerequisites
- Completed `fireflies-install-auth` setup
- Familiarity with `fireflies-core-workflow-a`
- Valid API credentials configured

## Instructions

### Step 1: Setup
Configure the search parameters or analytics scope. For keyword search, specify the terms and optional date range to search across all stored transcripts. For analytics, define the metrics you want to aggregate such as average meeting duration, most discussed topics, or participant engagement levels. Ensure your API plan supports the volume of transcripts you need to process.

```typescript
// Step 1 implementation
```

### Step 2: Process
Execute the search or analytics query against the Fireflies API. For search, paginate through results to collect all matching transcript segments. For analytics, aggregate the returned metrics and identify patterns or anomalies worth reporting. Cross-reference action items with their source meetings to track resolution rates over time.

```typescript
// Step 2 implementation
```

### Step 3: Complete
Produce the final deliverable: a search result report, analytics dashboard data, or compliance export. For bulk exports, compress and archive the output according to your retention policy. Share actionable insights with stakeholders in a format that requires minimal context to understand.

```typescript
// Step 3 implementation
```

## Output
- Completed Core Workflow B execution
- Search results or analytics report derived from transcript history
- Bulk export or compliance archive if requested
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
- [Fireflies.ai Documentation](https://docs.fireflies.com)
- [Fireflies.ai API Reference](https://docs.fireflies.com/api)

## Next Steps
For common errors, see `fireflies-common-errors`.