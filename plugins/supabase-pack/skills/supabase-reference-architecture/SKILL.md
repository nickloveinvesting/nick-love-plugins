---
name: supabase-reference-architecture
description: |
  Implement Supabase reference architecture with best-practice project layout.
  Use when designing new Supabase integrations, reviewing project structure,
  or establishing architecture standards for Supabase applications.
  Trigger with phrases like "supabase architecture", "supabase best practices",
  "supabase project structure", "how to organize supabase", "supabase layout".
allowed-tools: Read, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Supabase Reference Architecture

## Prerequisites
- Understanding of layered architecture
- Supabase SDK knowledge
- TypeScript project setup
- Testing framework configured

## Instructions

A well-structured Supabase project separates concerns across distinct layers: the client initialization layer (singleton instance, environment configuration), the data access layer (typed query functions that encapsulate Supabase calls), the business logic layer (services that orchestrate data access), and the presentation or API layer (controllers or route handlers). This separation makes the codebase testable, maintainable, and easier to migrate if you ever need to swap out the underlying data provider.

### Step 1: Create Directory Structure
Set up the project layout following the reference structure above. Place all Supabase client initialization in a single `lib/supabase.ts` module that the rest of the codebase imports, rather than allowing each file to create its own client instance. Centralizing client creation simplifies configuration changes and prevents connection pool fragmentation.

### Step 2: Implement Client Wrapper
Create the singleton client with caching and monitoring. The wrapper should expose typed query functions that return domain objects rather than raw Supabase response types, decoupling your business logic from the specifics of the Supabase API surface.

### Step 3: Add Error Handling
Implement custom error classes that translate Supabase error codes into domain-specific exceptions. This makes error handling in higher layers cleaner and avoids leaking Supabase implementation details into your API error responses.

### Step 4: Configure Health Checks
Add a health check endpoint that performs a lightweight Supabase connectivity test — a simple count query against a small table is sufficient. This allows your infrastructure orchestration layer to detect connectivity issues and route traffic away from affected instances.

## Output
- Structured project layout with clear separation of Supabase integration concerns
- Singleton client wrapper with typed domain query functions
- Custom error hierarchy translating Supabase errors to domain exceptions
- Health check endpoint confirming live Supabase connectivity

## Error Handling

See `${CLAUDE_SKILL_DIR}/references/errors.md` for comprehensive error handling.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for detailed examples.

## Resources
- [Supabase SDK Documentation](https://supabase.com/docs/sdk)
- [Supabase Best Practices](https://supabase.com/docs/best-practices)

## Overview

Implement Supabase reference architecture with best-practice project layout.