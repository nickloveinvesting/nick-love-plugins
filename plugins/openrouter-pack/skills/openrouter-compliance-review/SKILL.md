---
name: openrouter-compliance-review
description: |
  Run a compliance review of your OpenRouter integration. Use when preparing for audits or governance reviews. Trigger with phrases like 'openrouter compliance', 'openrouter governance', 'openrouter security review', 'audit openrouter setup'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Compliance Review

## Overview

This skill provides a framework for reviewing your OpenRouter integration against security, privacy, and regulatory compliance requirements.

## Prerequisites

- OpenRouter integration in use
- Compliance requirements documented (SOC2, GDPR, HIPAA, etc.)

## Instructions

1. **Inventory data flows**: Map every place where data enters and exits the OpenRouter API — prompts, responses, headers, and logs — to understand your data exposure surface
2. **Review key management**: Verify API keys are stored in environment variables or a secrets manager (never in code), rotated on a schedule, and scoped to minimum required permissions
3. **Check data residency**: Confirm that the models and providers you use process data in regions that comply with your regulatory requirements (check OpenRouter's data processing docs)
4. **Validate logging practices**: Ensure audit logs capture required events without storing sensitive content; verify PII redaction and log retention policies
5. **Document and remediate**: Produce a compliance checklist with pass/fail status for each item; create tickets for any findings that need remediation

## Output

- Data flow diagram showing all touchpoints with the OpenRouter API
- Compliance checklist with pass/fail status for each requirement
- Remediation action items with priority and assignee

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| Missing data flow documentation | Integration added without review | Retroactively document; add compliance review to your deployment checklist |
| Keys in source code | Developer committed credentials | Rotate key immediately; add secret scanning to CI pipeline |
| Non-compliant data residency | Using models hosted in restricted regions | Restrict model selection to compliant providers; use OpenRouter's provider filtering |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
