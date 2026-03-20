---
name: supabase-schema-from-requirements
description: |
  Execute Supabase primary workflow: Schema from Requirements.
  Use when Starting a new project with defined data requirements,
  Refactoring an existing schema based on new features, or Creating migrations from specification documents.
  Trigger with phrases like "supabase schema from requirements",
  "generate database schema with supabase".
allowed-tools: Read, Write, Edit, Bash(npm:*), Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Supabase Schema from Requirements

## Overview
Generate Supabase database schema from natural language requirements. This is the primary workflow for starting new Supabase projects. Translating business requirements directly into a well-structured Postgres schema with Row Level Security policies, appropriate indexes, and foreign key constraints is one of the highest-leverage activities in the early stages of a project. A well-designed schema is far cheaper to iterate on before data is in production than after.

## Prerequisites
- Completed `supabase-install-auth` setup
- Understanding of Supabase core concepts
- Valid API credentials configured

## Instructions

### Step 1: Initialize
Parse the natural language requirements into a structured entity list. Identify the main entities, their attributes, the relationships between them (one-to-one, one-to-many, many-to-many), and the access control rules that determine who can see or modify each entity. Clarify any ambiguous requirements before generating SQL to avoid costly schema revisions later.

```typescript
// Step 1 implementation
```

### Step 2: Execute
Generate the SQL migration file that creates the tables, defines foreign key constraints, adds appropriate indexes on foreign keys and frequently filtered columns, and sets up Row Level Security policies matching the identified access control rules. Review the generated schema for normalization issues and verify that the RLS policies correctly implement the intent of the requirements.

```typescript
// Step 2 implementation
```

### Step 3: Finalize
Apply the migration to your Supabase project and run integration tests that exercise each RLS policy with different user roles to confirm access control behaves as specified. Document the schema design decisions, particularly any denormalization choices made for performance reasons, so future maintainers understand the rationale.

```typescript
// Step 3 implementation
```

## Output
- Structured entity model derived from natural language requirements
- SQL migration creating tables, indexes, and RLS policies
- Verified schema with passing integration tests for each access control rule

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
- [Supabase Documentation](https://supabase.com/docs)
- [Supabase API Reference](https://supabase.com/docs/api)

## Next Steps
For secondary workflow, see `supabase-auth-storage-realtime-core`.