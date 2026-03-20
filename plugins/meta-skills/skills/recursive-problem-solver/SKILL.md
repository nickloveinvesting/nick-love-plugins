---
name: recursive-problem-solver
description: Implements recursive reflection and progressive deepening for complex problem-solving. Use when tasks require high confidence (>85%), critical decisions, multi-perspective analysis, validation of solutions, or breaking down complex problems into subtasks with iterative refinement. Provides self-critique, confidence tracking, and context management.
license: MIT
---

# Recursive Problem Solver

Transform into a recursively intelligent agent through progressive deepening, self-critique, and validation loops.

## Core Capabilities

1. **Progressive Deepening** - Analyze problems at increasing depth levels (0→1→2→3→4)
2. **Self-Critique** - Challenge own reasoning at each level
3. **Confidence Tracking** - Measure certainty and iterate until threshold met
4. **Validation Loops** - Test solutions before implementation
5. **Context Management** - Monitor token usage, warn at 80% capacity

## When to Use This Skill

**Always use when:**
- Critical decisions requiring >85% confidence
- Complex problems needing multi-step decomposition
- Solutions that must be validated before implementation
- High-stakes scenarios where errors are costly
- Context length approaching limits (need to compress/summarize)

**Consider using when:**
- Standard problems feel stuck or unclear
- Multiple competing approaches exist
- Learning complex topics requiring depth
- Architectural or strategic decisions

**Don't use when:**
- Simple, well-defined tasks
- Quick iterations needed
- Confidence threshold already met
- Exploratory brainstorming (use regular mode instead)

## Operational Framework

### Depth Levels Explained

**Depth 0: Initial Analysis**
- Quick assessment of the problem
- Identify key constraints and objectives
- Generate initial hypothesis
- Baseline confidence: typically 40-60%

**Depth 1: First Critique**
- Challenge assumptions from Depth 0
- Identify overlooked factors
- Consider alternative approaches
- Confidence target: 60-75%

**Depth 2: Deep Analysis**
- Examine edge cases and failure modes
- Evaluate trade-offs systematically
- Quantify risks and benefits
- Confidence target: 75-85%

**Depth 3: Validation & Refinement**
- Test hypothesis against constraints
- Identify implementation challenges
- Refine solution based on critiques
- Confidence target: 85-92%

**Depth 4+: Expert-Level (Optional)**
- Second-order effects analysis
- Long-term implications
- Systemic interactions
- Confidence target: 92%+

### Confidence Scoring Guidelines

Score solutions objectively using these criteria:

**90-100%: Extremely High Confidence**
- All major edge cases addressed
- Trade-offs explicitly acknowledged
- Implementation path clear
- Risks quantified and mitigated
- Multiple validation passes completed

**75-89%: High Confidence**
- Core approach sound
- Major concerns addressed
- Some edge cases may remain
- Trade-offs identified
- Ready for implementation with monitoring

**60-74%: Medium Confidence**
- Approach reasonable but incomplete
- Several concerns unresolved
- More analysis needed
- Not ready for critical decisions

**40-59%: Low Confidence**
- Initial hypothesis only
- Many unknowns remain
- Requires deeper analysis
- Multiple competing approaches

**<40%: Very Low Confidence**
- Problem poorly understood
- Question needs refinement
- More context required

## Recursive Workflow Process

### Phase 1: Problem Decomposition

```
1. Use sequential-thinking to break down the problem
2. Identify: objectives, constraints, success criteria
3. Generate initial hypothesis (Depth 0)
4. Score confidence (target: 40-60%)
```

**Tool to use:** `mcp-sequentialthinking-tools:sequentialthinking_tools`

**Template:**
- Thought 1: Understand the core problem
- Thought 2-3: Identify constraints and objectives
- Thought 4-5: Generate initial approach
- Thought 6: Score initial confidence

### Phase 2: Progressive Deepening

For each depth level (1 through target depth):

```
1. Use reflection tool to critique previous level
2. Challenge assumptions systematically
3. Identify gaps and alternatives
4. Refine hypothesis based on critiques
5. Score confidence at new level
6. STOP if confidence >= threshold OR max_depth reached
```

**Tool to use:** `reflection:reflect`

**Critique patterns to use:**
- "What assumptions am I making that could be wrong?"
- "What am I overlooking or not considering?"
- "What could go wrong with this approach?"
- "Are there better alternatives?"
- "What are the trade-offs I'm not seeing?"

### Phase 3: Validation

```
1. Test solution against edge cases
2. Evaluate implementation feasibility
3. Identify risks and mitigation strategies
4. Final confidence check
5. If confidence < threshold: return to Phase 2 with deeper analysis
```

### Phase 4: Implementation Recommendation

```
1. Synthesize insights from all depth levels
2. Provide clear, actionable recommendation
3. Include confidence score and key caveats
4. Warn about remaining risks
```

## Workflow Templates

### Template 1: Deep Dive (Complex Problem)

**Use for:** Architectural decisions, system design, strategic planning

**Process:**
1. **Initial Exploration** (Depth 0)
   - Use sequential-thinking: Break down problem (5-8 thoughts)
   - Identify: objectives, constraints, initial approach
   - Score confidence

2. **First Critique** (Depth 1)
   - Use reflection: "What am I overlooking in this approach: [paste Depth 0 summary]"
   - Refine based on critique
   - Score confidence

3. **Deep Analysis** (Depth 2)
   - Use reflection: "What could go wrong with this refined approach: [paste Depth 1 summary]"
   - Examine edge cases and trade-offs
   - Score confidence

4. **Validation** (Depth 3)
   - Use reflection: "Validate this solution against constraints: [paste Depth 2 summary]"
   - Test implementation feasibility
   - Score confidence

5. **Synthesis**
   - If confidence >= 85%: Provide final recommendation
   - If confidence < 85%: Continue to Depth 4 or refine question

### Template 2: Validation Loop (Solution Testing)

**Use for:** Verifying proposed solutions, catching errors, code review

**Process:**
1. **Propose Solution** (Depth 0)
   - Use sequential-thinking: Develop initial solution
   - Document approach clearly
   - Score confidence

2. **First Validation** (Depth 1)
   - Use reflection: "Find flaws in this solution: [solution description]"
   - List specific critiques
   - Severity assessment

3. **Refinement** (Depth 2)
   - Address each critique systematically
   - Use sequential-thinking: Develop improved solution
   - Score confidence

4. **Second Validation** (Depth 3)
   - Use reflection: "Validate refined solution: [improved solution]"
   - Check if previous critiques resolved
   - Score confidence

5. **Decision**
   - If confidence >= 85%: Approve for implementation
   - If confidence < 85%: Iterate or reconsider approach

### Template 3: Learning Deep Dive (Topic Mastery)

**Use for:** Understanding complex concepts, knowledge gaps, research

**Process:**
1. **Initial Understanding** (Depth 0)
   - Provide high-level explanation of topic
   - Score own understanding confidence

2. **Gap Identification** (Depth 1)
   - Use reflection: "What am I missing about [topic]?"
   - List knowledge gaps and unclear areas
   - Prioritize gaps by importance

3. **Deep Dive on Gaps** (Depth 2)
   - Address each major gap systematically
   - Provide detailed explanations
   - Score understanding confidence

4. **Integration** (Depth 3)
   - Connect concepts into coherent framework
   - Test understanding with examples
   - Score final understanding

5. **Validation**
   - If confidence >= 85%: Knowledge acquisition complete
   - If confidence < 85%: Identify remaining gaps, continue

### Template 4: Decision Framework (Multi-Option Evaluation)

**Use for:** Choosing between alternatives, trade-off analysis

**Process:**
1. **Options Generation** (Depth 0)
   - Use sequential-thinking: List all viable options
   - Initial pros/cons for each
   - Preliminary ranking

2. **Deep Evaluation** (Depth 1-2)
   - For each option, use reflection: "What are the hidden costs/risks of [option]?"
   - Uncover non-obvious factors
   - Quantify trade-offs where possible

3. **Comparative Analysis** (Depth 3)
   - Use reflection: "Compare options considering: [all factors identified]"
   - Weight factors by importance
   - Identify clear winner or hybrid approach

4. **Risk Assessment** (Depth 4)
   - Use reflection: "What could go wrong with chosen option: [decision]"
   - Mitigation strategies for each risk
   - Final confidence score

5. **Recommendation**
   - Clear decision with rationale
   - Confidence score
   - Key risks and mitigations

## Context Management Protocol

**CRITICAL:** Monitor token usage throughout recursive process.

**Check token usage after each depth level:**
- <50% used: Continue normally
- 50-80% used: Note current usage, continue
- 80-90% used: **WARNING** - Approaching limit. Consider:
  - Stopping at current depth
  - Summarizing key insights before continuing
  - Switching to new conversation with summary
- >90% used: **CRITICAL** - Must summarize and offer to continue in new thread

**When approaching limit:**
1. Summarize all insights from current depth levels
2. Provide current confidence score
3. Offer user: "We're at [X]% token capacity. Options:
   - Stop here with current confidence: [Y]%
   - Continue in new conversation with this summary: [paste summary]"

**Example warning:**
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

## Configuration Guidelines

Adapt depth and thresholds based on task criticality:

**Quick Tasks** (Target: 5-10 min)
- Max depth: 2
- Confidence threshold: 75%
- Token budget awareness: 50K

**Standard Analysis** (Target: 10-20 min)
- Max depth: 3
- Confidence threshold: 85%
- Token budget awareness: 100K

**Critical Decisions** (Target: 20-30 min)
- Max depth: 4
- Confidence threshold: 90%
- Token budget awareness: 150K

**Research Deep Dive** (Target: 30+ min)
- Max depth: 5+
- Confidence threshold: 92%
- Token budget awareness: 180K

## Tool Coordination

### Using Sequential-Thinking Tool

**When:** Initial exploration, step-by-step reasoning, implementation planning

**Pattern:**
```
Call: mcp-sequentialthinking-tools:sequentialthinking_tools
Parameters:
- thought: Current reasoning step
- thought_number: Progressive count
- total_thoughts: Estimate (can adjust)
- next_thought_needed: true/false
```

**Best practices:**
- Start with 5-8 estimated thoughts
- Adjust total_thoughts if more analysis needed
- Each thought should be 2-4 sentences
- Set next_thought_needed=false when depth level complete

### Using Reflection Tool

**When:** Self-critique, validation, finding gaps, challenging assumptions

**Pattern:**
```
Call: reflection:reflect
Parameters:
- claim: Hypothesis or solution to validate
- context: Problem description, constraints, previous insights
```

**Effective prompts:**
- "What am I missing about [topic]?"
- "Find flaws in this solution: [description]"
- "What could go wrong with: [approach]"
- "Challenge these assumptions: [list]"
- "Are there better alternatives to: [current approach]"

## Quality Metrics

Track these metrics to ensure effective recursion:

**1. Confidence Progression**
- Should increase with each depth level
- Good: 44% → 61% → 78% → 91%
- Bad: 44% → 47% → 49% → 51% (problem needs refinement)

**2. Insight Quality**
- Each depth should produce 3-5 actionable insights
- Insights should be specific, not generic
- Should challenge previous level's thinking

**3. Token Efficiency**
- Depth 0: ~1K-2K tokens
- Depth 1: ~2K-4K tokens  
- Depth 2: ~4K-8K tokens
- Depth 3: ~8K-15K tokens
- If using significantly more: thoughts may be too verbose

**4. Convergence**
- Confidence should reach threshold by Depth 3-4 for most problems
- If still low at Depth 4: question may be ill-defined

## Troubleshooting

**Problem:** Confidence stuck at low levels
**Solution:** 
- Question may be too broad or ill-defined
- Use initial sequential-thinking to clarify problem
- Add more context about constraints, objectives, scale

**Problem:** Too many tokens used
**Solution:**
- Keep thoughts concise (2-4 sentences)
- Reduce max_depth
- Focus reflection on specific aspects, not entire solution

**Problem:** Generic insights, not actionable
**Solution:**
- Add specific context to reflection prompts
- Include: tech stack, team size, scale, budget, timeline
- Ask for concrete examples in critiques

**Problem:** Confidence increases too slowly
**Solution:**
- Sharpen critique prompts
- Challenge assumptions more directly
- Look for edge cases and failure modes

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

## Examples

See `references/patterns.md` for detailed workflow examples:
- Database optimization (Deep Dive)
- System architecture (Decision Framework)
- Code review (Validation Loop)
- Topic mastery (Learning Deep Dive)

See `references/confidence-metrics.md` for scoring guidance and calibration examples.

## Best Practices Summary

1. **Always start with sequential-thinking** for initial exploration
2. **Use reflection for critique** at each depth level
3. **Track confidence rigorously** - be honest about uncertainty
4. **Monitor token usage** - warn at 80% capacity
5. **Stop when threshold met** - don't over-analyze
6. **Document insights** at each level for synthesis
7. **Validate before recommending** - test against edge cases
8. **Iterate based on confidence** - if <85%, go deeper or refine

## Success Criteria

Recursion is successful when:
- ✅ Confidence reaches target threshold (typically 85%+)
- ✅ Key risks identified and mitigation strategies proposed
- ✅ Trade-offs explicitly acknowledged
- ✅ Implementation path clear and feasible
- ✅ Edge cases considered
- ✅ Solution validated against constraints
- ✅ User has high confidence to proceed

Recursion should continue when:
- ❌ Confidence below threshold
- ❌ Major concerns unresolved
- ❌ Alternatives not fully explored
- ❌ Edge cases not considered
- ❌ Implementation feasibility unclear
- ❌ High-risk factors not mitigated
