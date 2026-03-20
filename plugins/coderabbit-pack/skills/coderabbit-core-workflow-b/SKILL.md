---
name: coderabbit-core-workflow-b
description: |
  Execute CodeRabbit secondary workflow: Core Workflow B.
  Use when implementing secondary use case,
  or complementing primary workflow.
  Trigger with phrases like "coderabbit secondary workflow",
  "secondary task with coderabbit".
allowed-tools: Read, Write, Edit, Bash(npm:*), Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# CodeRabbit Core Workflow B

## Overview
Secondary workflow for CodeRabbit. Complements the primary workflow by addressing configuration tuning, rule customization, and bulk remediation tasks that arise after the initial integration is established. Use this skill when you need to adjust review sensitivity, suppress false positives, or apply CodeRabbit feedback across multiple pull requests at once.

## Prerequisites
- Completed `coderabbit-install-auth` setup
- Familiarity with `coderabbit-core-workflow-a`
- Valid API credentials configured

## Instructions

### Step 1: Setup
Load the current CodeRabbit configuration and review the existing rule-set. Identify which rules are generating excessive noise or missing important patterns based on recent review history.

```typescript
// Step 1 implementation
```

### Step 2: Process
Update the configuration with refined rule weights, additional ignore patterns, or new custom rules. Apply the changes to the repository settings and validate by re-running CodeRabbit against a representative pull request to confirm the new behavior matches expectations.

```typescript
// Step 2 implementation
```

### Step 3: Complete
Commit the updated configuration file, document the rationale for each change in your team's runbook, and notify reviewers of the updated standards. Monitor the next several reviews to ensure the tuned configuration reduces noise without missing real issues.

```typescript
// Step 3 implementation
```

## Output
- Completed Core Workflow B execution
- Updated CodeRabbit configuration committed to repository
- Validation report confirming rule changes behave as intended
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
- [CodeRabbit Documentation](https://docs.coderabbit.com)
- [CodeRabbit API Reference](https://docs.coderabbit.com/api)

## Next Steps
For common errors, see `coderabbit-common-errors`.