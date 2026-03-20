---
name: retellai-core-workflow-b
description: |
  Execute Retell AI secondary workflow: Core Workflow B.
  Use when implementing secondary use case,
  or complementing primary workflow.
  Trigger with phrases like "retellai secondary workflow",
  "secondary task with retellai".
allowed-tools: Read, Write, Edit, Bash(npm:*), Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Retell AI Core Workflow B

## Overview
Secondary workflow for Retell AI. Complements the call execution workflow by focusing on agent optimization, batch call management, and analytics. Use this skill when you need to refine a voice agent's script based on call transcript analysis, run A/B tests between two conversation flows, manage a large batch of outbound calls with scheduling and concurrency controls, or generate performance reports across a campaign.

## Prerequisites
- Completed `retellai-install-auth` setup
- Familiarity with `retellai-core-workflow-a`
- Valid API credentials configured

## Instructions

### Step 1: Setup
Define the optimization or batch management task. For script refinement, collect a representative sample of call transcripts and identify the moments where conversations deviated from the intended flow or where the agent's responses were inaccurate. For batch calling, prepare the list of target contacts with any dynamic variables needed per call and configure the concurrency limit and scheduling window.

```typescript
// Step 1 implementation
```

### Step 2: Process
Apply the changes: update the agent script or LLM prompt with the identified improvements and test against a small subset of calls before rolling out broadly. For batch execution, submit the call batch via the Retell AI API and monitor the real-time progress dashboard for connection failures, dropped calls, or unusually short conversations that may indicate issues. Adjust concurrency if call quality metrics degrade under high load.

```typescript
// Step 2 implementation
```

### Step 3: Complete
After the batch or optimization cycle completes, generate a performance report summarizing call outcomes, conversation completion rates, and goal conversion metrics. Compare the improved script's performance against the previous baseline to quantify the impact of the changes. Archive the transcripts and recordings for compliance and share the performance summary with stakeholders.

```typescript
// Step 3 implementation
```

## Output
- Completed Core Workflow B execution
- Optimized agent script with validated improvements
- Batch call campaign report with outcome metrics
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
- [Retell AI Documentation](https://docs.retellai.com)
- [Retell AI API Reference](https://docs.retellai.com/api)

## Next Steps
For common errors, see `retellai-common-errors`.