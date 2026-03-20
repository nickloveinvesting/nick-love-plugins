---
name: openrouter-openai-compat
description: |
  Leverage OpenRouter's OpenAI API compatibility layer. Use when migrating from OpenAI or maintaining dual compatibility. Trigger with phrases like 'openrouter openai compatible', 'openrouter drop-in', 'openrouter migration from openai', 'openai to openrouter'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Openai Compat

## Overview

This skill explains how to use existing OpenAI SDK code with OpenRouter by changing only the base URL and API key, enabling access to 100+ models with minimal code changes.

## Prerequisites

- Existing OpenAI SDK integration (Python or Node.js)
- OpenRouter API key

## Instructions

1. **Swap the base URL**: Change `base_url` from `https://api.openai.com/v1` to `https://openrouter.ai/api/v1` in your OpenAI client initialization
2. **Update the API key**: Replace your OpenAI key with your OpenRouter `sk-or-...` key
3. **Update model IDs**: Change model names to OpenRouter format (e.g., `gpt-4` becomes `openai/gpt-4` or use any other provider's model)
4. **Add OpenRouter-specific headers**: Optionally set `HTTP-Referer` and `X-Title` headers for better analytics tracking in the OpenRouter dashboard
5. **Test compatibility**: Run your existing test suite against OpenRouter; most endpoints work identically, but verify edge cases like streaming, tools, and embeddings

## Output

- Existing OpenAI code working through OpenRouter with no logic changes
- Access to non-OpenAI models (Anthropic, Google, etc.) through the same SDK
- Side-by-side comparison showing the minimal changes needed

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| 400 unsupported parameter | OpenRouter doesn't support a parameter your code sends | Remove or conditionally set parameters like `logprobs` or `response_format` based on the target model |
| Different embedding format | Embedding endpoints may behave differently | Use OpenRouter-specific embedding models or fall back to direct OpenAI for embeddings |
| Missing `organization` header | OpenRouter doesn't use org-level auth | Remove the `organization` parameter from client initialization |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
