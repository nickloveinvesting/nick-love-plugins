---
name: openrouter-streaming-setup
description: |
  Implement streaming responses with OpenRouter. Use when building real-time chat interfaces or reducing time-to-first-token. Trigger with phrases like 'openrouter streaming', 'openrouter sse', 'stream response', 'real-time openrouter'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Openrouter Streaming Setup

## Overview

This skill demonstrates streaming response implementation for lower perceived latency and real-time output display.

## Prerequisites

- OpenRouter integration
- Frontend capable of handling SSE/streaming

## Instructions

1. **Enable streaming**: Set `stream: true` in your chat completion request body
2. **Handle SSE chunks**: Parse each `data: {...}` line from the response stream, extracting `choices[0].delta.content` from each chunk
3. **Detect stream end**: Watch for `data: [DONE]` to know when the stream is complete; accumulate chunks for the full response
4. **Implement frontend rendering**: Use `ReadableStream` or `EventSource` in the browser to display tokens as they arrive
5. **Add error recovery**: Handle mid-stream disconnections with automatic retry and partial response preservation

## Output

- Real-time token-by-token text output in the UI
- Reduced time-to-first-token compared to non-streaming requests
- Complete response assembled from all chunks with usage stats from the final chunk

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| Stream cuts off mid-response | Network timeout or model error | Implement reconnection logic; save partial output |
| Missing `usage` in stream | Some models omit usage in streaming mode | Set `stream_options: { include_usage: true }` or make a separate token count call |
| Empty delta chunks | Keep-alive pings from the server | Filter chunks where `delta.content` is null or empty |

See `${CLAUDE_SKILL_DIR}/references/errors.md` for full error reference.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for runnable code samples.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
