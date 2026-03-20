---
name: openrouter-common-errors
description: |
  Diagnose and fix common OpenRouter API errors. Use when encountering error codes or unexpected failures. Trigger with phrases like 'openrouter error', 'openrouter 401', 'openrouter 429', 'fix openrouter'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Common Errors

## Overview

This skill provides a comprehensive reference for diagnosing and resolving the most frequently encountered OpenRouter API errors.

## Prerequisites

- OpenRouter integration
- Basic HTTP status code knowledge

## Instructions

1. **Identify the error code**: Check the HTTP status code and the `error.code` field in the response body for the specific error type
2. **Look up the error**: Match the error against the common patterns below — 401 (auth), 402 (credits), 429 (rate limit), 400 (bad request), 5xx (server)
3. **Apply the fix**: Follow the resolution steps for the specific error; most common errors are configuration issues that can be fixed without code changes
4. **Add error handling**: Wrap API calls in try/catch blocks that handle each error category differently (retry for 429/5xx, fail fast for 401/400)
5. **Prevent recurrence**: Add validation middleware that catches common mistakes (missing API key, invalid model ID, malformed messages) before making the API call

## Output

- Error diagnosis with root cause identified
- Resolution steps specific to the error encountered
- Preventive validation middleware that catches common mistakes before API calls

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| 401 Unauthorized | Invalid, expired, or missing API key | Verify key starts with `sk-or-`; check it's not revoked at openrouter.ai/keys |
| 402 Payment Required | No credits remaining | Add credits at openrouter.ai/credits; or use a free model like `google/gemma-2-9b-it:free` |
| 429 Too Many Requests | Rate limit exceeded | Implement exponential backoff; respect `Retry-After` header; reduce request rate |
| 400 Bad Request | Malformed request body | Validate `messages` array format; check `model` ID includes provider prefix |
| 408 Request Timeout | Model took too long to respond | Retry with a faster model; reduce `max_tokens`; use streaming |
| 502/503 Server Error | Upstream provider outage | Retry with backoff; check status.openrouter.ai; use fallback models |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
