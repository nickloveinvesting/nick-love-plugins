---
name: openrouter-hello-world
description: |
  Create your first OpenRouter API request with a simple example. Use when learning OpenRouter or testing your setup. Trigger with phrases like 'openrouter hello world', 'openrouter first request', 'openrouter quickstart', 'test openrouter'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Hello World

## Overview

This skill provides a minimal working example to verify your OpenRouter integration is functioning and introduces the basic request/response pattern.

## Prerequisites

- OpenRouter API key configured
- Python 3.8+ or Node.js 18+
- OpenAI SDK installed

## Instructions

1. **Set your API key**: Export `OPENROUTER_API_KEY` as an environment variable or add it to your `.env` file
2. **Send a test completion**: Make a POST request to `https://openrouter.ai/api/v1/chat/completions` with a simple prompt using `model: "openai/gpt-3.5-turbo"`
3. **Verify the response**: Confirm the response contains `choices[0].message.content` and `usage` token counts
4. **Try a different model**: Swap the model to `anthropic/claude-3-haiku` or `google/gemma-2-9b-it:free` to confirm multi-model routing works

## Output

- A JSON response with `id`, `model`, `choices`, and `usage` fields
- Token usage breakdown (prompt_tokens, completion_tokens, total_tokens)
- Confirmation that your API key and network configuration are correct

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| 401 Unauthorized | Invalid or missing API key | Verify key starts with `sk-or-` and is exported correctly |
| 404 Not Found | Wrong base URL | Use `https://openrouter.ai/api/v1` (not v2) |
| 400 Bad Request | Malformed JSON body | Check `messages` array has `role` and `content` fields |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
