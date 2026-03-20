---
name: openrouter-context-optimization
description: |
  Optimize token usage and context window management. Use when reducing costs or fitting more information into model context. Trigger with phrases like 'openrouter context', 'token optimization', 'context window', 'reduce tokens'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Context Optimization

## Overview

This skill covers techniques for managing token budgets, optimizing prompt length, and making the most of each model's context window.

## Prerequisites

- OpenRouter integration
- Tokenizer library (tiktoken for OpenAI models, or approximate counting)

## Instructions

1. **Count tokens before sending**: Use `tiktoken` (Python) or `js-tiktoken` (JS) to estimate token counts before making API calls; abort if the prompt exceeds the model's context limit
2. **Implement conversation pruning**: For multi-turn chats, drop or summarize older messages when total tokens approach the context limit, keeping system prompts and recent messages
3. **Optimize system prompts**: Move static instructions to the system message and keep them concise; every token in the system prompt is repeated on every request
4. **Use response length controls**: Set `max_tokens` to the minimum needed for your use case; shorter completions cost less and return faster
5. **Select models by context need**: Route short-context tasks to cheaper models and reserve large-context models (128K+) for tasks that genuinely need them

## Output

- Token budget calculator that warns before exceeding context limits
- Conversation pruning middleware that keeps chats within context bounds
- Cost reduction from optimized prompt engineering (typically 20-40% savings)

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| 400 `context_length_exceeded` | Prompt + max_tokens exceeds model limit | Prune messages or switch to a model with a larger context window |
| Truncated responses | `max_tokens` set too low | Increase `max_tokens` or split the task into smaller requests |
| Token count mismatch | Wrong tokenizer for the model | Use the correct tokenizer per model family; fall back to rough estimation (1 token ~ 4 chars) |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
