---
name: vercel-reference-architecture
description: |
  Implement Vercel reference architecture with best-practice project layout.
  Use when designing new Vercel integrations, reviewing project structure,
  or establishing architecture standards for Vercel applications.
  Trigger with phrases like "vercel architecture", "vercel best practices",
  "vercel project structure", "how to organize vercel", "vercel layout".
allowed-tools: Read, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
compatible-with: claude-code, codex, openclaw
---
# Vercel Reference Architecture

## Prerequisites
- Understanding of layered architecture
- Vercel SDK knowledge
- TypeScript project setup
- Testing framework configured

## Instructions

A well-structured Vercel project separates concerns across distinct layers that align with Vercel's deployment model: the edge layer (middleware and edge functions for authentication, redirects, and A/B routing), the server layer (serverless API routes and server-side rendered pages), the client layer (static assets and client components), and the configuration layer (environment variables, headers, and rewrite rules). This separation makes each layer independently testable and ensures that decisions about caching, authentication, and data fetching are made at the optimal layer for the use case.

### Step 1: Create Directory Structure
Set up the project layout following the reference structure above. Organize API routes by domain feature rather than by HTTP method to keep related functionality co-located. Place middleware in the root-level `middleware.ts` file and scope it with path matchers to avoid running authentication logic on public static assets.

### Step 2: Implement Client Wrapper
Create a typed wrapper around any external API clients used by your serverless functions. The wrapper should handle authentication header injection, response parsing, and error normalization so that calling code does not need to handle Vercel-specific fetch patterns directly.

### Step 3: Add Error Handling
Implement a consistent error response format for API routes that distinguishes client errors (4xx with actionable messages) from server errors (5xx with request IDs for log correlation). Avoid leaking internal error details in production responses — log the full error server-side and return only a sanitized message to the client.

### Step 4: Configure Health Checks
Add a `/api/health` endpoint that verifies connectivity to your external dependencies (databases, third-party APIs) and returns a structured status response. Configure Vercel's deployment protection rules to run health checks after each deployment before promoting to production traffic.

## Output
- Structured project layout with clear separation across edge, server, and client layers
- Typed API client wrappers with consistent error normalization
- Standardized error response format with log correlation IDs
- Health check endpoint integrated into the deployment promotion flow

## Error Handling

See `${CLAUDE_SKILL_DIR}/references/errors.md` for comprehensive error handling.

## Examples

See `${CLAUDE_SKILL_DIR}/references/examples.md` for detailed examples.

## Resources
- [Vercel SDK Documentation](https://vercel.com/docs/sdk)
- [Vercel Best Practices](https://vercel.com/docs/best-practices)

## Overview

Implement Vercel reference architecture with best-practice project layout.