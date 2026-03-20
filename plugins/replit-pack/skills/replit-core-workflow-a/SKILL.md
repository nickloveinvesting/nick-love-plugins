---
name: replit-core-workflow-a
description: |
  Execute Replit primary workflow: Core Workflow A.
  Use when implementing primary use case,
  building main features, or core integration tasks.
  Trigger with phrases like "replit main workflow",
  "primary task with replit".
allowed-tools: Read, Write, Edit, Bash(npm:*), Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Replit Core Workflow A

## Overview
Primary money-path workflow for Replit. This is the most common use case. Replit is a browser-based development environment and deployment platform that lets you create, run, and host applications without any local setup. Its API enables programmatic management of Repls, making it useful for automated onboarding flows, educational platforms that provision development environments per student, and tools that need to spin up isolated code execution environments on demand.

## Prerequisites
- Completed `replit-install-auth` setup
- Understanding of Replit core concepts
- Valid API credentials configured

## Instructions

### Step 1: Initialize
Authenticate with the Replit API using your personal or team API token. Select the template or language runtime for the Repl you want to create or interact with. Verify that your account has sufficient compute quota for the expected number of concurrent Repls, particularly if you are building a multi-tenant system that provisions one environment per user.

```typescript
// Step 1 implementation
```

### Step 2: Execute
Create the Repl via the API with your specified configuration, or connect to an existing Repl by its slug. Execute code or run commands within the Repl environment using the API. Monitor the output stream for results, errors, or interactive prompts. For educational or demo use cases, share the Repl URL with users so they can view and interact with the running environment.

```typescript
// Step 2 implementation
```

### Step 3: Finalize
Capture the execution output and handle any errors returned from the runtime. If the Repl is ephemeral, clean up by deleting it after the session ends to avoid accumulating idle Repls against your quota. For persistent Repls, save the final state and ensure it is set to the correct visibility (public or private).

```typescript
// Step 3 implementation
```

## Output
- Completed Core Workflow A execution
- Repl created or accessed with confirmed runtime status
- Execution output or hosted application URL
- Success confirmation or error details if the operation failed

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
- [Replit Documentation](https://docs.replit.com)
- [Replit API Reference](https://docs.replit.com/api)

## Next Steps
For secondary workflow, see `replit-core-workflow-b`.