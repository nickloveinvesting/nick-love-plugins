---
name: groq-core-workflow-b
description: |
  Execute Groq secondary workflow: Core Workflow B.
  Use when implementing secondary use case,
  or complementing primary workflow.
  Trigger with phrases like "groq secondary workflow",
  "secondary task with groq".
allowed-tools: Read, Write, Edit, Bash(npm:*), Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Groq Core Workflow B

## Overview
Secondary workflow for Groq. Complements the primary inference workflow by focusing on batch processing, model benchmarking, and advanced prompt optimization. Use this skill when you need to evaluate multiple Groq models against the same prompt set, run A/B tests on different prompting strategies, or process large volumes of inference requests within API quota constraints.

## Prerequisites
- Completed `groq-install-auth` setup
- Familiarity with `groq-core-workflow-a`
- Valid API credentials configured

## Instructions

### Step 1: Setup
Define your prompt dataset and the set of model variants or parameter configurations you want to test. Structure the evaluation criteria: what constitutes a good response for your use case — accuracy, conciseness, format compliance, or latency. Implement a scoring function or evaluation rubric you can apply consistently across all model outputs.

```typescript
// Step 1 implementation
```

### Step 2: Process
Submit the prompt batch to each model configuration in turn, respecting rate limits between requests. Collect all responses along with latency and token count metadata. Apply your scoring function to each response and record the results. For high-volume batches, parallelize requests up to your rate limit and implement exponential backoff for any throttled calls.

```typescript
// Step 2 implementation
```

### Step 3: Complete
Aggregate the evaluation scores and produce a comparison report showing which model or configuration performed best across your prompt set. Commit the winning configuration to your application settings. Archive the full evaluation dataset including prompts, responses, and scores for future regression testing.

```typescript
// Step 3 implementation
```

## Output
- Completed Core Workflow B execution
- Model comparison report with scores and latency metrics per configuration
- Recommended optimal model and parameter settings for your use case
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
- [Groq Documentation](https://docs.groq.com)
- [Groq API Reference](https://docs.groq.com/api)

## Next Steps
For common errors, see `groq-common-errors`.