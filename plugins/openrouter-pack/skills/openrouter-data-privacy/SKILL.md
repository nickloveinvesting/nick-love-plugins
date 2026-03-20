---
name: openrouter-data-privacy
description: |
  Implement data privacy controls for OpenRouter API usage. Use when handling sensitive data or meeting privacy regulations. Trigger with phrases like 'openrouter privacy', 'openrouter data handling', 'openrouter pii', 'openrouter gdpr'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Data Privacy

## Overview

This skill covers techniques for protecting sensitive data when using the OpenRouter API, including PII filtering, data minimization, and privacy-preserving prompt design.

## Prerequisites

- OpenRouter integration
- Privacy requirements defined (GDPR, CCPA, HIPAA, etc.)

## Instructions

1. **Implement PII detection**: Scan prompts for personally identifiable information (names, emails, SSNs, phone numbers) using regex or a NLP-based PII detector before sending to the API
2. **Apply data minimization**: Only include data in prompts that is strictly necessary for the task; strip extraneous context, metadata, and user details
3. **Use placeholder substitution**: Replace PII with placeholders (e.g., `[USER_NAME]`, `[EMAIL]`) before sending, then re-substitute in the response
4. **Configure data retention**: Review OpenRouter's data retention policy; if your use case requires zero retention, check if the selected providers support it
5. **Implement consent tracking**: Log which users consented to AI processing and only send data for consented users; provide opt-out mechanisms

## Output

- PII detection middleware that flags or redacts sensitive data before API calls
- Data minimization checklist for prompt engineering
- Consent tracking system integrated with your user management

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| PII detected in prompt | User input contains sensitive data | Block the request and prompt the user to remove PII, or auto-redact |
| Missing consent record | User hasn't consented to AI processing | Block the request and redirect to consent flow |
| Data retention violation | Provider retains data longer than policy allows | Switch to a provider with compatible retention policy; check OpenRouter docs |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
