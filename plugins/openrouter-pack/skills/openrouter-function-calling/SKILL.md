---
name: openrouter-function-calling
description: |
  Implement function/tool calling with OpenRouter models. Use when building agents or structured outputs. Trigger with phrases like 'openrouter functions', 'openrouter tools', 'openrouter agent', 'function calling'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Function Calling

## Overview

This skill demonstrates implementing function calling and tool use patterns with OpenRouter-supported models.

## Prerequisites

- OpenRouter integration
- Model that supports function calling (GPT-4, Claude, etc.)

## Instructions

1. **Define tool schemas**: Create a `tools` array with JSON Schema definitions for each function, specifying name, description, and parameter types
2. **Send a request with tools**: Include the `tools` array in your chat completion request; set `tool_choice: "auto"` to let the model decide when to call functions
3. **Parse tool calls**: Extract `tool_calls` from `response.choices[0].message`, deserialize each `function.arguments` JSON string
4. **Execute and return results**: Run each function locally, then send a follow-up request with `role: "tool"` messages containing the results
5. **Handle multi-turn loops**: Continue the request-execute-respond cycle until the model returns a final text response without tool calls

## Output

- Model-generated function calls with properly typed arguments
- Multi-turn conversation with tool execution results fed back to the model
- Final synthesized response incorporating tool outputs

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| `tool_calls` is null | Model chose not to call tools or doesn't support them | Check model compatibility; use `tool_choice: "required"` to force |
| JSON parse error on arguments | Model generated malformed JSON | Wrap `JSON.parse` in try/catch; retry with a more capable model |
| 400 invalid tool schema | Schema has unsupported types or format | Use only JSON Schema draft-07 types; avoid `$ref` or complex constructs |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
