---
name: openrouter-audit-logging
description: |
  Implement audit logging for OpenRouter compliance. Use when meeting regulatory requirements or security audits. Trigger with phrases like 'openrouter audit', 'openrouter compliance log', 'openrouter security log', 'audit trail'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Audit Logging

## Overview

This skill demonstrates implementing comprehensive audit logging for security, compliance, and operational visibility.

## Prerequisites

- OpenRouter integration
- Audit requirements defined
- Log storage infrastructure

## Instructions

1. **Define audit event schema**: Create a structured log format that captures timestamp, user ID, model used, prompt hash (not raw content for privacy), token counts, cost, and response status
2. **Instrument the API client**: Add pre-request and post-response hooks that automatically log every OpenRouter API call with the defined schema
3. **Implement log storage**: Write audit logs to an append-only store (database table, S3 bucket, or centralized logging service) with retention policies
4. **Add PII redaction**: Before logging, scrub prompts and responses of personally identifiable information using regex patterns or a PII detection library
5. **Build audit queries**: Create reporting queries that answer common audit questions: who called what model, when, how much it cost, and whether any errors occurred

## Output

- Structured audit log entries for every API call with user, model, cost, and status
- PII-redacted log storage with configurable retention periods
- Audit reporting queries for compliance reviews and cost analysis

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| Log storage full | Retention policy not configured or too long | Implement log rotation and archival; set TTL on log entries |
| Missing audit entries | Logging middleware not covering all code paths | Centralize API calls through a single client wrapper with mandatory logging |
| PII leak in logs | Redaction patterns missing edge cases | Use a comprehensive PII detection library; review logs periodically for leaks |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
