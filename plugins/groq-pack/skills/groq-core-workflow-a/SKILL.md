---
name: groq-core-workflow-a
description: |
  Execute Groq primary workflow: Core Workflow A.
  Use when implementing primary use case,
  building main features, or core integration tasks.
  Trigger with phrases like "groq main workflow",
  "primary task with groq".
allowed-tools: Read, Write, Edit, Bash(npm:*), Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Groq Core Workflow A

## Overview
Primary money-path workflow for Groq. This is the most common use case. Groq provides ultra-low-latency LLM inference using custom LPU (Language Processing Unit) hardware, enabling token generation speeds that are significantly faster than GPU-based providers. This makes Groq the right choice for latency-sensitive applications such as real-time chat interfaces, voice assistants, and streaming analysis pipelines where response time directly impacts user experience.

## Prerequisites
- Completed `groq-install-auth` setup
- Understanding of Groq core concepts
- Valid API credentials configured

## Instructions

### Step 1: Initialize
Authenticate with the Groq API and select the target model from the available options (LLaMA, Mixtral, Gemma, or others available on the platform). Configure your default request parameters including temperature, max tokens, and stop sequences. Verify the model is available in your region and that your rate limits accommodate your expected request volume.

```typescript
// Step 1 implementation
```

### Step 2: Execute
Submit the chat completion or text completion request to Groq. Because of the LPU architecture, first-token latency is exceptionally low, so the streaming experience feels near-instant for end users. Monitor the token-per-second rate in the response metadata to confirm the performance profile matches expectations for your use case.

```typescript
// Step 2 implementation
```

### Step 3: Finalize
Handle the streamed or buffered response appropriately for your application. For interactive use cases, render tokens as they arrive. For batch processing, accumulate the full response before writing results. Log model ID, token usage, and latency metrics for cost attribution and capacity planning.

```typescript
// Step 3 implementation
```

## Output
- Completed Core Workflow A execution
- Generated text or chat completion response from the selected Groq model
- Token usage statistics and measured latency
- Success confirmation or error details if the request failed

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
- [Groq Documentation](https://docs.groq.com)
- [Groq API Reference](https://docs.groq.com/api)

## Next Steps
For secondary workflow, see `groq-core-workflow-b`.