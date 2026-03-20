---
name: logo-creator
description: Create top-tier professional logos through AI generation with brand strategy, design principles, and iterative refinement. Use when user wants to create a logo, brand mark, icon, favicon, mascot, emblem, wordmark, lettermark, or any visual brand identity element. Also trigger when user says "design a logo", "I need branding", "create an icon for", or "design something for my company/app/product". This skill combines brand strategy discovery, professional design evaluation criteria, and AI generation to produce logos that are not just visually appealing but strategically sound.
---

# Logo Creator Skill

Create professional, strategically-grounded logos through AI image generation and an iterative design process built on real brand strategy principles.

## Prerequisites

**Required API Keys (set in environment):**
- `GEMINI_API_KEY` — [Google AI Studio](https://aistudio.google.com/apikey)
- `REMOVE_BG_API_KEY` — [remove.bg](https://www.remove.bg/api)
- `RECRAFT_API_KEY` — [recraft.ai](https://www.recraft.ai/)

**Required Skills:**
- `nanobanana` — AI image generation (Gemini 3 Pro Image)

## File Output Location

```
.skill-archive/logo-creator/<yyyy-mm-dd-brandname>/
  logo-01.png ... logo-20.png
  logo-05-v1.png ... (iterations)
  logo-final-cropped.png
  logo-final-nobg.png
  logo-final.svg
  preview.html
  brand-brief.md
```

---

## THE 5 PRINCIPLES — Evaluate Every Logo Against These

Before generating or approving anything, these are the standards. A top-tier logo must satisfy all five.

1. **Simple** — Memorable at a glance. One clear idea. A child should be able to draw it from memory.
2. **Versatile** — Works at 16px favicon and 16-foot billboard. Works in black and white. Works on light and dark backgrounds.
3. **Timeless** — Avoids design trends. Will still look intentional in 10 years.
4. **Appropriate** — Matches the brand's industry, audience, and personality. A law firm and a gaming company should never have interchangeable logos.
5. **Distinctive** — Doesn't look like a competitor. Has a unique visual hook.

Use these to evaluate every batch. When presenting options, explicitly score each against these five.

---

## Workflow

### Step 1: Brand DNA Discovery

Do NOT skip this. The quality of the logo depends entirely on how well you understand the brand. Ask all of these before generating a single image.

**Required answers:**

**1. What does this company/product actually do?**
- One sentence. Force the user to be precise.

**2. Who is the target audience?**
- Age range, profession, lifestyle, sophistication level
- Example: "35-50 year old male real estate investors" vs "Gen Z female fitness enthusiasts"

**3. What is the brand's personality? (pick 3)**
```
Bold / Confident / Authoritative
Friendly / Approachable / Warm
Premium / Elegant / Luxurious
Innovative / Cutting-edge / Disruptive
Trustworthy / Reliable / Stable
Playful / Fun / Energetic
Minimal / Clean / Sophisticated
Gritty / Raw / Authentic
```

**4. Who are the top 3 competitors?**
- What do their logos look like?
- We need to differentiate, not blend in.

**5. What should the logo feel like?**
- Ask for 2-3 adjectives (e.g., "powerful and clean" or "warm and approachable")
- What should someone feel when they see it?

**6. What logos do you admire? (from any industry)**
- This reveals aesthetic preferences faster than asking about styles.

**7. Practical requirements:**
- Where will it primarily appear? (app icon, website, merchandise, signage, social media)
- Any colors already chosen or to avoid?
- Does it need to include the company name in the mark, or icon-only?

**Synthesize into a Brand Brief** before generating — save as `brand-brief.md` in the project folder. This becomes the prompt foundation.

---

### Step 2: Style Direction

Read [`references/styles.md`](./references/styles.md) for full style catalog with prompt patterns.

Based on brand DNA, recommend 2-3 styles that fit the brand's personality. Explain your reasoning. For example:

> "Given your premium positioning and B2B audience, I'd suggest starting with **Minimalist/Geometric** (clean authority) and **Lettermark** (professional legacy feel). I'd avoid mascots — they signal consumer/casual brands."

Do not ask the user to pick a style without giving them a recommendation first.

**Style → Brand Personality Mapping:**
| Style | Works Best For |
|-------|---------------|
| Minimalist/Flat | Tech, SaaS, professional services, premium brands |
| Lettermark/Monogram | Law, finance, luxury, personal brands, consulting |
| Mascot | Consumer apps, food, gaming, community, children |
| Abstract/Geometric | Tech, innovation, startups, forward-thinking brands |
| Pixel Art / 8-bit | Gaming, indie, developer tools, nostalgic tech |
| Emblem/Badge | Sports, craft/artisan, heritage, organizations |
| 3D/Isometric | Software products, platforms, modern SaaS |
| Wordmark | Media, fashion, consumer brands with short names |

---

### Step 3: Craft the Generation Prompts

This is where most AI logo attempts fail. Generic prompts produce generic logos.

**Prompt Architecture:**
```
[STYLE] + [SUBJECT/CONCEPT] + [BRAND PERSONALITY KEYWORDS] + [COLOR DIRECTIVE] + [FORMAT REQUIREMENTS] + [WHAT TO AVOID]
```

**Build 5 distinct prompt angles before batch generating:**
1. **Literal** — Direct visual representation of what the brand does
2. **Metaphorical** — Abstract concept that captures the brand's *feeling*
3. **Typographic** — Name or initials as the visual centerpiece
4. **Symbolic** — Universal symbol reinterpreted for this brand
5. **Character** — Mascot or anthropomorphic element (if appropriate)

**High-Performance Prompt Patterns:**

```
# Minimalist Tech
Minimalist {subject} icon, flat vector design, single {color}, geometric simplicity, 
clean negative space, professional and modern, white background, no gradients, 
no shadows, scalable to favicon size

# Premium/Luxury
Elegant {subject} logomark, refined line work, {color} on white, premium feel, 
geometric precision, balanced proportions, timeless not trendy, no decorative flourishes

# Bold/Confident
Strong {subject} mark, bold geometric shapes, {color} high contrast, 
powerful visual weight, confident design, clean edges, icon-style

# Mascot
{Character} mascot logo, {style} illustration, friendly and approachable, 
{colors}, simple enough to work as app icon, white background, 
flat or semi-flat style, no complex backgrounds

# Lettermark
Letter "{letters}" logo, custom typography, {style} design, 
{color} on white, unique letterform, professional, no clip art or stock elements
```

**Critical prompt constraints to always include:**
- `white background` — prevents the AI from adding complex backgrounds
- `no text` or `include brand name` — be explicit
- `scalable to favicon` — forces simplicity
- `vector-style` or `flat design` — prevents photo-realistic outputs
- `no gradients` — forces versatility (easier to reverse on dark BG)

---

### Step 4: Generate First Batch (20 Variations)

Use the 5 prompt angles. Generate 4 variations per angle.

```bash
# Single generation
python3 <nanobanana_skill_dir>/scripts/generate.py "{prompt}" \
  --ratio 1:1 -o .skill-archive/logo-creator/<date-name>/logo-01.png

# Batch (recommended)
python3 <nanobanana_skill_dir>/scripts/batch_generate.py "{prompt}" \
  -n 20 --ratio 1:1 -d .skill-archive/logo-creator/<date-name> -p logo
```

**Naming convention:**
- `logo-01.png` through `logo-20.png` — first batch
- `logo-05-v1.png`, `logo-05-v2.png` — iterations on #05
- `logo-final-cropped.png`, `logo-final-nobg.png`, `logo-final.svg` — finals

Copy the preview template and open:
```bash
cp <skill_dir>/templates/preview.html .skill-archive/logo-creator/<date-name>/preview.html
open .skill-archive/logo-creator/<date-name>/preview.html
```

---

### Step 5: Evaluate Batch Against the 5 Principles

Do not just present options. Evaluate them before asking for feedback.

For each notable option, score against the 5 principles:

```
Logo #07
✓ Simple — Clean single-mark concept, high memorability
✓ Versatile — Works in black and white, readable at 16px
✗ Timeless — Drop shadow feels dated (2018 SaaS)
✓ Appropriate — Premium feel matches B2B audience
✓ Distinctive — Strong visual hook, unlike competitors
Verdict: Strong candidate. Would improve by removing shadow.
```

Present your top 3-5 with this evaluation, then ask the user which direction resonates and why.

---

### Step 6: Iterate

Based on user selection and feedback:

1. Identify specifically what works: concept, shape, color, weight, style
2. Generate 10-20 focused variations on that direction
3. Use versioned naming: `logo-07-v1.png` through `logo-07-v15.png`
4. Update preview.html to reflect new count
5. Re-evaluate against 5 principles
6. Repeat until a clear winner emerges (typically 2-3 rounds)

**Iteration prompt refinement:**
- Remove what doesn't work: "no bevels", "no drop shadows", "simpler shapes"
- Amplify what does: "more geometric", "stronger weight", "more negative space"
- Reference the winner: "in the style of logo-07 but with more open letterforms"

---

### Step 7: Versatility Test (Before Final Approval)

Before the user locks in a final, verify the logo holds up in real use:

Ask them to mentally check (or use the preview HTML):
- [ ] Does it work in pure black on white?
- [ ] Does it work in white on black (dark mode)?
- [ ] Is it still recognizable at 32px?
- [ ] Does it read at a glance, or require study?
- [ ] Would it work on a t-shirt? A business card? A phone app?

If it fails any of these, note which and refine before finalizing.

---

### Step 8: Finalize and Export

Once the user approves a logo, run all three processing steps:

**8a. Crop to tight 1:1 square:**
```bash
python3 <skill_dir>/scripts/crop_logo.py {input.png} {logo-final-cropped.png}
```

**8b. Remove background (transparent PNG):**
```bash
python3 <skill_dir>/scripts/remove_bg.py {input.png} {logo-final-nobg.png}
```

**8c. Vectorize to SVG:**
```bash
python3 <skill_dir>/scripts/vectorize.py {input.png} {logo-final.svg}
```

---

### Step 9: Deliver Final Assets

```
## Final Logo Assets

| File | Description | Use Case |
|------|-------------|----------|
| logo-final.png | Original approved | Master file |
| logo-final-cropped.png | Tight crop, 1:1, white BG | Print, documents |
| logo-final-nobg.png | Transparent PNG | Web, overlays, merchandise |
| logo-final.svg | Scalable vector | Everything else |

All saved to: .skill-archive/logo-creator/<date-name>/
```

Also deliver a brief summary:
- What makes this logo work (which of the 5 principles it nails)
- Suggested primary color (hex) to lock in for brand consistency
- Recommended usage context (where it shines, any size/BG caveats)

---

## Quick Diagnostic: Common AI Logo Failures

When reviewing generated logos, reject any that show:

- **Noise / complexity** — Too much detail, won't scale down
- **Trendy effects** — Drop shadows, gradients, bevels, glows (unless deliberately retro)
- **Random text hallucinations** — AI often adds garbled text; reject these
- **Symmetry breaks** — Lopsided marks unless intentional
- **Generic clip-art feel** — Stock icon energy; push for more unique interpretations
- **Background contamination** — Complex backgrounds, textures, gradients behind the mark

---

## References

- [`references/styles.md`](./references/styles.md) — Full style catalog with 10 categories and prompt patterns. Read before recommending styles.
- [`examples/opc-logo-creation.md`](./examples/opc-logo-creation.md) — Complete worked example conversation.
