---
name: retellai-core-workflow-a
description: |
  Execute Retell AI primary workflow: Core Workflow A.
  Use when implementing primary use case,
  building main features, or core integration tasks.
  Trigger with phrases like "retellai main workflow",
  "primary task with retellai".
allowed-tools: Read, Write, Edit, Bash(npm:*), Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Retell AI Core Workflow A

## Overview
Primary money-path workflow for Retell AI. This is the most common use case. Retell AI is a platform for building conversational voice agents powered by large language models. It handles the telephony integration, real-time speech-to-text, LLM orchestration, and text-to-speech pipeline so that you can focus on defining the agent's conversation logic. It is commonly used for automated customer service calls, appointment booking, outbound sales dialing, and interactive voice response systems.

## Prerequisites
- Completed `retellai-install-auth` setup
- Understanding of Retell AI core concepts
- Valid API credentials configured

## Instructions

### Step 1: Initialize
Authenticate with the Retell AI API and verify that your agent is configured with the correct LLM model, voice profile, and conversation script. Confirm that your phone number is registered and associated with the agent. Review the agent's interrupt sensitivity and response latency settings to ensure they produce a natural conversation pace for your target use case.

```typescript
// Step 1 implementation
```

### Step 2: Execute
Initiate a call using the Retell AI API by providing the target phone number and any dynamic variables that should be injected into the conversation script for this specific call (e.g., the customer's name or appointment time). Monitor the call status and transcription stream in real time. Review the call recording and transcript after the call completes to assess conversation quality and identify script improvements.

```typescript
// Step 2 implementation
```

### Step 3: Finalize
Extract the call outcome and any data collected during the conversation from the Retell AI call record. Update your CRM or scheduling system with the result. For high-volume outbound campaigns, aggregate call outcomes across the batch to measure connection rate, completion rate, and goal achievement rate.

```typescript
// Step 3 implementation
```

## Output
- Completed Core Workflow A execution
- Voice call completed with full transcript and recording available
- Call outcome and collected data exported for downstream use
- Success confirmation or error details if the call could not be connected

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
- [Retell AI Documentation](https://docs.retellai.com)
- [Retell AI API Reference](https://docs.retellai.com/api)

## Next Steps
For secondary workflow, see `retellai-core-workflow-b`.