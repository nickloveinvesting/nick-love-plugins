---
name: openrouter-sdk-patterns
description: |
  Implement common SDK usage patterns for OpenRouter. Use when building reusable client libraries or wrappers. Trigger with phrases like 'openrouter sdk', 'openrouter client library', 'openrouter wrapper', 'openrouter patterns'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter SDK Patterns

## Overview

This skill covers best practices for building OpenRouter client wrappers, including retry logic, error handling, response typing, and reusable patterns.

## Prerequisites

- OpenRouter integration
- OpenAI SDK (Python or TypeScript)

## Instructions

1. **Create a typed client wrapper**: Build a class that wraps the OpenAI SDK with OpenRouter-specific defaults (base URL, default headers, retry config)
2. **Add automatic retries**: Implement retry logic with exponential backoff for 429 and 5xx errors; the OpenAI SDK has built-in retry support via `max_retries`
3. **Type your responses**: Define TypeScript interfaces or Python dataclasses for your expected response shapes to catch errors at compile time
4. **Implement request/response middleware**: Add hooks for logging, cost tracking, and metrics collection that run on every request
5. **Build reusable prompt templates**: Create typed functions for common tasks (summarize, translate, classify) that encapsulate model selection and prompt engineering

## Output

- A reusable OpenRouter client class with built-in retry, logging, and typing
- Prompt template functions for common AI tasks
- Middleware pipeline for cross-cutting concerns (logging, cost tracking)

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| Type mismatch on response | Model returned unexpected format | Add runtime validation alongside static types; handle gracefully |
| Retry exhaustion | Max retries exceeded on persistent errors | Log the final error with full context; surface to caller with actionable message |
| Middleware error | Logging or metrics code threw an exception | Wrap middleware in try/catch so it never breaks the main request flow |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
