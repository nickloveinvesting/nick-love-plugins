---
name: research-orchestrator
description: >
  Multi-workstream research orchestrator. Decomposes any research question into 2-4 focused workstreams, executes each with systematic web search, then synthesizes into a single coherent document with cross-cutting insights, contradictions, and confidence assessments. Use this skill whenever the user asks to "research", "deep dive", "analyze", "investigate", or "find out everything about" any topic. Also trigger when a question is complex enough that a single search would miss important angles — competitive analysis, market research, investment due diligence, scientific topics, strategic decisions, historical events, or any question where multiple perspectives matter. Activate proactively even if the user just says "help me understand X in depth."
---

# Research Orchestrator

Systematic multi-workstream research for any question. Decompose → Execute → Synthesize.

---

## Phase 1: Plan

Before searching anything:

1. **Understand the question.** What exactly needs to be learned? What decision or output will this research inform?

2. **Decompose into 2–4 workstreams.** Each workstream must have:
   - A clear, non-overlapping scope
   - 3–5 specific sub-questions or sections to answer
   - An implied search strategy (what sources, what angles)

3. **Present the plan to the user** in this format:

```
## Research Plan: [Topic]

**Core question:** [What we're actually trying to answer]

### Workstream 1: [Name]
**Scope:** [1 sentence]
**Key questions:**
1. [Question]
2. [Question]
3. [Question]

### Workstream 2: [Name]
...

### Synthesis
After all workstreams: cross-cutting themes, contradictions, confidence assessment, recommendations.

---
Proceed with this plan? Or adjust workstream scope?
```

4. **Wait for user confirmation** before executing. Do not begin research until approved.

---

## Phase 2: Execute Workstreams

Execute workstreams **sequentially** (Claude.ai constraint — no parallel agents). For each workstream:

### Search Protocol

For each sub-question in the workstream:
1. Run 1–3 targeted web searches (keep queries 2–5 words, specific)
2. Fetch full content from the most relevant result(s) using web_fetch
3. Extract and record findings before moving to the next search
4. Never run 3+ searches in a row without recording findings — research loops produce nothing

### Source Standards
- Every quantitative claim requires an inline source
- Prefer primary sources (company filings, peer-reviewed papers, official data) over aggregators
- If sources conflict, note the conflict — don't pick one arbitrarily
- Flag any finding where source quality is low or data is >2 years old

### Depth Calibration
- Simple factual question: 2–3 searches per workstream, ~200–400 words output
- Strategic/analytical question: 4–8 searches per workstream, ~500–1,000 words output
- Deep research request: 8–15 searches per workstream, 1,000–2,000 words output

### Progress Reporting
After completing each workstream, briefly report:
```
✓ Workstream 1 complete: [2-sentence summary of what was found]
Starting Workstream 2...
```

---

## Phase 3: Synthesize

After all workstreams complete, produce a synthesis document with these sections:

### 1. Executive Summary
3–5 bullets. The most important things learned. What would change decisions.

### 2. Key Findings by Theme
Organized by cross-cutting theme — NOT by workstream. This is the value-add: insights that span multiple workstreams, patterns that only emerge when the full picture is assembled.

### 3. Contradictions & Tensions
What did different workstreams find that conflicts? Where is the evidence genuinely uncertain? Do not paper over these — flag them explicitly.

### 4. Confidence Assessment
| Finding | Confidence | Basis |
|---------|-----------|-------|
| [Claim] | High / Medium / Low | [Why] |

High = multiple corroborating primary sources
Medium = single good source or multiple secondary sources
Low = limited data, old data, or conflicting sources

### 5. Recommended Next Steps
What should the user do with this research? What gaps remain? What would move low-confidence findings to high?

---

## Key Rules

1. **Never start research without user approval of the plan.** The decomposition IS the insight — wrong workstreams waste everything that follows.

2. **Write-then-search, not search-then-search.** After every 1–2 searches, record findings. Never queue up 5 searches and then try to synthesize from memory.

3. **Contradictions are features, not bugs.** If workstreams surface conflicting data, report it. The user hired a researcher, not a PR firm.

4. **Depth matches the question.** Don't produce a 3,000-word synthesis for a question that has a clear 200-word answer. Calibrate.

5. **Workstream scope should be exhaustive but non-overlapping.** If two workstreams would both naturally search for the same thing, adjust the split before launching.

6. **Flag source quality inline.** If you're citing a Reddit post or an SEO farm, say so. The user needs to know where the evidence is solid.

7. **The synthesis is not a summary.** It surfaces cross-cutting patterns, not a workstream-by-workstream recap. If the synthesis just repeats what each workstream said, it failed.

---

## Workstream Decomposition Patterns

Use these as starting points — adapt to the actual question:

**Competitive / Market Analysis**
- W1: Market structure & sizing
- W2: Competitor positioning & differentiation
- W3: Customer behavior & unmet needs
- W4: Regulatory / macro environment

**Investment / Deal Due Diligence**
- W1: Asset / business fundamentals
- W2: Market comparable & valuation
- W3: Risk factors & downside scenarios
- W4: Operator / management track record

**Technology Evaluation**
- W1: Technical capabilities & architecture
- W2: Adoption landscape & case studies
- W3: Limitations, failure modes & alternatives
- W4: Vendor / ecosystem health

**Person / Organization Research**
- W1: Background & track record
- W2: Public reputation & third-party assessments
- W3: Network, affiliations & interests
- W4: Recent activity & stated positions

**Strategic Decision Support**
- W1: Factual landscape (what is true now)
- W2: Expert opinion & practitioner experience
- W3: Historical precedents & analogues
- W4: Dissenting views & counterarguments

---

## Output Format Options

Ask the user (or infer from context) which output format they need:

- **Conversational**: Findings presented as prose in the chat. Good for quick research, single-question answers.
- **Structured report**: Synthesis document formatted with headers, tables, confidence ratings. Good for sharing, decision support, long shelf life.
- **Actionable brief**: Executive summary + top 3 recommendations only. Good for busy decisions.

Default to **structured report** unless the question is simple or the user signals otherwise.
