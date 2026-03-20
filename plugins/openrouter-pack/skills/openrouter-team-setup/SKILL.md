---
name: openrouter-team-setup
description: |
  Configure OpenRouter for multi-user team environments. Use when setting up shared access or team-level controls. Trigger with phrases like 'openrouter team', 'openrouter multi-user', 'openrouter organization', 'team api keys'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Team Setup

## Overview

This skill covers configuring OpenRouter for team use, including per-user API key strategies, usage tracking by team member, and shared budget management.

## Prerequisites

- OpenRouter account with admin access
- Team structure and access requirements defined

## Instructions

1. **Design the key strategy**: Choose between per-user keys (best for attribution) or shared service keys (best for centralized control); consider a hybrid with a shared key plus user identification headers
2. **Implement user tracking**: Pass `X-Title` header with user or team identifiers so usage shows up attributed in the OpenRouter dashboard
3. **Set per-user budgets**: Create separate keys with individual credit limits for each team member or team, preventing any single user from exhausting the shared budget
4. **Build a usage dashboard**: Aggregate per-user token counts and costs from your audit logs; display daily/weekly spend by user and model
5. **Establish governance policies**: Define which models each team can use, set approval workflows for expensive models, and configure alerts when users approach their limits

## Output

- API key management strategy document for the team
- Per-user usage tracking and attribution system
- Team budget dashboard with per-user spend visibility

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| User exceeds personal budget | No per-user limits set | Create individual keys with credit limits; implement middleware budget checks |
| Attribution missing | Requests not tagged with user ID | Enforce `X-Title` header in shared client wrapper; reject untagged requests |
| Key sprawl | Too many keys to manage | Consolidate to service keys with user headers; implement key lifecycle management |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
