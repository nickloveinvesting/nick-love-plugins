---
name: openrouter-known-pitfalls
description: |
  Avoid common OpenRouter integration pitfalls and gotchas. Use proactively when designing or reviewing an integration. Trigger with phrases like 'openrouter pitfalls', 'openrouter gotchas', 'openrouter mistakes', 'openrouter best practices'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Known Pitfalls

## Overview

This skill documents the most common mistakes developers make when integrating OpenRouter and how to avoid them.

## Prerequisites

- OpenRouter integration (planned or existing)

## Instructions

1. **Avoid hardcoding model IDs**: Models get renamed or removed; always validate model availability at startup and handle missing models gracefully
2. **Don't ignore token limits**: Each model has different context windows; always check `context_length` from the models API and validate prompt size before sending
3. **Handle provider differences**: The same prompt can produce different results across providers; test critical prompts with your specific model, not just any model
4. **Set max_tokens explicitly**: Without `max_tokens`, models may generate very long (and expensive) responses; always set a reasonable limit
5. **Don't store API keys in code**: Use environment variables or a secrets manager; add `.env` to `.gitignore`; rotate keys if they're ever exposed

## Output

- Checklist of common pitfalls with prevention strategies
- Code review checklist for OpenRouter integrations
- Configuration validation script that catches common mistakes

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| `model_not_found` after working fine | Model was renamed or deprecated | Query `/models` at startup; maintain a fallback model list |
| Unexpectedly large bill | No `max_tokens` set on expensive model | Always set `max_tokens`; implement cost tracking middleware |
| Different behavior across models | Assuming all models handle prompts identically | Test with each model you plan to use; adjust prompts per model if needed |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
