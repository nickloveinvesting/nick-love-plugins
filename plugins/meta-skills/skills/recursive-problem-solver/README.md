# Recursive Problem Solver Skill

A comprehensive Claude skill for tackling complex problems through progressive deepening, self-critique, and validation loops.

## Overview

This skill transforms Claude into a recursively intelligent agent that:
- **Progressively deepens** analysis at increasing depth levels (0→1→2→3→4)
- **Self-critiques** reasoning at each level to identify flaws and gaps
- **Tracks confidence** objectively and iterates until threshold met (typically 85%+)
- **Validates solutions** before implementation to catch errors early
- **Manages context** by monitoring token usage and warning at capacity limits

## Quick Start

### When to Use This Skill

✅ **Always use when:**
- Critical decisions requiring >85% confidence
- Complex problems needing multi-step decomposition
- Solutions must be validated before implementation
- High-stakes scenarios where errors are costly

✅ **Consider using when:**
- Standard approaches feel stuck or unclear
- Multiple competing approaches exist
- Architectural or strategic decisions needed

❌ **Don't use when:**
- Simple, well-defined tasks
- Quick iterations needed
- Exploratory brainstorming (use regular mode)

### Basic Usage Pattern

1. **Start with sequential thinking** to break down the problem
2. **Use reflection for critique** at each depth level
3. **Track confidence rigorously** - be honest about uncertainty
4. **Stop when threshold met** (typically 85-92%)

### Example: Quick Problem-Solving

```
User: "Should we use Redis or Memcached for session storage?"

Claude (using recursive-problem-solver):

[Depth 0: Initial Analysis - Sequential Thinking]
- Both are in-memory caches
- Key differences: data structures, persistence, clustering
- Initial hypothesis: Redis for feature richness
- Confidence: 45%

[Depth 1: Critique via Reflection]
- Challenge: Do we need Redis features? (lists, sets, pub/sub)
- Challenge: What's the actual workload? (read/write ratio)
- Challenge: Team expertise with each?
- Refined hypothesis: Need more context about use case
- Confidence: 62%

[Depth 2: Deep Analysis]
- Use case: Simple key-value session storage
- Scale: 10K concurrent users
- Features needed: TTL, basic get/set
- Conclusion: Memcached is sufficient (simpler, faster for basic use)
- Confidence: 87% ✅

[Recommendation]
Use Memcached because:
- Session storage is simple key-value (don't need Redis data structures)
- Memcached has lower overhead for basic operations
- Team already familiar with Memcached
- Can migrate to Redis later if advanced features needed

Confidence: 87% - Ready to implement
```

## Documentation Structure

### Core Documentation

**📄 [SKILL.md](SKILL.md)** - Main skill documentation
- Core capabilities and operational framework
- Depth level explanations (0→4)
- Confidence scoring guidelines
- Workflow templates for different problem types
- Tool coordination (sequential-thinking + reflection)
- Context management protocol (token budget tracking)
- Best practices and troubleshooting

### Reference Materials

**📊 [references/confidence-metrics.md](references/confidence-metrics.md)** - Confidence scoring guide
- Mathematical scoring framework
- Confidence bands (90-100%, 75-89%, 60-74%, etc.)
- Calibration examples (well-calibrated vs over/under-confident)
- Confidence progression patterns
- Red flags for confidence inflation

**🎯 [references/patterns.md](references/patterns.md)** - Workflow pattern examples
- Pattern 1: Database Optimization (Deep Dive)
- Pattern 2: System Architecture Decision (Decision Framework)
- Pattern 3: Code Review (Validation Loop)
- Pattern 4: Topic Mastery (Learning Deep Dive)
- Pattern 5: API Design (Progressive Deepening)
- Each with full depth-by-depth walkthroughs

## Workflow Templates

The skill provides 4 main workflow templates:

### 1. Deep Dive (Complex Problems)
**Use for:** Architectural decisions, system design, strategic planning

**Process:** Depth 0 → Depth 1 → Depth 2 → Depth 3 → Synthesis

**Target confidence:** 85-92%

**Token budget:** ~25-35K tokens

### 2. Validation Loop (Solution Testing)
**Use for:** Code review, catching errors, verifying proposals

**Process:** Propose → Validate → Refine → Re-validate → Approve

**Target confidence:** 90%+

**Token budget:** ~20-25K tokens

### 3. Learning Deep Dive (Topic Mastery)
**Use for:** Understanding complex concepts, knowledge gaps, research

**Process:** Initial understanding → Gap identification → Deep dive on gaps → Integration → Validation

**Target confidence:** 85-92% understanding

**Token budget:** ~18-25K tokens

### 4. Decision Framework (Multi-Option Evaluation)
**Use for:** Choosing between alternatives, trade-off analysis

**Process:** Options generation → Deep evaluation → Comparative analysis → Risk assessment → Recommendation

**Target confidence:** 85-92%

**Token budget:** ~22-30K tokens

## Tool Integration

### Sequential Thinking Tool
**When:** Initial exploration, step-by-step reasoning, planning

**Pattern:**
```
Call: mcp-sequentialthinking-tools:sequentialthinking_tools
- Start with 5-8 estimated thoughts
- Each thought: 2-4 sentences
- Adjust total_thoughts as needed
- Set next_thought_needed=false when complete
```

### Reflection Tool
**When:** Self-critique, validation, finding gaps, challenging assumptions

**Pattern:**
```
Call: reflection:reflect
- Claim: Hypothesis or solution to validate
- Context: Problem description, constraints, previous insights
```

**Effective prompts:**
- "What am I missing about [topic]?"
- "Find flaws in this solution: [description]"
- "What could go wrong with: [approach]"
- "Challenge these assumptions: [list]"

## Confidence Tracking

### Confidence Bands

| Range | Level | Characteristics | Action |
|-------|-------|-----------------|--------|
| 90-100% | Extremely High | All edge cases addressed, validated | Implement |
| 75-89% | High | Core sound, ready with monitoring | Implement |
| 60-74% | Medium | Approach reasonable but incomplete | Continue analysis |
| 40-59% | Low | Initial hypothesis, many unknowns | Need deeper analysis |
| <40% | Very Low | Problem poorly understood | Refine question |

### Progression Pattern

**Good progression (healthy recursion):**
```
Depth 0: 44% → Depth 1: 65% → Depth 2: 81% → Depth 3: 92% ✅
```

**Bad progression (false confidence):**
```
Depth 0: 50% → Depth 1: 55% → Depth 2: 58% → Depth 3: 61% ❌
(Problem likely ill-defined or missing context)
```

## Context Management

### Token Budget Protocol

**CRITICAL:** Monitor token usage throughout recursive process.

| Usage | Status | Action |
|-------|--------|--------|
| <50% | ✅ Normal | Continue normally |
| 50-80% | ⚠️ Note | Track usage, continue |
| 80-90% | ⚠️ WARNING | Consider stopping or summarizing |
| >90% | 🚨 CRITICAL | Must summarize, offer to continue in new thread |

**Current budget:** 190K tokens total

**Warning threshold:** 152K tokens (80%)

### Context Length Warning Example

```
⚠️ CONTEXT LENGTH WARNING ⚠️
Token usage: 152K/190K (80%)

Current progress:
- Depth 0-2 completed
- Confidence: 78%
- Key insights: [bullet points]

Options:
1. Stop here (confidence below target 85%)
2. Continue to Depth 3 (may use 170K+ tokens)
3. Create summary and continue in fresh conversation

Which do you prefer?
```

## Quality Metrics

Track these to ensure effective recursion:

### 1. Confidence Progression
- Should increase 10-20% per depth level
- Good: Steady climb
- Bad: Barely increasing (problem ill-defined)

### 2. Insight Quality
- Each depth: 3-5 actionable insights
- Should challenge previous thinking
- Must be specific, not generic

### 3. Token Efficiency
- Depth 0: ~1-2K tokens
- Depth 1: ~2-4K tokens
- Depth 2: ~4-8K tokens
- Depth 3: ~8-15K tokens

### 4. Convergence
- Confidence should reach threshold by Depth 3-4
- If still low at Depth 4: question needs refinement

## Success Criteria

Recursion is successful when:
- ✅ Confidence reaches target threshold (typically 85%+)
- ✅ Key risks identified with mitigation strategies
- ✅ Trade-offs explicitly acknowledged
- ✅ Implementation path clear and feasible
- ✅ Edge cases considered
- ✅ Solution validated against constraints

## Troubleshooting

### Confidence Stuck at Low Levels
**Cause:** Question too broad or ill-defined

**Solution:** 
- Use initial sequential-thinking to clarify problem
- Add more context about constraints, objectives, scale

### Too Many Tokens Used
**Cause:** Thoughts too verbose or too many depth levels

**Solution:**
- Keep thoughts concise (2-4 sentences)
- Reduce max_depth
- Focus reflection on specific aspects

### Generic Insights
**Cause:** Missing context or vague prompts

**Solution:**
- Add specific context to reflection prompts
- Include tech stack, team size, scale, budget, timeline
- Ask for concrete examples in critiques

### Confidence Increases Too Slowly
**Cause:** Weak critique or missing self-challenge

**Solution:**
- Sharpen critique prompts
- Challenge assumptions more directly
- Look for edge cases and failure modes

## Configuration Guidelines

Adapt depth and thresholds based on task criticality:

| Task Type | Max Depth | Confidence Target | Token Budget |
|-----------|-----------|-------------------|--------------|
| Quick Tasks | 2 | 75% | ~50K |
| Standard Analysis | 3 | 85% | ~100K |
| Critical Decisions | 4 | 90% | ~150K |
| Research Deep Dive | 5+ | 92% | ~180K |

## Best Practices

1. ✅ **Always start with sequential-thinking** for initial exploration
2. ✅ **Use reflection for critique** at each depth level
3. ✅ **Track confidence rigorously** - be honest about uncertainty
4. ✅ **Monitor token usage** - warn at 80% capacity
5. ✅ **Stop when threshold met** - don't over-analyze
6. ✅ **Document insights** at each level for synthesis
7. ✅ **Validate before recommending** - test against edge cases
8. ✅ **Iterate based on confidence** - if <85%, go deeper or refine

## Examples

For detailed, step-by-step examples, see:
- **[patterns.md](references/patterns.md)** - 5 complete walkthroughs with actual tool calls
- **[confidence-metrics.md](references/confidence-metrics.md)** - Scoring calibration examples

## Integration with Other Tools

**Combine with Web Search:**
- Use recursion for analysis framework
- Search for specific data points as needed
- Validate assumptions against external sources

**Combine with File Operations:**
- Save depth-level summaries to files
- Reference previous analyses
- Build knowledge base over time

**Combine with Code Execution:**
- Test hypotheses with actual code
- Validate performance assumptions
- Iterate based on real results

## Version & License

**Version:** 1.0.0

**License:** MIT

**Created:** 2024

**Status:** Production-ready

---

## Quick Reference Card

**Basic pattern:**
1. Sequential-thinking (break down)
2. Reflection (critique)
3. Refine hypothesis
4. Score confidence
5. Repeat until threshold met (85%+)

**Stop conditions:**
- Confidence >= target (typically 85-92%)
- Max depth reached (typically 3-4)
- Token budget at 80% (152K/190K)

**Warning signs:**
- Confidence not increasing (problem ill-defined)
- Generic insights (need more context)
- Token usage too high (thoughts too verbose)

**Success indicators:**
- Steady confidence progression (10-20% per depth)
- Specific, actionable insights
- Edge cases identified
- Clear implementation path

---

**Get Started:** Read [SKILL.md](SKILL.md) for full documentation, then check [patterns.md](references/patterns.md) for concrete examples.
