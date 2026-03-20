---
name: replit-core-workflow-b
description: |
  Execute Replit secondary workflow: Core Workflow B.
  Use when implementing secondary use case,
  or complementing primary workflow.
  Trigger with phrases like "replit secondary workflow",
  "secondary task with replit".
allowed-tools: Read, Write, Edit, Bash(npm:*), Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Replit Core Workflow B

## Overview
Secondary workflow for Replit. Complements the Repl creation and execution workflow by focusing on collaboration management, deployment configuration, and bulk Repl administration. Use this skill when you need to manage team member access to Repls, configure custom domains for deployed projects, migrate Repls between teams, or audit and clean up stale Repls across an organization.

## Prerequisites
- Completed `replit-install-auth` setup
- Familiarity with `replit-core-workflow-a`
- Valid API credentials configured

## Instructions

### Step 1: Setup
Identify the administrative task to perform: collaboration management, deployment configuration, or bulk cleanup. For collaboration changes, compile the list of team members and the permission levels (viewer, editor, owner) they should hold on each Repl. For deployment configuration, gather the custom domain, environment variables, and always-on settings required for production hosting.

```typescript
// Step 1 implementation
```

### Step 2: Process
Apply the configuration changes via the Replit API. For permission updates, patch each Repl's collaboration settings with the new access list. For deployment configuration, update the Repl's hosting settings and verify the custom domain resolves correctly. For bulk cleanup, list all Repls matching your stale criteria and batch-delete or archive them to reclaim quota.

```typescript
// Step 2 implementation
```

### Step 3: Complete
Confirm that all changes took effect by querying the Repl metadata and verifying the updated state. Notify affected team members of permission changes. Document the administrative actions taken along with the rationale, particularly for deletions, so the audit trail is clear if questions arise later.

```typescript
// Step 3 implementation
```

## Output
- Completed Core Workflow B execution
- Updated Repl configurations, permissions, or deployment settings
- Cleanup report listing archived or deleted Repls
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
- [Replit Documentation](https://docs.replit.com)
- [Replit API Reference](https://docs.replit.com/api)

## Next Steps
For common errors, see `replit-common-errors`.