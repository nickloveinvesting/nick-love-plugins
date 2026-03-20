---
name: perplexity-core-workflow-a
description: |
  Execute Perplexity primary workflow: Core Workflow A.
  Use when implementing primary use case,
  building main features, or core integration tasks.
  Trigger with phrases like "perplexity main workflow",
  "primary task with perplexity".
allowed-tools: Read, Write, Edit, Bash(npm:*), Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Perplexity Core Workflow A

## Overview
Primary money-path workflow for Perplexity. This is the most common use case. Perplexity is an AI-powered answer engine that grounds its responses in real-time web searches, providing cited, up-to-date answers rather than responses based solely on training data. It is particularly valuable for research tasks that require current information, such as market analysis, technology trend monitoring, or fact-checking against live sources.

## Prerequisites
- Completed `perplexity-install-auth` setup
- Understanding of Perplexity core concepts
- Valid API credentials configured

## Instructions

### Step 1: Initialize
Authenticate with the Perplexity API and select the appropriate model — `sonar` for fast web-grounded answers or `sonar-pro` for deeper research with extended search coverage. Configure your system prompt if you want to shape the response format, language, or domain focus for your use case.

```typescript
// Step 1 implementation
```

### Step 2: Execute
Submit your research query to the Perplexity chat completions endpoint. The model will retrieve relevant web sources and synthesize a grounded answer. Examine the `citations` field in the response to identify which sources were consulted. Verify that the cited pages actually support the claims made in the answer before presenting the information externally.

```typescript
// Step 2 implementation
```

### Step 3: Finalize
Extract the answer text and citations from the API response. Format the citations as hyperlinks or footnotes according to your output requirements. If the answer is being incorporated into a document or report, note the query date alongside each citation since web content can change over time.

```typescript
// Step 3 implementation
```

## Output
- Completed Core Workflow A execution
- Grounded answer text with source citations from live web search
- List of supporting URLs for fact verification
- Success confirmation or error details if the query could not be fulfilled

## Error Handling
| Error | Cause | Solution |
|-------|-------|----------|
| Error 1 | Cause | Solution |
| Error 2 | Cause | Solution |

## Examples

### Complete Workflow
```typescript
// Complete workflow example
```

### Common Variations
- Variation 1: Description
- Variation 2: Description

## Resources
- [Perplexity Documentation](https://docs.perplexity.com)
- [Perplexity API Reference](https://docs.perplexity.com/api)

## Next Steps
For secondary workflow, see `perplexity-core-workflow-b`.