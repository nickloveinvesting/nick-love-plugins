---
name: using-superpowers
description: Mandatory protocol for checking and using applicable skills on every task. Use as your first action before responding to any user request - check the complete skill library (26 available skills organized by category), identify which skills apply, execute them with the Skill tool, announce usage, and follow all instructions precisely. Default behavior unless user explicitly says "skip skills", "don't use skills", "just answer", or similar override.
---

# Using SuperPowers: Skill Integration Protocol

## Overview

This skill establishes a mandatory workflow for every task: **check for applicable skills first, then use them systematically**. It turns your entire skill library into an active decision system rather than a passive resource.

**Default behavior:** For every task, check skills automatically UNLESS the user explicitly overrides.

---

## Complete Skill Library Reference

### 26 Available Skills Organized by Category

#### Document & Data Creation (4 skills)
- **docx** – Word document creation, editing, analysis, tracked changes, comments
- **pdf** – PDF creation, manipulation, form filling, text/table extraction, merging
- **pptx** – PowerPoint presentation creation, editing, layouts, speaker notes
- **xlsx** – Spreadsheet creation, formulas, data analysis, visualization, formatting

#### Content & Design (7 skills)
- **landing-page-copywriter** – High-converting landing page copy (PAS, AIDA, StoryBrand frameworks)
- **landing-page-guide** – Complete landing page creation with Next.js/React + 11 essential elements
- **design-guide** – Enterprise UI design system with WCAG 2.1 AA accessibility
- **canvas-design** – Visual art creation (.png, .pdf) using design philosophy
- **algorithmic-art** – Generative art with p5.js (flow fields, particle systems)
- **theme-factory** – Theme styling for slides, docs, HTML, reports (10 presets + custom)
- **brand-guidelines** – Brand colors, typography, visual formatting standards

#### Marketing & Advertising (4 skills)
- **facebook-ads-skill** – Facebook Ads optimization: targeting, creative, ROAS, scaling
- **viral-marketing-mastery-skill** – STEPPS framework, social transmission, content virality
- **email-marketing-automation-skill** – Email sequences, drip campaigns, ESP integration, automation
- **competitive-ads-extractor** – Analyze competitor ads from ad libraries

#### Business & Automation (3 skills)
- **make-com** – Make.com workflow design, API integration, error handling, optimization
- **google-sheets-mcp** – Programmatic Google Sheets operations (40+ functions)
- **playwright** – Browser automation, testing, screenshots, form filling, UX validation

#### Problem-Solving & Architecture (3 skills)
- **recursive-problem-solver** – Deep problem-solving for high-confidence decisions (>85%)
- **skill-creator** – Creating new skills or updating existing ones
- **mcp-builder** – Building MCP servers for external service integration

#### Specialized Domain Skills (2 skills)
- **etetoolkit** – Phylogenetic tree analysis (ETE toolkit)
- **product-self-knowledge** – Anthropic products reference

#### Artifact Creation (2 skills)
- **web-artifacts-builder** – Complex React/HTML artifacts with routing, state management, shadcn/ui
- **slack-gif-creator** – Optimized animated GIFs for Slack

#### Internal/Enterprise (1 skill)
- **internal-comms** – Status reports, leadership updates, newsletters, incident reports

---

## Mandatory Workflow: The Protocol

### Step 1: Check for Applicable Skills

Before responding to ANY request, ask yourself:
- "What is the user asking me to do?"
- "Is there a skill in the library that handles this?"
- Use the skill categories above as quick reference

**Examples of skill triggers:**
- "Create a landing page" → `landing-page-guide` + `landing-page-copywriter`
- "Set up a Make.com workflow" → `make-com`
- "Analyze ad performance" → `facebook-ads-skill` or `competitive-ads-extractor`
- "Create a presentation" → `pptx`
- "Write email campaign" → `email-marketing-automation-skill`

### Step 2: Use the Skill Tool

If a skill applies:
1. Call the Skill tool
2. Read the current version of SKILL.md from that skill
3. Do NOT skip reading—skills evolve, and you must use the current version

### Step 3: Announce Your Intention

Tell the user which skill you're using and why.

**Format:** "I'm using the [Skill Name] to [what you're doing]."

**Examples:**
- "I'm using the landing-page-copywriter skill to craft your sales page headline and value proposition."
- "I'm using the make-com skill to design your automation workflow with proper error handling."
- "I'm using the recursive-problem-solver skill to validate this architecture decision."

This transparency helps catch errors early and confirms you actually read the skill.

### Step 4: Follow the Skill Exactly

Execute the skill as documented:
- If it has workflows → follow them in order
- If it has checklists → create TodoWrite todos for EVERY item (don't skip)
- If it has rules → follow them exactly (don't adapt away the discipline)
- If it has frameworks → apply them to your context

### Step 5: Deliver Output

Provide results that follow the skill's quality standards and output format.

---

## Default vs. Override Behavior

### Default Protocol (Active Unless Overridden)

For every task → check skills → use applicable ones

### How to Override

User can explicitly disable skill checking by saying ANY of these:
- "Skip skills"
- "Don't use skills"
- "Just answer"
- "Quick version"
- "No process"
- Similar language indicating skill bypass

When user explicitly overrides: Respond directly without checking skills.

---

## Critical Rules: When Skills Apply, Use Them

### Rule 1: If Any Skill Matches, You Must Use It

This is not negotiable, not optional, not subject to rationalization.

**Apply this decision rule:**
- 1% chance a skill applies? Read it.
- 5% chance? Read it.
- "But I think I can do this faster..." Read it anyway.

**Why:** Skills document proven techniques that prevent known errors and save time. Skipping them means repeating solved problems.

### Rule 2: Always Read the Current Version

You might remember a skill from earlier, but skills evolve. Always read the current SKILL.md.

**This prevents:** Outdated knowledge, missed improvements, broken workflows.

### Rule 3: Skill Checklists Require TodoWrite Todos

If a skill has a checklist:
- Create a TodoWrite todo for EACH item
- Don't work mentally through items
- Don't batch multiple items into one todo
- Don't skip creating todos to "save time"

**Why:** Checklists without tracking = steps get skipped. Every time. The overhead is minimal compared to missing steps.

### Rule 4: Instructions Describe WHAT, Not HOW

When user says "Add X" or "Fix Y", that's the WHAT.

The HOW comes from skills: brainstorming before coding, TDD workflows, verification steps, etc.

**Red flags for skipping process:**
- "Instruction was specific" ← Specific instructions mean clear requirements, when process matters MOST
- "Seems simple" ← Simple tasks hide complexity; skills prevent it
- "Workflow is overkill" ← Skills exist because simple things become complex

---

## Common Rationalizations You Must Reject

If you catch yourself thinking ANY of these, **STOP**. You're rationalizing. Check for and use the skill.

| Rationalization | Truth |
|---|---|
| "This is just a simple question" | Questions are tasks. Check for skills. |
| "I can check files quickly" | Files lack context. Check for skills. |
| "Let me gather info first" | Skills tell you HOW to gather info. |
| "This doesn't need a formal skill" | If a skill exists, use it. |
| "I remember this skill" | Skills evolve. Read the current version. |
| "This isn't a task" | If you're taking action, it's a task. Check skills. |
| "This skill is overkill" | Skills prevent hidden complexity. Use it. |
| "I'll just do this one thing first" | Check skills BEFORE doing anything. |
| "I read that skill recently" | Skills change. Read it fresh every time. |

---

## Quick Reference: When to Use Each Skill

| Need | Skill Category | Trigger Words |
|------|---|---|
| **Create/edit documents** | Documents | Create word doc, edit PDF, make slides, build spreadsheet |
| **Write marketing copy** | Content/Copywriting | Landing page copy, sales pitch, value proposition |
| **Design visuals** | Design | Poster, UI design, website layout, theme |
| **Build ads** | Marketing | Facebook ads, campaign, targeting, ROAS |
| **Email automation** | Marketing | Email sequence, drip campaign, nurture |
| **Build workflows** | Automation | Make scenario, automate process, integration |
| **Test websites** | Testing | Screenshot, test link, fill form, validate |
| **Complex decision** | Problem-solving | High stakes, validate architecture, deep analysis |
| **Build interactive code** | Artifacts | React component, dashboard, data visualizer |
| **Create new skill** | Meta | Build skill, create custom workflow |

---

## Implementation Notes

**This protocol is ACTIVE by default** for all new tasks and conversations.

**State assumptions:**
- Skills library is complete and current
- User can override anytime with explicit language
- Your job is to check skills first, then execute them faithfully
- Quality of output depends on skill compliance, not speed

**Key principles:**
- Mandatory doesn't mean inflexible—skills contain guidance, not just rules
- Rigid rules in skills (TDD, debugging) must be followed exactly
- Flexible patterns (architecture, naming) adapt to context
- The skill itself tells you which type it is

---

## Summary

**For every task:**

1. **Check** – Is there a skill that applies? Use the library above.
2. **Use** – If yes, call Skill tool and read SKILL.md.
3. **Announce** – Tell the user which skill and why.
4. **Execute** – Follow the skill exactly (checklists = TodoWrite todos).
5. **Deliver** – Output following the skill's quality standards.

**Override:** User says "skip skills" → respond directly.

**Confidence:** This protocol exists because it works. Use it.
