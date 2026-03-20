---
name: perplexity-core-workflow-b
description: |
  Execute Perplexity secondary workflow: Core Workflow B.
  Use when implementing secondary use case,
  or complementing primary workflow.
  Trigger with phrases like "perplexity secondary workflow",
  "secondary task with perplexity".
allowed-tools: Read, Write, Edit, Bash(npm:*), Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Perplexity Core Workflow B

## Overview
Secondary workflow for Perplexity. Complements the single-query answer workflow by enabling multi-turn research sessions, batch query processing, and structured report generation. Use this skill when you need to conduct an in-depth investigation across multiple related questions, generate a comprehensive research brief from a series of queries, or monitor a topic over time by running scheduled queries and comparing responses.

## Prerequisites
- Completed `perplexity-install-auth` setup
- Familiarity with `perplexity-core-workflow-a`
- Valid API credentials configured

## Instructions

### Step 1: Setup
Define the research topic and decompose it into a structured list of questions that progressively build from broad context to specific details. For multi-turn sessions, design the conversation history so each follow-up query references insights from the previous answers, enabling the model to synthesize a coherent research thread across multiple exchanges.

```typescript
// Step 1 implementation
```

### Step 2: Process
Execute the query sequence in order, passing the conversation history to each subsequent request so Perplexity maintains context. For batch report generation, collect all question-answer pairs with their citations. Review each answer for consistency and flag any contradictions between responses that need further clarification with a follow-up query.

```typescript
// Step 2 implementation
```

### Step 3: Complete
Synthesize the collected answers into a structured research document, organizing sections according to your outline. Include all cited sources in a consolidated bibliography. For monitoring scenarios, compare the current run's answers against previous snapshots to highlight what has changed on the topic since the last research cycle.

```typescript
// Step 3 implementation
```

## Output
- Completed Core Workflow B execution
- Structured multi-section research document synthesized from the query sequence
- Consolidated bibliography of all cited sources
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
- [Perplexity Documentation](https://docs.perplexity.com)
- [Perplexity API Reference](https://docs.perplexity.com/api)

## Next Steps
For common errors, see `perplexity-common-errors`.