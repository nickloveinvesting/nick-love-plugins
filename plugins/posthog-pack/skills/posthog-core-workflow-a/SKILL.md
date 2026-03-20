---
name: posthog-core-workflow-a
description: |
  Execute PostHog primary workflow: Core Workflow A.
  Use when implementing primary use case,
  building main features, or core integration tasks.
  Trigger with phrases like "posthog main workflow",
  "primary task with posthog".
allowed-tools: Read, Write, Edit, Bash(npm:*), Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# PostHog Core Workflow A

## Overview
Primary money-path workflow for PostHog. This is the most common use case. PostHog is an open-source product analytics platform that captures user events, tracks feature flag states, records sessions, and runs A/B experiments. Unlike third-party analytics services, PostHog can be self-hosted so that event data never leaves your infrastructure, which is critical for companies with strict data residency or privacy requirements.

## Prerequisites
- Completed `posthog-install-auth` setup
- Understanding of PostHog core concepts
- Valid API credentials configured

## Instructions

### Step 1: Initialize
Authenticate with the PostHog API using your project API key. Verify that the PostHog SDK is correctly initialized in your application and that events are flowing to your project. Confirm that distinct user IDs are consistent across anonymous and identified sessions to avoid identity fragmentation in your funnel analysis.

```typescript
// Step 1 implementation
```

### Step 2: Execute
Capture the target events using `posthog.capture()` calls with the appropriate event name and property payload. Ensure that each event includes the properties needed for downstream analysis — for example, subscription tier, page name, or experiment variant. Use the PostHog API to query event counts, create funnels, or fetch session recordings programmatically when you need to embed analytics data in external dashboards.

```typescript
// Step 2 implementation
```

### Step 3: Finalize
Review the captured events in the PostHog dashboard to verify that property names are consistent and that volumes match expectations. Set up any required alerts or annotations to mark significant product changes that could affect metric trends. Export the data or query results to your reporting pipeline if needed.

```typescript
// Step 3 implementation
```

## Output
- Completed Core Workflow A execution
- Events successfully captured and queryable in PostHog
- Verified event schema with consistent property names
- Success confirmation or error details if event ingestion failed

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
- [PostHog Documentation](https://docs.posthog.com)
- [PostHog API Reference](https://docs.posthog.com/api)

## Next Steps
For secondary workflow, see `posthog-core-workflow-b`.