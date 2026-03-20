---
name: openrouter-model-catalog
description: |
  Build explore and query the OpenRouter model catalog programmatically. Use when selecting models or checking availability. Trigger with phrases like 'openrouter models', 'list openrouter models', 'openrouter model catalog', 'available models openrouter'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Model Catalog

## Overview

This skill teaches you how to query the OpenRouter models API, filter by capabilities, and select the right model for your use case.

## Prerequisites

- OpenRouter API key configured
- Basic understanding of LLM model differences

## Instructions

1. **Fetch the model list**: GET `https://openrouter.ai/api/v1/models` to retrieve all available models with pricing, context length, and capability metadata
2. **Filter by criteria**: Parse the response to filter models by `context_length`, `pricing.prompt`, `pricing.completion`, or provider prefix (e.g., `anthropic/`, `openai/`)
3. **Check model capabilities**: Look at the `supported_parameters` field to verify features like function calling, streaming, or JSON mode
4. **Compare pricing**: Sort models by cost per million tokens to find the best value for your workload
5. **Cache results**: Store the catalog locally with a TTL of 1 hour since model availability changes infrequently

## Output

- Full model catalog JSON with IDs, pricing, and context lengths
- Filtered model lists by capability (e.g., function-calling models, free models)
- Cost comparison table for your shortlisted models

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| Empty model list | API returned no models | Check API key permissions; free keys may have limited access |
| Stale pricing data | Using cached data too long | Set cache TTL to 1 hour and refetch periodically |
| Model ID not found | Model was removed or renamed | Re-query the catalog; model IDs change when providers update versions |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
