---
name: openrouter-model-routing
description: |
  Implement intelligent model routing strategies with OpenRouter. Use when optimizing cost/quality tradeoffs across models. Trigger with phrases like 'openrouter routing', 'model selection', 'route requests', 'model routing strategy'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Model Routing

## Overview

This skill teaches you how to build intelligent routing logic that selects the best model based on task complexity, cost constraints, or latency requirements.

## Prerequisites

- OpenRouter integration with multiple models tested
- Understanding of model capabilities and pricing differences

## Instructions

1. **Classify request complexity**: Analyze the incoming prompt to determine if it needs a simple, mid-tier, or advanced model (e.g., by token count, keyword patterns, or task type)
2. **Build a routing table**: Map task categories to model IDs — e.g., simple Q&A to `google/gemma-2-9b-it:free`, code generation to `anthropic/claude-3.5-sonnet`, reasoning to `openai/gpt-4-turbo`
3. **Implement the router function**: Create a function that takes a prompt and returns the appropriate model ID based on your classification logic
4. **Add cost guardrails**: Set per-request `max_tokens` and budget caps to prevent expensive models from exceeding cost limits
5. **Monitor and tune**: Log which model handles each request and track quality metrics to adjust routing thresholds over time

## Output

- A routing function that selects models based on task type and constraints
- Cost savings from using cheaper models for simple tasks
- Quality metrics per route to validate routing decisions

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| Wrong model selected | Classification logic too simple | Add more granular task categories; test with diverse prompts |
| Model unavailable | Selected model is temporarily down | Chain to fallback model (see openrouter-fallback-config) |
| Cost overrun | Complex tasks routed to expensive models | Set hard `max_tokens` limits and daily budget caps |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
