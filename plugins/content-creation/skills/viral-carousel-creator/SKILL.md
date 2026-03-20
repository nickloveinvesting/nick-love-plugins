---
name: viral-carousel-creator
description: Create viral carousel posts for TikTok Photo Mode and Instagram with research-backed frameworks, hook writing, slide architecture, and design specifications. Use when the user wants to create carousel content, write carousel hooks, design slide sequences, plan carousel campaigns, generate carousel copy, build carousel templates, or optimize existing carousels for engagement. Also trigger when user mentions "carousel," "photo mode," "swipe post," "slide deck for social," "multi-image post," or any request involving multi-slide social media content creation. Covers the full pipeline from hook writing through slide scripting, visual design specs, and platform-specific optimization.
allowed-tools: Read Write Edit Grep Glob WebSearch WebFetch AskUserQuestion
---

# Viral Carousel Creator

Create high-engagement carousel content for TikTok Photo Mode and Instagram using research-backed frameworks, proven hook patterns, psychological trigger words, and a complete visual design system.

Carousels are the highest-leverage organic format in 2026. TikTok carousels generate 81% more engagement than video. Instagram carousels produce 1.9x higher reach than single images and 3x more engagement. Every swipe is a micro-commitment that signals active engagement to the algorithm.

---

## Step 1: Gather Context

Before generating any content, determine what you're working with.

**If the user provides a topic or request directly**, extract:
- Content topic or theme
- Target platform (TikTok, Instagram, or both)
- Brand voice and visual identity (if known)
- Target audience
- Goal (awareness, engagement, leads, sales)
- Whether they need hooks only, full slide scripts, design specs, or the complete package

**If context is missing**, ask:
"I'll build your carousel content. What's the topic, who's the audience, and which platform — TikTok, Instagram, or both?"

Apply defaults for anything not specified:
- Platform: Both TikTok and Instagram
- Slide count: 8-10 slides
- Goal: Maximize saves and shares
- Voice: Professional, direct, authority-driven

---

## Step 2: Read Reference Files

**MANDATORY before generating any output.** Read the reference files relevant to the task:

| Task | Files to Read |
|------|--------------|
| Writing hooks | `./references/hook-patterns.md` + `./references/trigger-words.md` |
| Full carousel script | All reference files relevant to the content type |
| Design specs only | `./references/design-system.md` |
| Campaign planning | All reference files |
| Optimizing existing carousel | `./references/slide-architecture.md` + `./references/design-system.md` |
| Understanding why carousels go viral | `./references/psychology-engine.md` |
| B2B / high-ticket lead gen carousels | `./references/conversion-system.md` + `./references/hook-patterns.md` |
| Comment-to-DM automation setup | `./references/conversion-system.md` |

Reference files:
- `./references/hook-patterns.md` — 25+ hook patterns (19 general + 6 carousel-specific + 3 engineering templates) with selection matrices
- `./references/trigger-words.md` — 4 categories of viral trigger words with integration guidelines
- `./references/slide-architecture.md` — 10-slide framework, pacing rules, content type templates, CTA tactics, and metrics
- `./references/design-system.md` — Typography, color psychology, layout patterns, visual devices, precise safe zones (840x1280), audio strategy, OCR/SEO, and reverse swipe engineering
- `./references/psychology-engine.md` — Dual-system theory (Kahneman), cognitive biases matrix, Information Gap Theory, PAS framework, 4U Formula, System 1→2 transition architecture
- `./references/conversion-system.md` — B2B copywriting formulas (Symptom/Root Cause, Enemy/Hero, Myth Buster, PAS), Comment-to-DM automation, ManyChat DM sequences, funnel math, A/B testing framework

---

## Step 3: Generate the Hook

The hook carries 80% of the weight. Slide 1 determines whether the viewer stops or scrolls.

### Hook Generation Process

1. **Select 2-3 hook patterns** from `hook-patterns.md` that match the content goal and platform using the Pattern Selection Matrix.
2. **Draft each hook** using the pattern template as the starting structure.
3. **Integrate 1-2 trigger words** from `trigger-words.md` into each hook:
   - Insider words → exclusivity patterns
   - Helper words → problem/urgency patterns
   - Thinker words → contrarian patterns
   - Amplifiers → any pattern for intensity boost
4. **Apply carousel-specific hook rules:**
   - Maximum 10 words on slide 1 (ideal: 8)
   - Must pass the Squint Test (readable when eyes are squinted, simulating scroll speed)
   - Create an open loop that demands swiping to resolve
   - Lead with the most emotionally charged element

### Hook Output Format

For each hook option:
```
### [Pattern Name]
[Hook text — under 10 words]

**Trigger words used:** [word1], [word2]
**Psychology:** [One sentence on why this stops the scroll]
**Slide 2 bridge:** [What slide 2 says to validate and pull forward]
```

Generate 3 hook options minimum. Each must use a different pattern.

---

## Step 4: Script the Full Carousel

Use the 10-Slide Architecture from `slide-architecture.md`:

| Slide | Function | Rules |
|-------|----------|-------|
| 1 | HOOK | One idea. Under 10 words. 80% of the weight. |
| 2 | INSTANT VALUE | No warmup. Jump into the meat immediately. |
| 3-5 | CORE VALUE | One point per slide. Flashcard, not paragraph. |
| 6-7 | BUILD + PROOF | Data, case study, or transformation moment. |
| 8 | OPEN LOOP | Tease what most people miss. Pull forward. |
| 9 | PAYOFF | Deliver the promised insight or conclusion. |
| 10 | CTA | Comment, save, share, or DM keyword. |

### Slide Script Format

For each slide, provide:
```
**Slide [N] — [FUNCTION]**
Headline: [Main text — bold, large]
Supporting: [Secondary text — smaller, lighter weight]
Visual note: [Layout template, accent elements, or design direction]
Micro-hook: [Phrase or element that pulls to the next slide]
```

### Pacing Rules
- One point per slide. No exceptions.
- Bold the key phrase on every slide. Keep supporting text short.
- Use open loops between slides ("Next: the fix that takes 2 minutes").
- Put a soft CTA mid-way and a hard CTA on the last slide.
- Make saves rational (templates, frameworks, checklists).
- Make shares social ("Send this to the person who handles hiring").

---

## Step 5: Specify the Visual Design

Reference `design-system.md` for all specifications. Key non-negotiables:

**Hook slide:** 70-100pt headline. Maximum contrast. Under 10 words. Zero clutter.

**Body slides:** 40-50pt headlines. 26-30pt supporting text. One focal point per slide. 60% white space / 40% content.

**TikTok safe zone:** Keep text in center 1080x1520px area (top 150px and bottom 250px covered by UI).

**Instagram safe zone:** Keep important text in top 60% of image.

**Consistency:** Same color palette, typography, and layout grid across all slides. Swipe indicator on every slide. Brand identifier (headshot + name) in consistent position.

### Design Spec Output Format

When providing design specifications:
```
**Dimensions:** [Platform-specific]
**Background:** [Color hex]
**Primary text:** [Color hex + font + weight]
**Accent:** [Color hex + usage]
**Layout template:** [Centered Statement / Progressive List / Split Frame]
**Slide 1 layout:** [Specific placement of hook text, brand identifier, swipe cue]
**Body slide layout:** [Repeating structure for slides 2-9]
**CTA slide layout:** [Reversed colors or distinct treatment]
```

---

## Step 6: Platform Optimization

### TikTok Photo Mode
- Upload as native Photo Mode (not video slideshow) for algorithm boost
- Add trending sound that matches the content mood
- Write caption with search keywords (TikTok indexes text on slides + captions)
- Optimal slide count: 5-10 for engagement, 4-8 for completion rate
- Dimensions: 1080x1920px (9:16)

### Instagram Carousels
- Use triple-hook strategy: slides 1-3 each function as standalone hooks (Instagram re-serves carousels starting from later slides)
- Optimal slide count: 5-8
- Dimensions: 1080x1350px (4:5) or 1080x1080 (1:1)
- Reinforce CTA in both final slide and caption

### Cross-Posting
- Design at 1080x1920 for TikTok first
- Adjust to 1080x1350 for Instagram (reposition text within safe zones)
- Adapt caption for each platform's search behavior

---

## Step 7: Metrics and Targets

| Metric | Target | Why |
|--------|--------|-----|
| Swipe-Through Rate | 60%+ | Primary algorithm signal. Below 40% = content dies. |
| Completion Rate | 70%+ | Viewers reaching last slide. Signals strong arc. |
| Dwell Time / Slide | 3-5 seconds | Sweet spot between engagement and confusion. |
| Save Rate | Highest possible | Strongest quality signal in 2026. |
| Share Rate | Track weekly | Fastest path to viral distribution. |
| Reverse Swipe Rate | Any occurrence | Re-reading = content so valuable they go back. |

---

## Output Modes

Match the output to what the user asks for:

**"Write me carousel hooks"** → Step 3 only. Generate 3-5 hooks with trigger words and pattern labels.

**"Script a carousel about X"** → Steps 3 + 4. Full 10-slide script with hooks, slide copy, micro-hooks, and CTA.

**"Create a complete carousel"** → Steps 3 + 4 + 5. Full script plus design specifications.

**"Plan a carousel campaign"** → Steps 3-6 for multiple carousels. Include weekly cadence, content type rotation, and hook style variety.

**"Review/optimize my carousel"** → Evaluate against the 10-slide architecture, hook rules, design non-negotiables, and fatal mistakes list from references. Provide specific fixes.

**"Build a lead gen carousel"** → Read `conversion-system.md`. Use B2B copywriting formulas, include Comment-to-DM CTA, specify keyword trigger, and provide DM sequence templates.

**"Set up carousel automation"** → Read `conversion-system.md`. Provide ManyChat setup steps, DM sequence, funnel math projections, and A/B testing framework.

**"Explain the psychology behind viral carousels"** → Read `psychology-engine.md`. Walk through System 1/2, cognitive biases, Information Gap Theory, PAS framework, and 4U Formula with carousel-specific applications.

---

## Content Type Templates

High-performing carousel content types to suggest when the user needs topic direction:

| Type | Structure | Best Hook Style |
|------|-----------|----------------|
| Educational Listicle | Each item = one slide | Promise or Step-by-Step |
| Step-by-Step Framework | Sequential instruction | Promise or List |
| Myth Busting | One myth per slide | Mistake or Shock/Stat |
| Before/After Transformation | Story arc across slides | Curiosity/Cliffhanger |
| Problem Cascade | Escalating consequences | Question or Mistake |
| Contrarian Take | Bold claim + proof | Shock/Stat or Question |
| Personal Story Arc | Vulnerability + proof + system | Curiosity/Cliffhanger |

---

## Seven Fatal Carousel Mistakes

Flag these when reviewing or creating:

1. **Too many words on slide 1.** Over 12 words kills performance.
2. **Medium contrast backgrounds.** Use extreme contrast only.
3. **No narrative arc.** Random slides without logical flow.
4. **Burying the value.** Slide 2 must be instant value, not setup.
5. **Every slide looks the same.** Alternate layouts within brand consistency.
6. **Weak or missing CTA.** No explicit CTA drops engagement 30-50%.
7. **Video slideshow instead of native Photo Mode on TikTok.**

---

## Quality Checklist (Self-Verification)

Before delivering any carousel output, verify:

- [ ] Hook is under 10 words and passes the Squint Test
- [ ] Hook uses a proven pattern from reference files
- [ ] 1-2 trigger words integrated naturally
- [ ] One point per slide, no exceptions
- [ ] Open loops between slides pull the viewer forward
- [ ] CTA is explicit and specific on the final slide
- [ ] Design specs respect platform safe zones
- [ ] Maximum 2 fonts, maximum 3 colors
- [ ] 60% white space / 40% content per slide
- [ ] Swipe indicator present on every slide
