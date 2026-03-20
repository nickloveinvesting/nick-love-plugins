---
name: openrouter-multi-provider
description: |
  Use multiple AI providers through OpenRouter. Use when leveraging different providers for different capabilities. Trigger with phrases like 'openrouter providers', 'multi provider', 'openrouter openai anthropic', 'use multiple models'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Multi Provider

## Overview

This skill shows how to leverage OpenRouter's unified API to access models from OpenAI, Anthropic, Google, Meta, Mistral, and other providers through a single integration point.

## Prerequisites

- OpenRouter integration with sufficient credits
- Familiarity with models from at least two providers

## Instructions

1. **Understand the provider namespace**: OpenRouter model IDs use `provider/model-name` format (e.g., `openai/gpt-4-turbo`, `anthropic/claude-3.5-sonnet`, `google/gemini-pro`)
2. **Compare provider strengths**: Test the same prompt across providers to evaluate quality, speed, and cost; each provider excels at different task types
3. **Route by task type**: Use OpenAI models for code generation, Anthropic for analysis and safety, Google for multimodal, and open-source models for cost-sensitive tasks
4. **Handle provider-specific features**: Some features (like system prompts, tool calling, or JSON mode) work differently across providers; test each model's behavior
5. **Build a provider abstraction**: Create a thin wrapper that normalizes provider differences so your application code doesn't need to know which provider is serving the request

## Output

- A unified client that works with any provider through OpenRouter
- Provider comparison matrix for your specific use cases
- Task-to-provider routing logic that optimizes for quality and cost

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| Feature not supported | Provider doesn't support the requested feature (e.g., tools) | Check model capabilities via `/models` endpoint before sending |
| Different response formats | Providers return slightly different structures | Normalize responses through your abstraction layer |
| Provider outage | Single provider is down | Implement cross-provider fallback (e.g., OpenAI -> Anthropic -> Google) |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
