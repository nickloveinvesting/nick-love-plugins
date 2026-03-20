---
name: coderabbit-core-workflow-a
description: |
  Execute CodeRabbit primary workflow: Core Workflow A.
  Use when implementing primary use case,
  building main features, or core integration tasks.
  Trigger with phrases like "coderabbit main workflow",
  "primary task with coderabbit".
allowed-tools: Read, Write, Edit, Bash(npm:*), Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# CodeRabbit Core Workflow A

## Overview
Primary money-path workflow for CodeRabbit. This is the most common use case. CodeRabbit is an AI-powered code review platform that automatically reviews pull requests, identifies bugs, suggests improvements, and enforces coding standards. By integrating this skill into your workflow you gain consistent, automated feedback on every diff without waiting for human reviewers.

## Prerequisites
- Completed `coderabbit-install-auth` setup
- Understanding of CodeRabbit core concepts
- Valid API credentials configured

## Instructions

### Step 1: Initialize
Connect to the CodeRabbit API using your configured credentials and confirm the target repository is accessible. Verify that the webhook or CI integration is active so CodeRabbit can receive pull-request events automatically.

```typescript
// Step 1 implementation
```

### Step 2: Execute
Trigger the core review workflow by opening or updating a pull request. CodeRabbit will analyze the diff, apply your configured rule-sets, and post structured comments directly on the affected lines. Review the summary report to understand which categories of issues were found (security, performance, style, logic).

```typescript
// Step 2 implementation
```

### Step 3: Finalize
Act on the feedback: resolve addressed comments, re-request review after fixes, and merge once all blocking issues are cleared. Archive or dismiss suggestions that are intentional deviations so the signal-to-noise ratio stays high for future reviews.

```typescript
// Step 3 implementation
```

## Output
- Completed Core Workflow A execution
- Structured line-level review comments on the pull request
- Summary report categorizing issues by severity and type
- Success confirmation or error details if the review could not complete

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
- [CodeRabbit Documentation](https://docs.coderabbit.com)
- [CodeRabbit API Reference](https://docs.coderabbit.com/api)

## Next Steps
For secondary workflow, see `coderabbit-core-workflow-b`.