# Presentation Generation Deep Dive

This reference provides comprehensive guidance for creating high-quality presentations via the Canva MCP generate-design tool.

## Complete Presentation Query Format

When generating presentations, format the query string with ALL these sections in exact order:

### Section 1: Presentation Brief

```
**Presentation Brief**

* **Title**: [Working title for the deck - descriptive, not generic]
* **Topic / Scope**: [1-2 lines defining what this covers; include definitions for uncommon terms]
* **Key Messages**: 
  1. [First crisp takeaway - specific, actionable]
  2. [Second takeaway]
  3. [Third takeaway]
  4. [Fourth takeaway (optional)]
  5. [Fifth takeaway (optional)]
* **Constraints & Assumptions**: [Timebox, brand requirements, data limits, language, audience level]
* **Style Guide**: [Tone (professional/casual/inspirational), color palette hints, typography preferences, imagery style (photos/illustrations/icons)]
```

### Section 2: Narrative Arc

```
**Narrative Arc**

[One paragraph describing the story flow. Example:]
"Open with a provocative question about [pain point] (Hook). Present data showing the scale of the problem (Problem). Reveal the counterintuitive insight that [key insight] (Insight). Introduce [solution framework] as the answer (Solution). Prove it works with [case study/data] (Proof). Outline the implementation roadmap (Plan). Close with specific next steps and timeline (CTA)."
```

### Section 3: Slide Plan

For EACH slide, include ALL subsections in this exact order:

```
**Slide 1 — "[Exact Title - max 65 chars, action/insight-oriented]"**

* **Goal:** [One sentence describing this slide's purpose]
* **Bullets (3-6):**
  - [Short, parallel phrasing with specific facts/numbers]
  - [Avoid vague verbs like "improve" - use "increase by 40%"]
  - [Include examples where helpful]
  - [Each bullet 1-2 sentences max]
* **Visuals:** [Explicit recommendation - NOT "relevant image" but specific like:]
  - "Clustered bar chart comparing Q1-Q4 revenue by region"
  - "2×2 matrix: Risk vs. Reward with quadrant labels"
  - "Full-bleed photo of diverse team in modern office"
  - "Swimlane diagram showing 5-stage process"
  - "Icon grid: 4 icons representing core pillars"
* **Data/Inputs:** [Concrete values or realistic example figures:]
  - "$2.4M revenue, 34% YoY growth"
  - "Example values: 15% conversion, 2.3x ROI"
* **Speaker Notes:** [2-4 sentences with narrative details, definitions, context for presenter]
* **Asset Hint:** [Optional - reference uploaded asset: "Use Asset #2: company_logo.png as corner mark"]
* **Transition:** [One sentence logically leading to next slide]
```

## Quality Checklist (Self-Verify Before Submitting)

Before finalizing the query, verify:

- [ ] Titles are unique, ≤65 characters, action/insight-oriented (not "Overview" or "Introduction")
- [ ] Each slide has 3-6 bullets; no paragraph walls
- [ ] Numbers are specific where possible (not "significant increase" but "47% increase")
- [ ] Visuals are concrete (chart type + variables + timeframes)
- [ ] Tables only used when truly necessary
- [ ] Terminology defined once and used consistently
- [ ] Acronyms expanded on first use
- [ ] Transitions form intelligible narrative
- [ ] Story arc obvious from titles alone
- [ ] No placeholders like "[TBD]" or "[insert]" - use realistic example values instead
- [ ] All headers and subsections present in exact order

## Example: Complete Presentation Query

```
**Presentation Brief**

* **Title**: Building Passive Income Through Multifamily Real Estate
* **Topic / Scope**: Introduction to multifamily investing for beginners; covers property types, financing basics, and first-deal strategy
* **Key Messages**:
  1. Multifamily properties generate cash flow from day one with proper underwriting
  2. 5-20 unit properties offer the best risk/reward ratio for first-time investors
  3. Creative financing allows entry with 10-15% down vs. traditional 25%
  4. The BRRRR method (Buy, Rehab, Rent, Refinance, Repeat) enables portfolio growth
* **Constraints & Assumptions**: 45-minute webinar format; audience has basic investment knowledge but no real estate experience; no specific brand colors required
* **Style Guide**: Professional but approachable tone; dark blue and gold accents; clean photography of properties; minimal text per slide

**Narrative Arc**

Open with the frustration of trading time for money in traditional employment (Hook). Present data on wealth inequality and how the top 1% use real estate (Problem). Reveal that multifamily is accessible to everyday investors with proper education (Insight). Introduce the 4-pillar framework: Find, Fund, Fix, Fill (Solution). Share case study of first-time investor achieving $3,200/month cash flow (Proof). Outline the 90-day action plan to first deal (Plan). Close with free resource download and consultation booking CTA (CTA).

**Slide Plan**

**Slide 1 — "Your Money Works While You Sleep: The Multifamily Advantage"**

* **Goal:** Hook audience with the transformation possible through passive income
* **Bullets:**
  - Average W-2 employee works 40+ years to achieve "retirement"
  - Multifamily investors often reach financial freedom in 5-10 years
  - One 10-unit property can replace a $60K salary with 4 hours/month management
* **Visuals:** Split image: stressed office worker on left, relaxed investor on beach with laptop on right; timeline graphic showing 40 years vs. 7 years to financial freedom
* **Data/Inputs:** $60,000 annual passive income target; 10-unit property generating $6,000/month gross, $5,000 NOI
* **Speaker Notes:** Start with relatable frustration. Pause after "40+ years" for effect. The beach image isn't about laziness—it's about freedom to choose how you spend time. This sets up the contrast for the entire presentation.
* **Transition:** "But how do the wealthy actually make this happen? Let's look at the numbers..."

**Slide 2 — "The Wealth Gap Reality: Why Real Estate Dominates"**

* **Goal:** Establish credibility of real estate as wealth-building vehicle with data
* **Bullets:**
  - 90% of millionaires built wealth through real estate (Andrew Carnegie study)
  - Commercial multifamily market: $3.5 trillion in the US alone
  - Average annual returns: 9.4% (vs. 7.1% S&P 500 adjusted for volatility)
  - Tax advantages unavailable in stocks: depreciation, 1031 exchanges, cost segregation
* **Visuals:** Horizontal bar chart comparing 20-year returns: Multifamily RE vs. S&P 500 vs. Bonds vs. Savings; pie chart showing millionaire wealth sources
* **Data/Inputs:** 9.4% average annual return; $3.5T market size; 90% millionaire statistic
* **Speaker Notes:** The Carnegie study is from his famous quote, often cited but powerful. Emphasize "adjusted for volatility"—real estate has lower standard deviation. Tax advantages are the hidden multiplier most beginners miss.
* **Transition:** "Now that we've established WHY, let's talk about HOW to actually get started..."

[Continue for remaining slides...]
```

## Common Presentation Mistakes to Avoid

1. **Generic titles**: "Introduction" → "Why 83% of Retirees Regret Their Savings Strategy"
2. **Vague visuals**: "Relevant chart" → "Waterfall chart showing revenue sources Q1-Q4 2024"
3. **Missing specifics**: "Increased significantly" → "Increased 47% over 6 months"
4. **Wall-of-text bullets**: Keep each bullet to 1-2 lines max
5. **No transitions**: Each slide should logically flow to the next
6. **Inconsistent tone**: Match style guide throughout all slides
7. **Missing speaker notes**: These help AI understand context and generate better content

## Asset Integration for Presentations

When using `asset_ids` parameter:

1. Upload assets first via `upload-asset-from-url`
2. Note the returned asset IDs
3. Pass in order matching slide sequence:
   - `asset_ids: ["logo_id", "hero_image_id", "chart_id", "team_photo_id"]`
4. Reference in slide plan: "Asset Hint: Use Asset #1 as header logo"

The AI will place assets in corresponding slides based on order and hints.

## Presentation Types by Use Case

| Use Case | Recommended Slides | Key Focus |
|----------|-------------------|-----------|
| Sales pitch | 10-12 | Problem → Solution → Proof → CTA |
| Webinar | 15-25 | Education → Authority → Offer |
| Investor deck | 12-15 | Market → Product → Traction → Ask |
| Training | 20-30 | Concept → Examples → Practice → Review |
| Keynote | 8-12 | Story → Insight → Inspiration |
| Status update | 5-8 | Progress → Blockers → Next steps |
