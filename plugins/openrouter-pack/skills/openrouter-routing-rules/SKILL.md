---
name: openrouter-routing-rules
description: |
  Define custom routing rules for OpenRouter requests. Use when implementing complex routing logic beyond simple model selection. Trigger with phrases like 'openrouter rules', 'routing rules', 'custom routing', 'openrouter request routing'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Routing Rules

## Overview

This skill shows how to implement rule-based routing that dynamically selects models based on prompt content, user tier, cost constraints, or time-of-day patterns.

## Prerequisites

- OpenRouter integration with multiple models configured
- Routing requirements defined (by user tier, task type, cost, etc.)

## Instructions

1. **Define routing dimensions**: Identify the factors that should influence model selection — user tier (free/paid), task type (chat/code/analysis), cost budget, latency requirement
2. **Build a rules engine**: Create a configuration-driven rules engine where each rule has conditions (e.g., `user.tier == "free"`) and actions (e.g., `model = "google/gemma-2-9b-it:free"`)
3. **Implement rule evaluation**: Process rules in priority order; the first matching rule determines the model; always include a default/catch-all rule
4. **Add dynamic rules**: Support rules that query real-time data (current cost, model availability, error rates) to make routing decisions
5. **Test with rule scenarios**: Write test cases for each rule to verify correct model selection under different conditions

## Output

- A configurable rules engine that selects models based on multiple dimensions
- Rule configuration file (JSON/YAML) that can be updated without code changes
- Test suite validating each routing rule produces the correct model selection

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| No rule matched | Conditions don't cover all cases | Always include a default catch-all rule at the end |
| Rule evaluation error | Dynamic rule query failed (e.g., cost API timeout) | Add fallback values for dynamic data; never block on rule evaluation |
| Wrong model selected | Rule priority order incorrect | Add logging to show which rule matched and why; review priority ordering |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
