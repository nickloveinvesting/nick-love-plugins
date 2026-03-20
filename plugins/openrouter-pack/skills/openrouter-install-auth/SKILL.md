---
name: openrouter-install-auth
description: |
  Execute set up OpenRouter API authentication and configure API keys. Use when starting a new OpenRouter integration or troubleshooting auth issues. Trigger with phrases like 'openrouter setup', 'openrouter api key', 'openrouter authentication', 'configure openrouter'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Install Auth

## Overview

This skill guides you through obtaining and configuring OpenRouter API credentials, setting up environment variables, and verifying your authentication is working correctly.

## Prerequisites

- OpenRouter account (free at openrouter.ai)
- Python 3.8+ or Node.js 18+
- OpenAI SDK installed (`pip install openai` or `npm install openai`)

## Instructions

1. **Create an OpenRouter account**: Sign up at [openrouter.ai](https://openrouter.ai) and navigate to the API Keys page
2. **Generate an API key**: Click "Create Key", give it a descriptive name, and copy the `sk-or-...` value immediately (it won't be shown again)
3. **Configure your environment**: Add `OPENROUTER_API_KEY=sk-or-...` to your `.env` file or export it in your shell profile
4. **Initialize the OpenAI SDK**: Point the SDK at `base_url="https://openrouter.ai/api/v1"` with your key
5. **Verify authentication**: Run a minimal chat completion request and confirm you get a 200 response with valid output

## Output

- A working OpenAI SDK client configured for OpenRouter
- Environment variable set and loadable from `.env`
- Successful test request confirming authentication works

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| 401 `invalid_api_key` | Key is malformed or revoked | Regenerate at openrouter.ai/keys |
| 401 `missing_api_key` | Authorization header missing | Add `Authorization: Bearer sk-or-...` header |
| 403 `insufficient_credits` | Account has no credits | Add credits at openrouter.ai/credits or use a free model |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
