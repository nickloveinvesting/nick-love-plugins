---
name: fireflies-core-workflow-a
description: |
  Execute Fireflies.ai primary workflow: Core Workflow A.
  Use when implementing primary use case,
  building main features, or core integration tasks.
  Trigger with phrases like "fireflies main workflow",
  "primary task with fireflies".
allowed-tools: Read, Write, Edit, Bash(npm:*), Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Fireflies.ai Core Workflow A

## Overview
Primary money-path workflow for Fireflies.ai. This is the most common use case. Fireflies.ai is an AI meeting recorder and transcription service that automatically joins video calls, generates searchable transcripts, and extracts action items and summaries. Integrating Fireflies into your workflow eliminates manual note-taking and ensures that key decisions and follow-ups are captured consistently across all meetings.

## Prerequisites
- Completed `fireflies-install-auth` setup
- Understanding of Fireflies.ai core concepts
- Valid API credentials configured

## Instructions

### Step 1: Initialize
Authenticate with the Fireflies.ai API and verify that your workspace bot is properly configured to join meetings. Confirm that your calendar integrations (Google Calendar or Outlook) are connected so the bot receives invites automatically. Check that the preferred recording language and transcript format are configured according to your team's standards.

```typescript
// Step 1 implementation
```

### Step 2: Execute
Retrieve completed meeting transcripts using the Fireflies GraphQL API. Query by date range, participant, or meeting title to locate the recording you need. Access the full transcript text, speaker-diarized segments, and AI-generated summary. Review the action items extracted by Fireflies to determine which require follow-up assignment.

```typescript
// Step 2 implementation
```

### Step 3: Finalize
Export the transcript and action items to your downstream systems — project management tools, CRMs, or team wikis. Use the speaker labels and timestamps to attribute decisions correctly. Distribute the meeting summary to attendees who need a quick recap without reading the full transcript.

```typescript
// Step 3 implementation
```

## Output
- Completed Core Workflow A execution
- Full transcript with speaker attribution and timestamps
- AI-generated summary and extracted action items
- Success confirmation or error details if the transcript could not be retrieved

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
- [Fireflies.ai Documentation](https://docs.fireflies.com)
- [Fireflies.ai API Reference](https://docs.fireflies.com/api)

## Next Steps
For secondary workflow, see `fireflies-core-workflow-b`.