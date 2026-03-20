---
name: gemini-ai-image-prompting--unshakable-brand
description: Master skill for generating Gemini Nano Banana Pro 2 image prompts for The Unshakable Investor brand. Use when Nick requests any AI image generation — Facebook ads, event banners, book covers, carousels, Stories, lead magnet covers, or any brand visual. Covers the full SLCSQ framework, brand color rules, Toby Potter photo library, per-platform aspect ratios, negative prompt library, template system by use case, hybrid workflow, and iteration protocol. All rules are non-negotiable and applied automatically.
---

# GEMINI AI IMAGE PROMPTING — MASTER PLAYBOOK
## The Unshakable Investor Brand
**Version 2.0 | March 2026 | Compiled from all production sessions, iterations, and failure logs**

> **Primary reader:** Claude (AI assistant). This document governs how Claude generates Gemini prompts for The Unshakable Investor brand. Apply every rule in this document automatically. Do not wait for the user to specify brand rules. Enforce them on every prompt output.

> **Platform:** Gemini Nano Banana Pro 2 via web interface only. No API. No code. Prompts are typed or pasted directly into Gemini's web UI with reference photos attached when needed.

---

## TABLE OF CONTENTS

1. [Model Selection](#1-model-selection)
2. [Core Prompt Philosophy](#2-core-prompt-philosophy)
3. [Brand Rules — Non-Negotiable](#3-brand-rules--non-negotiable)
4. [Color System](#4-color-system)
5. [The SLCSQ Prompt Framework](#5-the-slcsq-prompt-framework)
6. [Toby Potter Photo Library](#6-toby-potter-photo-library)
7. [Toby Potter Standard Portrait Blocks](#7-toby-potter-standard-portrait-blocks)
8. [Text in Images](#8-text-in-images)
9. [Aspect Ratios and Safe Zones](#9-aspect-ratios-and-safe-zones)
10. [Negative Prompt Master Library](#10-negative-prompt-master-library)
11. [Style Reference Library](#11-style-reference-library)
12. [Prompt Templates by Use Case](#12-prompt-templates-by-use-case)
    - 12A. Facebook Feed Ad (1:1 and 4:5)
    - 12B. Stories and Reels (9:16)
    - 12C. Event Banner / Wide Format (2:1)
    - 12D. Lead Magnet Book Cover System (3:4)
    - 12E. Carousel Slides (4:5)
    - 12F. Webinar / Landing Page Hero (16:9)
13. [The Hybrid Workflow](#13-the-hybrid-workflow)
14. [Iteration Protocol](#14-iteration-protocol)
15. [Common Failure Patterns and Fixes](#15-common-failure-patterns-and-fixes)
16. [Pre-Generate Checklist](#16-pre-generate-checklist)

---

## 1. MODEL SELECTION

There is one model for this brand. Use nothing else for final output.

| Model | Web UI Name | Use |
|-------|-------------|-----|
| Gemini 3 Pro Image | **Nano Banana Pro 2** | ALL final ad creatives, covers, event banners, carousels |
| Gemini 2.5 Flash Image | Nano Banana | Quick concept drafts and speed tests only |

**Rule:** Always default to Nano Banana Pro 2. Only drop to Nano Banana when Nick explicitly needs a fast concept draft and quality does not matter yet.

Nano Banana Pro 2 advantages over other models:
- Handles text rendering better than any other available model
- Character consistency across multiple images using the same reference photo
- Accepts up to 14 reference images simultaneously (6 objects, 5 people, 3 style references)
- 4K output resolution
- Multi-turn consistency through thought signatures (web UI handles this automatically in conversation)

---

## 2. CORE PROMPT PHILOSOPHY

### Think Like an Art Director, Not a Spec Sheet

The single most impactful lesson from all production sessions: Gemini responds to creative direction, not technical specifications.

**What fails every time:**
```
Background: #050505. Subject at center. Text "BLUEPRINT" in 105px 
Montserrat Black, gold gradient #FFD700 to #FFA500 to #FF4500. 
Shadow: 0 0 40px rgba(212,175,55,0.5). Top margin: 80px.
```

**What works:**
```
You are a world-class graphic designer at Pentagram. Design an event 
banner that belongs on the homepage of a Fortune 500 investor summit. 
Not an internet marketing ad. A premium, restrained, editorially-designed 
announcement.
```

Gemini interprets design philosophy and cinematic intent far more accurately than CSS properties and pixel coordinates. Describe the FEELING, the REFERENCE POINTS, and especially the RESTRAINT. Let the model make design decisions inside those constraints.

### The Subtraction Principle

Every prompt iteration that improved output REMOVED elements. Every iteration that made output worse ADDED elements. Premium design is defined by what is NOT there.

**Rule:** If you can remove an element without losing the core message, remove it. Fewer elements always produce cleaner, more professional output.

### Hierarchy of Prompt Effectiveness (Ranked Most to Least Effective)

1. Design philosophy and reference brands ("Think Bloomberg meets TED keynote")
2. Spatial relationships and breathing room ("Generous space between every element")
3. Mood and atmosphere descriptions ("Dramatic Rembrandt lighting, cinematic depth")
4. Color discipline stated as rules ("Only three colors exist: black, white, and gold")
5. Specific text content (exact words for headlines, spelled out in quotes)
6. Negative prompts (what to exclude)
7. Technical specs like hex codes — least effective alone, use as parenthetical reinforcement only

### The Three-Color Discipline

Default palette for every prompt: obsidian black (#050505), white (#FFFFFF), and one accent — almost always gold. State this as a rule inside the prompt: "Only three colors exist in this image: black, white, and gold." A fourth color can appear at less than 10% of the composition only.

---

## 3. BRAND RULES — NON-NEGOTIABLE

These rules apply to every prompt Claude generates for this brand. They are not suggestions. Apply them automatically without being asked.

**Rule 1 — Background is obsidian, never navy.**
Describe backgrounds as "pure black," "obsidian black," or "near-solid black." Never say "dark blue," "navy," "midnight blue," or simply "dark" without qualification. Include "No blue tones. No navy." in the prompt body AND "navy blue, blue tones" in the negative prompt. Both are required. Gemini defaults to blue-tinted dark tones if not explicitly corrected on both fronts.

**Rule 2 — Gold is never flat unless context demands it.**
Two treatments exist:
- Energetic/advertising context: "warm gold gradient flowing from bright gold through amber to deep fire orange" (maps to #FFD700 → #FFA500 → #FF4500)
- Premium/editorial/PDF context: "flat muted gold matching a luxury watch bezel" (maps to #D4AF37)
Never say just "gold" without specifying which treatment.

**Rule 3 — No fire unless explicitly requested.**
Gemini associates this brand with fire and will add flames unprompted. Include "no fire, no flames, no embers" in both the prompt body and the negative prompt on every generation unless Nick specifically asks for fire elements.

**Rule 4 — No cool tones anywhere.**
The brand palette is warm: black, gold, amber, white. Include "No cool tones anywhere. Warm palette only." in every prompt. Add "teal, cyan, cool tones, cool lighting" to every negative prompt.

**Rule 5 — No dashes in any text on any image.**
No em dashes, en dashes, or hyphens used as punctuation in any text element baked into a prompt. Restructure the sentence instead. This is a brand-wide rule that extends into imagery.

**Rule 6 — Text must be spelled out exactly, word for word.**
If text appears in the image, write every single word in quotation marks inside the prompt. Gemini hallucinates text content when given vague instructions like "add a headline" or "include some text." Spell it out completely.

**Rule 7 — Aspect ratio declared in the first line.**
Every prompt must open with the aspect ratio and format stated explicitly. Never let Gemini choose. See Section 9 for ratio logic by platform.

**Rule 8 — Describe scenes, not blueprints.**
Natural spatial language only. Use "centered," "upper third," "left portion," "below his shoulders," "generous space above." Never use x/y pixel coordinates. Gemini does not process coordinate values accurately.

**Rule 9 — Face accuracy requires triple reinforcement when Toby is in the image.**
See Section 7 for the exact triple-reinforcement template. This is required on every portrait prompt — not optional.

**Rule 10 — Never use generic coaching language in any text elements.**
Text in images follows the same brand voice rules as copy. Banned phrases: "unlock your potential," "transform your life," "take it to the next level," "crush it," "level up," "game changer." Use specific, proof-driven language.

---

## 4. COLOR SYSTEM

### How to Reference Colors in Gemini Prompts

Gemini does not precisely interpret hex codes as primary instruction. Use descriptive language as the primary reference and hex codes as parenthetical reinforcement.

| Brand Element | Prompt Language | Hex Code |
|---------------|----------------|----------|
| Backgrounds | "Pure black," "obsidian black," "near-solid black" | #050505 or #0B0B0F |
| Cards and containers | "Dark charcoal panel," "near-black card" | #1A1A1A |
| Gold gradient (ads) | "Warm gold gradient from bright gold through amber to deep fire orange" | #FFD700 → #FFA500 → #FF4500 |
| Gold flat (editorial) | "Flat muted gold matching a luxury watch bezel," "solid antique gold" | #D4AF37 |
| White text | "Bright white," "crisp white," "bold white" | #FFFFFF |
| Muted supporting text | "Muted gray," "light gray" | #999999 or #BBBBBB |

### When to Use Gradient vs. Flat Gold

| Context | Gold Treatment | Reason |
|---------|---------------|--------|
| Facebook ad creatives | Gradient (#FFD700 → #FF4500) | Catches attention in the feed, energy signal |
| Instagram Stories / Reels | Gradient | Full-screen context, motion energy |
| Eventbrite banners | Flat #D4AF37 | Reads premium and editorial, not promotional |
| PDF ebooks and lead magnets | Flat #D4AF37 | Document aesthetic, print quality feel |
| Social carousel text highlights | Flat brush stroke | Editorial, not flashy |
| CTA buttons | Flat for premium events, gradient for urgency campaigns | Match the overall tone of the piece |

### Critical Color Negatives (Always Include)

```
navy blue, blue tones, teal, cyan, cool tones, cool lighting, cool rim light, 
blue ambient light, navy (#1A1A2E), blue glow
```

---

## 5. THE SLCSQ PROMPT FRAMEWORK

Every prompt for this brand uses the SLCSQ structure. This is not optional formatting; it is how Gemini receives and interprets creative briefs. Use it on every prompt.

The five sections are: **Scene, Lighting, Composition, Style, Quality.**

### [SCENE]
Describe what exists in the image. Subject, background, atmosphere, props. Lead with natural language descriptions. Include hex codes only as parenthetical reinforcement after the natural language description. State color rules here ("No blue tones. Warm palette only.").

### [LIGHTING]
Where light comes from. Use real photography terminology — Gemini understands it accurately. Specify key light direction, rim light color, fill ratio, and ambient mood.

**Photography lighting terms Gemini responds to:**
- Rembrandt lighting: Triangle of light on cheek, dramatic and authoritative
- Butterfly lighting: Shadow under nose, glamorous and polished
- Split lighting: Half face lit, intense and dramatic
- Loop lighting: Small shadow from nose, flattering and approachable
- Broad lighting: Lit side toward camera, open and confident
- Short lighting: Shadow side toward camera, mysterious and cinematic

For this brand: warm gold rim light along the right shoulder and hair edge is the default. Always specify unless Nick requests something different.

### [COMPOSITION]
Where everything sits spatially. Define clear zones for text overlay using natural spatial language. Never use x/y coordinates.

**Standard spatial language:**
- "Centered in the lower half of the frame"
- "Upper 40% is clean, dark, uncluttered space for headline text"
- "Left third of the frame with clear space on the right"
- "Generous breathing room between the top of his head and the top of the frame"
- "Lower 20% reserved for a full-width text strip"

### [STYLE]
What it feels like. Reference real-world design benchmarks to calibrate Gemini's output register. Always include an anti-reference.

### [QUALITY]
How sharp and detailed. Camera simulation language calibrates output fidelity even in the web interface.

**Standard quality block:**
```
8K hyperdetailed. Canon EOS R5, 85mm f/1.4. Natural skin texture, 
subtle pores and lines visible. Professional color grading. Sharp focus 
on eyes. Magazine cover quality.
```

### Full SLCSQ Example

```
Square image, exactly 1:1 aspect ratio. Photorealistic, cinematic.

[SCENE]
Professional advertisement. Obsidian black background, pure black 
(#050505), no blue tones. Warm atmospheric amber glow at center behind 
the subject. No fire, no flames.

[LIGHTING]
Key light from upper left. Warm golden rim light along right shoulder 
and hair edge creating strong separation from background. Soft amber 
atmospheric glow behind subject. No cool tones in lighting. Warm 
palette only.

[COMPOSITION]
Subject centered in the lower half. The entire upper 40% is clean, 
dark, and uncluttered — suitable for headline text overlay. No 
elements above his head. Generous breathing room between the top of 
his head and the top of the frame.

[STYLE]
Bloomberg event invitation meets Netflix documentary title card. 
Premium, cinematic, sophisticated. Not a Canva template. Not a 
motivational speaker flyer. Not an internet marketing ad.

[QUALITY]
8K hyperdetailed. Canon EOS R5, 85mm f/1.4. Natural skin texture 
preserved, subtle pores and lines visible. Professional color grading. 
Sharp focus on eyes. Magazine cover quality.

Only three colors exist in this image: black, white, and gold.
```

---

## 6. TOBY POTTER PHOTO LIBRARY

When generating any image that includes Toby, always attach a reference photo from this library. Tell the user which file to attach. Never rely on a text description alone.

The following photos are available. Each has a specific highest-value use case.

---

### Photo 1 — `toby_black_suit.png`
**Best for: Authority ads, book covers, event banners, any premium ad creative**

What the photo shows: Toby from mid-chest up, looking directly at the camera with a warm, confident smile. Dark charcoal pinstripe suit jacket. Light blue open-collar dress shirt, no tie. Gold coin lapel pin on the left lapel. Gold chain necklace visible. Silver-white hair styled back. Gray beard, full and well-groomed. Background is pure black. Clean professional lighting. This is a pre-cut photo with a clean black background, which makes it ideal for compositing into any AI-generated scene.

**Why it's the primary reference:** The black background eliminates edge conflicts with new backgrounds. The direct camera smile reads authority with warmth — not stiff. The suit and lapel pin signal the credentials without being formal.

---

### Photo 2 — `Toby.png`
**Best for: Speaking content, dynamic teaching moments, energy-forward creatives**

What the photo shows: Toby from mid-chest up, caught mid-gesture, right hand extended toward the camera with energy. Blue blazer. Light blue shirt with conference lanyard visible. Intense, focused expression — not smiling, fully engaged in making a point. Silver-white hair. Gray beard. Background is pure black.

**Why to use it:** The gesture and expression communicate teaching authority. Use when the image needs energy, urgency, or a moment of direct challenge to the viewer.

---

### Photo 3 — `New_toby_Picture.png`
**Best for: Profile compositions, speaker authority, strength framing**

What the photo shows: Toby in profile, facing left. Blue blazer. Right fist clenched at chest height in a focused, controlled gesture. Intense expression showing concentration. Silver-white hair. Gray beard. Background is pure black.

**Why to use it:** The side profile with clenched fist communicates focused power without aggression. Strong for event promotion where strength and clarity of thought are the message.

---

### Photo 4 — `Toby-Potter-_Magazine-_dallas_herald-_Leadership-791x1024.png`
**Best for: Face accuracy reference, editorial tone, premium credibility contexts**

What the photo shows: Dallas Herald magazine cover, October 2025. Toby from chest up, warm confident smile, dark pinstripe suit, purple/lavender open-collar shirt. Cross necklace visible. Face is well-lit from the front with warm lighting. Hair slightly tousled with more texture visible than other photos. Premium editorial framing.

**Why to use it:** The front-facing well-lit quality makes this the clearest face reference available. When Gemini is struggling with face accuracy, attach this alongside the primary photo. Also useful for any editorial or credibility context where "published, respected figure" is the message.

---

### Photo 5 — `IMG_6920.jpg`
**Best for: Candid authority, thoughtful expert, approachable leadership**

What the photo shows: Toby seated, casually dressed in a pink open-collar shirt and jeans. Hands clasped together in front of him, rings and layered bracelets visible. Looking slightly upward with a thoughtful, serious expression. Casual auditorium setting with dark curtain background. Not a promotional photo — this is a real moment.

**Why to use it:** Use when the image needs to feel earned, unposed, and authentic. The casual wardrobe and candid posture make this valuable for content targeting skeptical audiences who distrust polished guru imagery. Not for premium event promotion.

---

### Photo 6 — `IMG_6857.jpg`
**Best for: Community contexts, speaking at scale, accessible authority**

What the photo shows: A selfie taken by Toby at the front of a large auditorium filled with hundreds of seated people. Toby is in the foreground close to the camera, wearing a navy blazer and cream/tan open-collar shirt with a gold crown lapel pin. Warm smile. The audience behind him demonstrates scale. The environment is a school auditorium with institutional lighting.

**Why to use it:** The scale of audience creates social proof. For IGNITE community content or any creative where demonstrated reach and trust at scale matters. The organic setting makes it feel real and not staged.

---

### Photo 7 — `Toby-Potter__Speaking___11_.JPG`
**Best for: Stage authority, full-body speaker shots, event promotion with energy**

What the photo shows: Full body shot of Toby on a stage in front of a large branded LED screen showing "THE UNSHAKABLE INVESTOR." He is wearing a blue blazer and jeans with boots. Holding a microphone in his right hand, left hand pointing upward. The Unshakable Investor branding and logo are visible on the screen behind him. He is elevated on the stage, looking upward with energy.

**Why to use it:** The only available full-body, on-stage photo with visible brand elements. Use when the event context or stage presence is part of the message. The Unshakable Investor screen behind him adds brand credibility. Useful for event promotion where the live event scale matters.

---

### Photo Usage Protocol

When building a prompt that includes Toby, Claude must:
1. Identify which photo is best suited for the creative goal using the descriptions above
2. Tell the user which file to attach to the Gemini prompt before generating
3. Include face accuracy instructions in THREE places in the prompt (see Section 7)
4. Default to `toby_black_suit.png` when no specific reason favors another photo

**Example instruction to user:** "Attach `toby_black_suit.png` to this Gemini prompt before generating. That's the dark suit clean background version — it gives Gemini the strongest base for compositing him into the new scene."

---

## 7. TOBY POTTER STANDARD PORTRAIT BLOCKS

These are pre-written, tested description blocks. Copy and paste them into prompts verbatim. Do not rewrite from scratch each time.

### Face Accuracy Block — TOP (paste at the very beginning of the prompt)
```
CRITICAL INSTRUCTION: The subject's face MUST exactly match the attached 
reference photo. Do not approximate, reimagine, smooth, age, de-age, or 
stylize any facial features. Copy the face identically. This overrides 
all other instructions.
```

### Face Accuracy Block — BOTTOM (paste at the very end of the prompt, before the negative prompt)
```
FINAL CHECK: The face must be an identical match to the attached reference 
photo. This is the single most important instruction in this prompt and 
overrides everything else.
```

### Color Portrait Block (Primary — Default for Most Ads)
```
A distinguished man in his late 50s. Silver-white hair styled neatly and 
swept back. Full gray beard, well-groomed and trimmed. Dark charcoal 
pinstripe suit jacket. Crisp light blue open-collar dress shirt, no tie. 
Gold coin lapel pin on the left lapel. Gold chain necklace visible at the 
collar. Warm confident smile facing the camera directly. Use the attached 
reference photo for his exact likeness.
```
*Attach: `toby_black_suit.png`*

### B&W Speaker Block (Secondary — For Energy and Teaching Contexts)
```
Black and white with a subtle warm sepia tone. Same man holding a 
microphone, speaking with energy and conviction. Dynamic three-quarter 
pose, slight lean forward. Slightly smaller than the primary color figure. 
Left edge dissolves softly into the dark background at approximately 60% 
opacity. Positioned slightly behind and to the side of the primary figure. 
Adds kinetic energy without competing with the main subject.
```
*Attach: `Toby.png` or `Toby-Potter__Speaking___11_.JPG`*

### Dynamic Visionary Block (Atmospheric Layer — Background Element Only)
```
Black and white, warm tone, approximately 35 to 40% opacity. Dynamic and 
passionate. One hand raised in a powerful gesture, leaning forward with 
intense expression. Blending almost entirely into the dark background. 
Much smaller than the primary figure. An atmospheric element, not a 
competing subject. Dissolves into the background from the edges.
```
*Attach: `New_toby_Picture.png` for the side-profile energy*

### Triple Composite Block (All Three Versions in One Image)
```
Three versions of the same man at different scales and treatments:

RIGHT SIDE, DOMINANT: Full color. [Color Portrait Block above]. Cropped 
from mid-chest up. This is the primary, largest figure. Sharp and 
prominent.

CENTER-LEFT, SECONDARY: Black and white, warm sepia, approximately 70% 
opacity. Same man at the microphone, speaking with energy. Slightly 
smaller than the color version. Three-quarter pose facing right. They 
overlap slightly at the shoulder. Adds depth without competing.

FAR LEFT, ATMOSPHERIC: Black and white, warm tone, approximately 35% 
opacity. Same man, dynamic gesture, passionate expression. Smallest of 
the three. Dissolves into the background. Atmospheric only.

All three versions share the same background. Their lighting feels 
unified — they all exist in the same cinematic space. No visible edges 
or pasted-in quality.
```

---

## 8. TEXT IN IMAGES

### Gemini Text Rendering Reality

Do not assume Gemini will render text perfectly. Know these reliability rates before deciding whether to include text in the prompt or route to the hybrid workflow.

| Text Type | Reliability | Recommendation |
|-----------|-------------|----------------|
| 1 to 3 word headlines | 85% accurate | Include in prompt |
| 4 to 8 word headlines | 60% accurate | Include, verify output |
| Full sentences | 30% accurate | Skip. Add in Canva instead. |
| Small body text or labels | 10% accurate | Never include |
| Button text | 70% accurate | Include, verify |
| Multi-line stacked text | 40% accurate | Use as layout guide only, rebuild in Canva |

### How to Specify Text in the Prompt

When including text in a Gemini prompt, spell out every word in quotation marks. Include a size hierarchy so Gemini understands relative importance.

**Example text hierarchy block:**
```
TEXT CONTENT AND SIZE HIERARCHY:
1st largest (dominant visual anchor): "BLUEPRINT"
2nd largest: "March 28 | 9:00 AM CST | Live Virtual"
3rd largest: "The 5-Step System for Business Owners Doing $500K+"
4th largest: "Register Free"
5th largest: "Hosted by Toby Potter | Global Integrity Finance"

The word "BLUEPRINT" is the visual anchor of the entire design. 
Everything else is secondary to it.
```

### The Hybrid Decision Rule

Route to the hybrid workflow (Gemini for visual, Canva for text) when ANY of the following are true:
- More than 3 text elements in the image
- Text must overlap a complex background or a person's body
- Precise brand typography is required (Montserrat, Inter)
- The image includes a CTA bar, credentials line, or event date/time
- Carousel slides that must have identical text styling across all slides
- Any text with specific line breaks that must be preserved

When routing to hybrid, add this to the prompt:
```
No text in the image. Visual only. Clean dark space in the [upper third / 
lower strip / left column] suitable for text to be added later in 
post-production.
```

Keep Gemini-rendered text only for: 1 to 2 large words maximum ("BLUEPRINT," "FREE," "LIVE"), text on clean uncluttered dark areas, and draft concepts where speed matters more than perfection.

---

## 9. ASPECT RATIOS AND SAFE ZONES

### Ratio Selection by Platform

Always declare the aspect ratio in the FIRST LINE of the prompt. Never let Gemini choose.

| Platform/Use | Ratio | First Line of Prompt |
|--------------|-------|---------------------|
| Facebook Feed ad (default) | 1:1 | "Square image, exactly 1:1 aspect ratio." |
| Instagram Feed (more screen space) | 4:5 | "Vertical portrait image, exactly 4:5 aspect ratio." |
| Stories and Reels | 9:16 | "Vertical full-screen image, exactly 9:16 aspect ratio." |
| Eventbrite banner / event cover | 2:1 | "Wide horizontal banner, exactly 2:1 aspect ratio." |
| Webinar hero / YouTube thumbnail | 16:9 | "Horizontal image, exactly 16:9 aspect ratio." |
| Ebook cover / lead magnet cover | 3:4 | "Vertical cover image, exactly 3:4 aspect ratio." |
| Carousel single slide | 4:5 | "Vertical portrait image, exactly 4:5 aspect ratio." |

### Safe Zone Rules (Embed These in the Prompt When Relevant)

**9:16 Stories and Reels:**
Platform UI covers the top 15% (profile/username bar) and bottom 15% (swipe-up or CTA overlay). The safe content zone is the middle 70% of the vertical frame.
Embed in prompt: "Keep all important visual elements in the center 70% of the vertical frame. Top 15% and bottom 15% will be covered by platform UI overlays."

**2:1 and 16:9 Wide Banners:**
Many platforms crop wide images to a center square for preview thumbnails (Eventbrite, Facebook Event covers, some Instagram views). The critical content rule: all faces, headlines, and CTAs must fit inside the center square. The left and right atmospheric edges can be cropped without losing the message.
Embed in prompt: "All critical content (subject's face, headline, CTA) must fit inside the center square of this wide image. Left and right edges are atmospheric-only visual space that may be cropped on some platforms."

**4:5 Feed Portrait:**
Standard content margins apply. Top and bottom 90px are typically safe but keep headline text at least 120px from the top edge.
Embed in prompt: "Maintain clear margins of at least 10% at top and bottom. All text zones sit within the inner 80% of the vertical space."

---

## 10. NEGATIVE PROMPT MASTER LIBRARY

Copy the entire universal block on every prompt. Then append the situation-specific additions based on what the image contains.

### Universal Block (Always Include on Every Prompt)
```
navy blue, blue tones, teal, cyan, cool tones, cool lighting, fire, flames, 
embers, floating particles, lens flare, bokeh circles, neon, sparkles, 
cartoon, illustration, clip art, 3D render, template look, Canva aesthetic, 
stock photo feel, busy, cluttered, overlapping text, text on face, blurry 
text, warped letters, watermark, logo, signature, bright background, white 
background, plastic skin, waxy face, overly smooth, AI-generated look
```

### Add for Portrait Images (Any Image with Toby or Any Person)
```
distorted face, wrong face, altered features, smoothed skin, de-aged face, 
different person, asymmetric face, extra fingers, deformed hands, extra 
limbs, uncanny valley
```

### Add for Typography-Heavy Images
```
misspelled words, illegible text, ghost text, mirrored text, duplicate text, 
background text, merged letters, missing letters, garbled text, wrong spelling
```

### Add for Premium and Editorial Tone
```
promotional, cheesy, cheap, amateur, gradient button, orange text, star shape, 
diamond shape, corner decorations, decorative elements, internet marketing
```

### Add for Dark Background Images (Any Image with Obsidian/Near-Black Background)
```
navy (#1A1A2E), blue glow, cool rim light, blue ambient light, daytime, 
bright sky, overexposed, flat lighting
```

### Add for City Skyline Backgrounds
```
daytime city, bright sky, blue sky, daylight, overexposed cityscape, 
flat city lighting
```

### Add for Event Creatives (If Fire is NOT Requested)
```
fire, flames, burning, embers, sparks, explosion, fireworks
```

### Add When Output Keeps Coming Out "Cheesy" or "Internet Marketing"
```
promotional, internet marketing ad, sales funnel, webinar ad, Facebook ad 
template, motivational poster, guru marketing, inspirational quote, stock 
business photo, royalty free image
```

### Add for Star/Diamond Artifacts (Known Gemini Default)
```
star shape, diamond shape, star burst, corner decorations, decorative 
geometric shapes, ornamental borders
```

---

## 11. STYLE REFERENCE LIBRARY

Match the user's intent to the right style reference. These go in the [STYLE] section of the SLCSQ framework. Always include at least one anti-reference.

| Intent | Style Reference Language |
|--------|-------------------------|
| Authority and credibility | "Fortune 500 executive portrait. Bloomberg Businessweek cover." |
| Premium event promotion | "TED stage announcement meets Netflix documentary title card." |
| Premium editorial | "Pentagram-designed annual report. Monocle magazine feature." |
| Urgency and scarcity | "Premium direct response. Luxury casino meets limited-edition drop." |
| Lead magnet and ebook promo | "Apple product announcement. Premium SaaS launch." |
| Testimonial and social proof | "WSJ feature profile. Editorial documentary still." |
| Community and belonging | "WeWork brand campaign meets Soho House membership invitation." |
| Speaker and stage content | "TED main stage program guide. Bloomberg Summit speaker roster." |
| Educational content | "Harvard Business Review feature. McKinsey report cover." |

**Always include one anti-reference.** Choose the most relevant:
- "This is NOT a Facebook ad template."
- "NOT a Canva design."
- "NOT a motivational speaker flyer."
- "NOT an internet marketing ad."
- "NOT a stock photo composite."

---

## 12. PROMPT TEMPLATES BY USE CASE

### 12A. Facebook Feed Ad — Authority Figure (1:1 and 4:5)

Use for: webinar promotion, strategy call booking, program awareness. Toby centered, city skyline or clean background, text space above.

**Tell user:** Attach `toby_black_suit.png`

```
[ASPECT RATIO LINE — use "Square image, exactly 1:1 aspect ratio." 
or "Vertical portrait image, exactly 4:5 aspect ratio."]
Photorealistic. Cinematic.

CRITICAL INSTRUCTION: The subject's face MUST exactly match the attached 
reference photo. Do not approximate, reimagine, smooth, age, or stylize 
any facial features. This overrides all other instructions.

[SCENE]
Professional advertisement. A distinguished man in his late 50s. 
Silver-white hair styled neatly and swept back. Full gray beard, 
well-groomed and trimmed. Dark charcoal pinstripe suit jacket. Crisp 
light blue open-collar dress shirt, no tie. Gold coin lapel pin on left 
lapel. Warm confident smile facing the camera. Use the attached reference 
photo for his exact likeness.

He is centered, cropped from mid-chest up, positioned in the lower half 
of the frame.

Background: dramatic darkened aerial city skyline at night with warm amber 
and gold city lights. Heavily darkened with an obsidian black (#050505) 
overlay. No blue tones. No navy. No cool colors. Warm palette only.

[LIGHTING]
Key light from upper left. Warm golden rim light along right shoulder and 
hair edges creating strong separation from the background. Soft amber 
atmospheric glow behind his head. Face is the sharpest, best-lit element. 
Natural skin texture preserved.

[COMPOSITION]
Subject centered in the lower half. The entire upper 40% of the frame is 
clean, dark, and uncluttered space suitable for headline text overlay. No 
elements above his head. Generous breathing room between the top of his 
head and the top of the frame.

[STYLE]
Bloomberg event invitation meets Netflix documentary title card. Premium, 
cinematic, sophisticated. Not a Canva template. Not a motivational speaker 
flyer. Not an internet marketing ad.

[QUALITY]
8K hyperdetailed. Canon EOS R5, 85mm f/1.4. Natural skin texture, subtle 
pores and lines visible. Professional color grading. Sharp focus on eyes. 
Magazine cover quality.

Only three colors exist in this image: black, white, and gold.

FINAL CHECK: Face must be identical to the attached reference photo. This 
overrides all other instructions.

Avoid the following: [PASTE UNIVERSAL NEGATIVE + PORTRAIT ADDITIONS + DARK 
BACKGROUND ADDITIONS + CITY SKYLINE ADDITIONS]
```

---

### 12B. Stories and Reels (9:16)

Use for: Instagram Stories ads, Facebook Stories, Reels placements. Subject fills lower two-thirds, clean dark space in upper third.

**Tell user:** Attach `toby_black_suit.png`

```
Vertical full-screen image, exactly 9:16 aspect ratio. Photorealistic.

CRITICAL INSTRUCTION: The subject's face MUST exactly match the attached 
reference photo. Do not approximate, reimagine, smooth, or stylize any 
facial features. This overrides all other instructions.

[SCENE]
A distinguished man in his late 50s. [Color Portrait Block from Section 7]. 
Cropped from waist up, filling the lower two-thirds of the vertical frame. 
Looking directly at the camera with warm confident expression.

Background: deep obsidian black (#050505) with warm amber atmospheric glow 
behind the subject. No fire, no flames. No blue tones. Warm palette only.

Upper third of the frame is clean, dark, uncluttered space for text overlay.
Keep all important elements in the center 70% of the vertical frame. Top 
15% and bottom 15% will be covered by platform UI overlays.

[LIGHTING]
Key light from upper left. Warm golden rim light along right shoulder and 
hair edges. Face well-lit. No cool tones in lighting.

[COMPOSITION]
Subject in the lower two-thirds. Upper third completely clear and dark. 
Lower edge fades gently into the background. No crowding.

[STYLE]
Netflix documentary feature. Premium event announcement. Not a Facebook 
ad. Not a Canva template.

[QUALITY]
8K hyperdetailed. 85mm f/1.4 portrait quality. Sharp face. Natural skin 
texture. Professional color grading.

Only three colors: black, white, and gold.

FINAL CHECK: Face identical to reference photo. This overrides everything.

Avoid the following: [UNIVERSAL NEGATIVE + PORTRAIT + DARK BACKGROUND]
```

---

### 12C. Event Banner — Wide Format (2:1)

Use for: Eventbrite banners, Facebook Event covers, webinar headers. Center-square rule is critical here.

**Tell user:** Attach `toby_black_suit.png`

```
Wide horizontal banner, exactly 2:1 aspect ratio. Photorealistic. Premium.

CRITICAL INSTRUCTION: Subject's face must exactly match the attached 
reference photo. Do not approximate or alter any facial features.

[SCENE]
Split composition. 

LEFT HALF: Text and typographic zone. Dark obsidian black (#050505) 
background. Clean and spacious. [Insert specific text content here with 
exact words spelled out.]

RIGHT HALF: Subject portrait. [Color Portrait Block from Section 7]. 
Cropped from mid-chest up, positioned in the right half of the frame. 
Warm city skyline or pure obsidian background behind him. Warm amber 
glow behind head. No blue tones.

All critical content (subject face, headline, event details) is 
concentrated in the center square of this wide image. Left and right 
outer edges are atmospheric and may be cropped on some platforms.

[LIGHTING]
Key light from upper center-left. Warm golden rim light on right shoulder 
and hair. Clean separation from background.

[COMPOSITION]
Everything important lives in the center 50% of the horizontal width. 
Edges add atmosphere only. Generous spacing between all text elements.
Breathing room. Not crowded.

[STYLE]
Fortune 500 investor summit announcement. Bloomberg event cover. Not 
internet marketing. Not a Canva design.

[QUALITY]
8K hyperdetailed. Magazine print quality. Professional color grading.

Only three colors: black, white, and gold.

FINAL CHECK: Face identical to reference. Overrides everything.

Avoid the following: [UNIVERSAL NEGATIVE + PORTRAIT + DARK BACKGROUND + 
TYPOGRAPHY if text is included]
```

---

### 12D. Lead Magnet Book Cover System (3:4)

This is a full multi-phase methodology, not a single template. For every lead magnet cover, follow all phases in sequence.

#### Phase 1: Extract Three Things from the Lead Magnet

Before writing a single line of prompt, read the lead magnet and identify:

**1. The Transformation** — not the topic. The before and after shift in one sentence.
Ask: "What does the reader have after finishing this that they didn't have before?"
This becomes the subtitle or core messaging on the cover.

**2. The Audience Signal** — words that make the target reader recognize themselves.
Ask: "What language would make the right person stop scrolling because they see themselves?"
Use concrete demographics: revenue, deal volume, industry, geography, role. Never use psychographics ("overwhelmed," "burned out"). The audience signal goes at the very top of the cover in small text. It is the first thing read and the primary filter.

**3. The Sharpest Proof Point** — one specific number or claim that creates a pattern interrupt.
Ask: "What single data point from inside this content would stop someone mid-scroll?"
Examples from past leads: "$63K-to-$1,275 profit collapse," "13.1% vs 4.4% net margin split," "75x faster buyer matching." This becomes either a subtitle element, a visual callout, or part of the visual metaphor.

#### Phase 2: Choose the Visual Metaphor

One concept per cover. Functional, not decorative. The image must communicate what the lead magnet is about within 2 seconds at mobile scroll speed.

The metaphor comes FROM the content, not from generic design thinking.

**Examples from actual production:**
- Grass breaking through concrete → landscaping business breaking through a revenue plateau
- Vault door with gold light → capital readiness, something valuable behind the door
- Split house with AI scanning overlay → rehab estimation powered by technology
- Gold circuit pipeline with 4 phase nodes → systematic tool stack across operational phases

**Test:** If someone saw only the visual with no text, could they identify the general category of the lead magnet within 5 seconds? If not, the metaphor is too abstract.

**What never works:**
- Abstract energy bursts with no conceptual anchor
- Generic success imagery (mountain peaks, rocket ships, chess pieces)
- Literal depictions (a photo of a house for real estate)
- Multiple competing metaphors in one cover

#### Phase 3: Build Three Prompts (Not One)

**Prompt A — Typography-Dominant (Safest, Most Reliable)**

The title carries the cover. One subtle visual accent. Think Alex Hormozi's $100M Leads cover.

When to use: title is specific and punchy enough alone. Visual metaphor is hard to render. Reliability is more important than visual ambition.

Reliability: 8/10

Layout zones:
- Top 35%: Small qualifier audience line → Big title (white) + key accent word (gold gradient) → Subtitle
- Center 45%: Minimal visual accent. Soft radial glow behind text. Faint texture. Maximum 1 stat callout box if needed.
- Bottom 20%: Author name and brand line. Small. Secondary. Quiet.

```
Vertical cover image, exactly 3:4 aspect ratio. Flat 2D graphic design, 
NOT a photograph.

[SCENE]
Ebook cover design. Pure obsidian black background (#050505). Warm amber 
radial glow at center behind the main title text at approximately 12% 
opacity, creating depth without distraction.

TITLE ZONE — TOP THIRD:
[Insert qualifier line: "For Business Owners Doing $500K+"]
[Insert main title — word by word in quotes, with line breaks specified]
[Insert subtitle text]
Text alignment: center-aligned.

VISUAL ACCENT — CENTER:
[Single subtle visual element OR simply the warm glow with no additional 
visual elements. Describe ONE thing.]

AUTHOR ZONE — BOTTOM:
"TOBY POTTER" in flat gold (#D4AF37), bold, uppercase.
"THE UNSHAKABLE INVESTOR" below in small white uppercase text.

[LIGHTING]
No directional lighting on a flat graphic. Warm ambient inner glow 
behind the central text only.

[STYLE]
Alex Hormozi book cover aesthetic meets Bloomberg annual report. 
Typography-first. Clean. No decoration. Not a Canva template. 
Not a course brochure.

[QUALITY]
Razor-sharp text edges. No compression artifacts. Print quality.

Only three colors: black, white, and gold.

TEXT SIZE HIERARCHY:
1st largest: [Title anchor word or phrase]
2nd largest: [Main title remaining lines]
3rd largest: [Subtitle]
4th largest: Author name
5th largest: Brand line and qualifier

Avoid the following: [UNIVERSAL NEGATIVE + TYPOGRAPHY ADDITIONS + DARK 
BACKGROUND ADDITIONS]
```

**Prompt B — Visual Metaphor Hero (Higher Risk, Higher Reward)**

The signature visual concept from Phase 2 occupies the center. Title is large but shares the canvas with the visual.

Reliability: 5/10 — plan for 2 to 3 regenerations. Hybrid fallback is expected, not a failure.

Critical structural lesson: Describe the visual element as ONE unified object with named parts, not a list of independent elements. "A horizontal gold pipeline bar with four hexagonal nodes mounted on it" works. "Four hexagons floating near a bar with arrows between them" produces chaos.

```
Vertical cover image, exactly 3:4 aspect ratio. Flat 2D graphic design 
with one photorealistic visual element.

[SCENE]
Ebook cover. Pure obsidian black background (#050505). Soft warm amber 
radial glow at center behind the visual element, approximately 10% opacity.

TITLE ZONE — TOP THIRD:
[Qualifier line small text]
[Main title, word for word, line breaks specified]
[Subtitle]
All text centered.

VISUAL ZONE — CENTER 45%:
[Describe ONE unified visual structure. Name it as a single object. 
Specify its parts as components OF that object, not separate floating 
elements. Always use symmetry language: "symmetrical," "centered," 
"mathematically even."]

Example structure language: "A single horizontal gold bar spanning 80% 
of the image width, with four hexagonal stations mounted on it at 
mathematically evenly spaced intervals. Each hexagon is the same size. 
The bar is centered vertically in this zone."

AUTHOR ZONE — BOTTOM 20%:
"TOBY POTTER" in flat gold, bold uppercase.
"THE UNSHAKABLE INVESTOR" in small white uppercase.

[LIGHTING]
Warm inner glow behind the visual element only. No cool tones anywhere.

[STYLE]
Apple product announcement meets premium SaaS launch visual. 
Sophisticated. Restrained. Not a PowerPoint flowchart. Not clip art.

[QUALITY]
Sharp clean edges on all visual elements. Print quality resolution.

Only three colors: black, white, and gold.

COMPOSITION RULES:
Visual element centered horizontally and vertically within its zone.
All visual elements are part of one unified structure, not scattered.
Generous breathing room between all zones.
Title at top is the first element read. Visual supports it from below.

DO NOT INCLUDE: scattered floating elements, tilted panels, 
concentric circles, particle effects, multiple competing visual 
concepts, title at the bottom

Avoid the following: [UNIVERSAL NEGATIVE + TYPOGRAPHY + DARK BACKGROUND + 
add specific failure modes from this lead magnet if known]

HYBRID FALLBACK NOTE: If text renders with any errors, regenerate with 
"No text in the image. Visual only." The [describe the core visual object] 
is the asset. All typography goes in Canva.
```

**Prompt C — Toby as Anchor (Authority Play)**

Toby in high-contrast black and white with gold rim light. One structural element behind him communicating the system. Andy Elliott Sales Warrior Playbook style adapted for Unshakable.

When to use: credibility depends on the author. Audience needs to trust the source before trusting the content.

**Tell user:** Attach `toby_black_suit.png`

```
Vertical cover image, exactly 3:4 aspect ratio. Mixed: photorealistic 
portrait + flat graphic design elements.

CRITICAL INSTRUCTION: The subject's face MUST exactly match the attached 
reference photo. Do not approximate or alter any facial features. 
This overrides all other instructions.

[SCENE]
Ebook cover. Pure obsidian black background (#050505). 

TITLE ZONE — TOP 35%:
[Qualifier line]
[Main title text, word for word]
[Subtitle]
All centered.

VISUAL ZONE — CENTER 45%:
Black and white portrait of a distinguished man in his late 50s. 
Silver-white hair, gray beard, dark suit. Use attached reference photo 
for exact likeness. Cropped from chest up. Facing camera, strong 
expression. High contrast B&W processing with warm sepia undertone.
Strong warm gold rim light along right shoulder and hair edge 
(#D4AF37 flat gold).

Behind him, ONE structural element: [describe the system graphic — 
a ring with phase icons, an annotation overlay, a framework diagram. 
Describe it as one object. It frames him from behind, he is in FRONT 
of it.] The structural element is partially visible on both sides of 
his figure.

AUTHOR ZONE — BOTTOM 20%:
"TOBY POTTER" in flat gold, bold uppercase.
"THE UNSHAKABLE INVESTOR" in small white uppercase.

[LIGHTING]
On portrait: dramatic Rembrandt lighting from upper left. Strong warm 
gold rim light on right shoulder. High contrast black and white.
On background element: ambient warm glow.

[STYLE]
Andy Elliott Sales Warrior Playbook meets Bloomberg executive profile. 
Authority and system visible simultaneously. Not a motivational poster. 
Not a life coach cover.

[QUALITY]
Sharp portrait. Razor-sharp text. Print quality.

Only three colors: black, white, gold.

FINAL CHECK: Face identical to reference. This overrides all instructions.

DO NOT INCLUDE: full-color portrait in this variant, garbled labels 
on the structural element, title at the bottom

Avoid the following: [UNIVERSAL NEGATIVE + PORTRAIT + DARK BACKGROUND + 
TYPOGRAPHY]

HYBRID FALLBACK NOTE: If the structural element behind Toby renders 
with garbled text or wrong structure, regenerate as portrait only with 
gold rim light. Build the structural element and all text in Canva.
```

#### Phase 4: Post-Cover Ad Creative Set

Once the book cover is finalized, build these five ad creative prompts using the finished cover image attached as a reference input.

1. **3D Book Mockup with Callout Arrows** (1:1 or 4:5): Floating 3D render of the book at an angle with 3 to 4 curved gold arrows pointing to value callout boxes. Text for callout boxes comes from the top proof points identified in Phase 1. Attach the finished cover.

2. **Toby Holding Book with Headline** (1:1): Toby holding the book in a natural hand. Bold headline text on the left. "FREE" callout. Gold bottom bar. Attach both `toby_black_suit.png` and the finished cover.

3. **Stacked Stack Style** (1:1): 3 to 4 copies of the book fanned or stacked on a dark background. Bold headline above. Price anchor if relevant. Obsidian background with brand gold glow. Attach finished cover.

4. **Real-World Context Shot** (1:1 or 4:5): The book photographed in a relevant real-world environment (conference table, desk, field if applicable to the content). iPhone snapshot aesthetic. Not staged. The book appears mid-work. Attach finished cover.

5. **Clean Book Hero** (1:1): Book centered on a warm dark textured surface with subtle environmental props relevant to the content. Headlines on the left. Gold bottom bar. Premium editorial feel. Attach finished cover.

---

### 12E. Carousel Slides (4:5)

Use for: Instagram and Facebook carousel posts. Educational content, step breakdowns, social proof sequences.

**Design System Requirements — All Slides Must Share:**
- Identical background color (#F5F3F0 warm off-white for editorial OR #050505 obsidian for brand)
- Same font pairing (serif headline + sans-serif subtext)
- Same brush stroke highlight style and color
- Same bottom dot and arrow navigation system
- Same text alignment (all left-aligned to same invisible guide)

**Carousel Dot Progression (specify per slide):**
```
Slide 1: First dot filled gold, remaining dots outlined gray
Slide 2: Second dot filled gold, remaining outlined
Slide N (final): Nth dot filled gold, no arrow, no "SWIPE" text
```

**Hook Slide Rules:**
- Headline: 8 to 10 words maximum
- Must answer both: "Is this for me?" and "What do I get if I swipe?"
- Slide 2 must also work as a standalone hook (Instagram resurfaces from slide 2)
- One idea per slide. No cramming.

**Single Slide Template (Editorial Style — Warm Off-White Background):**

```
Vertical portrait image, exactly 4:5 aspect ratio. Flat 2D graphic design. 
NOT a photograph. Clean editorial typography.

[SCENE]
Carousel slide design. Warm off-white background (#F5F3F0). No texture. 
Clean and spacious.

HEADLINE TEXT ZONE:
[Exact headline text, line breaks specified]
Font style: large bold black serif (Playfair Display Black style)
Specific words to highlight: "[word or phrase]" — these words have a 
hand-painted flat gold (#D4AF37) brush stroke behind them. Organic, 
textured, visible bristle marks. Not a digital highlight bar.

SUBTEXT ZONE (below headline):
"[Exact subtext]"
Font style: clean sans-serif, dark gray

BOTTOM NAVIGATION ZONE:
Slide [N] of [total]. Dot N filled gold, remaining dots outlined gray.
Right arrow icon. "SWIPE →" in light gray, small text.
[On final slide: no arrow, no SWIPE text]

VISUAL ACCENT ELEMENT (optional, if relevant):
Abstract geometric element in flat gold (#D4AF37) at 12 to 15% opacity. 
NOT an icon. NOT clip art. Think Bloomberg data visualization stripped 
to pure geometry. Positioned to not compete with the headline.

[STYLE]
Bloomberg data editorial meets Harvard Business Review feature. 
Clean. Restrained. Not a social media template. Not a Canva design.

[QUALITY]
Sharp text edges. Clean. Print quality.

DO NOT INCLUDE: photographs, icons, clip art, gradients, 3D elements, 
blue tones, decorative borders

Avoid the following: [UNIVERSAL NEGATIVE + TYPOGRAPHY ADDITIONS]
```

---

### 12F. Webinar and Landing Page Hero (16:9)

Use for: webinar registration page hero images, YouTube thumbnails, webinar promotion headers.

**Tell user:** Attach `toby_black_suit.png`

```
Horizontal image, exactly 16:9 aspect ratio. Photorealistic. Cinematic.

CRITICAL INSTRUCTION: Subject's face must exactly match attached reference 
photo. Do not alter any facial features.

[SCENE]
Webinar landing page hero image. 

LEFT HALF: Subject. [Color Portrait Block from Section 7]. Cropped from 
mid-chest up, positioned in the left third of the frame, facing slightly 
right into the frame. Warm confident expression.

RIGHT HALF: Clean dark space. A subtle warm typographic zone area with no 
actual text rendered — this area will receive text overlay in production. 
Dark, slightly lighter than the deepest obsidian, giving the text area 
some implied depth.

Background: deep obsidian black (#050505). Dramatic darkened city skyline 
in the extreme background, barely visible. No blue. Warm amber city glow 
only. Heavy obsidian overlay.

All critical content concentrated in the center 60% of the horizontal 
width. Left and right outer edges atmospheric only.

[LIGHTING]
Key light from upper left on subject. Warm golden rim light on right 
shoulder and hair edge. Ambient warm glow. No cool tones.

[COMPOSITION]
Subject in left third. Right half clear and dark for text. Safe zone for 
text overlay begins where subject's body ends.

[STYLE]
Bloomberg Summit speaker feature. Netflix documentary chapter card. 
Not an internet marketing page header. Not a stock photo composite.

[QUALITY]
8K hyperdetailed. 85mm portrait quality on subject. Magazine standard.

Only three colors: black, white, and gold.

FINAL CHECK: Face identical to reference.

Avoid the following: [UNIVERSAL NEGATIVE + PORTRAIT + DARK BACKGROUND + 
CITY SKYLINE]
```

---

## 13. THE HYBRID WORKFLOW

### When to Use It

Use the hybrid workflow (Gemini generates the visual, Canva handles all text and branding elements) when:
- More than 3 text elements in the image
- Text must overlap a person or complex background
- Precise brand typography is required
- CTA bars, credential lines, or multi-line event details are needed
- Carousel slides requiring identical text styling across all slides
- Any final production asset (versus a draft concept)

The hybrid workflow is not a backup plan. For Prompt B and C book covers, it is the expected workflow. Plan for it from the start.

### Step-by-Step Process

**Step 1:** Write the Gemini prompt with "No text in the image. Visual only." at the end. Request clean dark space wherever text will be added.

**Step 2:** Generate in Gemini. Iterate on the VISUAL only until composition, lighting, mood, and subject are correct. Do not worry about text at this stage.

**Step 3:** Download the final visual as PNG.

**Step 4:** Open Canva. Create new design at exact pixel dimensions needed (1080×1080, 1080×1350, etc.).

**Step 5:** Upload the Gemini visual as the background layer.

**Step 6:** Add all text elements using brand fonts.

**Step 7:** Add CTA bars, bottom strips, credential lines, badge elements.

**Step 8:** Export as PNG. Done.

### Canva Text Specifications

| Element | Font | Weight | Color | Case |
|---------|------|--------|-------|------|
| Main headline | Montserrat | Black (900) | White #FFFFFF | Uppercase |
| Gold accent line | Montserrat | Extra Bold (800) | Apply Ignite gradient | Uppercase |
| Subtitle / body | Inter | Regular (400) or Medium (500) | White #FFFFFF | Sentence case |
| Qualifier / eyebrow | Inter | Medium (500) | Gold #D4AF37 | Uppercase, wide letter spacing |
| Author name | Montserrat or Inter | Bold (700) | Gold #D4AF37 | Uppercase |
| Brand line | Inter | Regular (400) | White #FFFFFF | Uppercase, smaller |
| CTA button text | Montserrat | Bold (700) | White on dark background | Uppercase |

**Pro tip:** When prompting the Gemini visual, instruct it to make the upper portion darker than the lower portion. This creates a natural dark zone for white headline text without needing a separate dark overlay strip. White text on a naturally dark area always looks better than white text on an added gradient strip.

---

## 14. ITERATION PROTOCOL

When a Gemini output needs improvement, use this decision tree. Do not iterate randomly.

**Face is wrong (common):**
Do not re-prompt with the same approach. After 2 failed face attempts, switch to the composite workflow: generate the background and environment WITHOUT Toby, then composite his real photo into the scene in Canva. Match lighting in Canva adjustments. This is the professional agency workflow, not a failure.

**Text is warped or misspelled:**
Do not re-prompt for text correction. Use the current output as a layout positioning template. The positions, sizes, and relationships Gemini established are your guide. Rebuild all text in Canva using the AI output as reference.

**Output is too busy or cluttered:**
Remove elements from the prompt. Never add. Reducing the element count by 30% almost always improves quality.

**Wrong mood (output looks promotional or cheap):**
Add more design philosophy language. Increase the quality of style references. Add anti-references ("This is NOT a Facebook ad"). Add: "This image belongs in a premium financial publication, not an internet marketing funnel."

**Colors wrong (blue tint, wrong gold):**
Reinforce color rules with more force. State them earlier in the prompt. Double down on negatives: "Absolutely no blue tones. No navy. No cool colors of any kind. The only colors in this image are black, white, and warm gold."

**Layout or spacing is off:**
Add breathing room language. Use the "——— generous space ———" notation between elements. Use words: "generous," "ample," "significant breathing room," "wide margins."

**After 3 failed iterations on a specific element:**
Stop prompting for that element. Build it in code (Python/Pillow or React) or in Canva for pixel-perfect control. Use Gemini only for atmospheric and photographic elements where AI generation adds genuine value.

---

## 15. COMMON FAILURE PATTERNS AND FIXES

These patterns have appeared across every lead magnet and ad creative production session. Check this list before writing prompts.

| Failure | Why It Happens | Fix |
|---------|---------------|-----|
| Background comes out navy/dark blue | Gemini defaults to cool dark tones | State "#050505 obsidian black, no blue tones" AND add blue to negative prompt. Both required. |
| Fire appears without being requested | Brand association or dramatic default | Include "no fire, no flames, no embers" in both prompt body AND negative prompt |
| Face looks AI-generated or waxy | Default Gemini skin rendering | Add "natural skin texture, subtle pores and lines visible, not waxy, not overly smooth, real photographic quality" |
| Text warped or misspelled | AI text rendering limitation | Use hybrid workflow. Generate visual only. Add text in Canva. |
| Wide image content gets cropped on platforms | Platform crops to center square | State the center square safe zone rule in the prompt. Center ALL critical elements. |
| Output looks like a Canva template | Prompt is too structured/clinical | Describe a scene, not a layout. Reference Bloomberg, Netflix, Pentagram. Add: "This is NOT a Canva template." |
| "Parts list" scatter | 8+ independent elements scatter randomly | Describe ONE unified structure with named components. One object, not many. |
| Title buried at bottom | Visual hero takes center and pushes title down | State explicitly: "Title at the top. Always. The visual supports the title from below." |
| Too many floating stat panels | Three or four data callout boxes conflict | Maximum ONE stat callout on any cover. Additional stats go in the ad creative, not the book cover. |
| Multiple subjects look pasted/collaged | Gemini struggles with multi-person composites | Describe blending explicitly: opacity values, dissolving edges, shared lighting. |
| Star or diamond artifacts in corners | Gemini decorative default | Add to negative prompt: "star shape, diamond shape, corner decorations" |
| Image looks cheesy or internet marketing | Too many elements, too much color variety | Enforce 3-color palette. Remove 30% of elements. Add: "This is NOT a Facebook ad." |
| Navy creep despite specifying black | Model defaults strongly to navy | State "Not navy. Not dark blue." in the background description AND include "navy, blue" in negative prompt. Both required. |

---

## 16. PRE-GENERATE CHECKLIST

Run through every item before submitting any prompt to Gemini.

### Foundation
- [ ] First line of prompt states the exact aspect ratio
- [ ] Platform safe zone rule included if applicable (9:16 or 2:1)
- [ ] Design philosophy and reference brands mentioned (Bloomberg, TED, Pentagram, Netflix)
- [ ] Anti-reference included ("Not a Canva template," "Not a Facebook ad," etc.)

### Color Rules
- [ ] Background described as "obsidian black," "pure black," or "#050505 near-black"
- [ ] "No blue tones. No navy." appears in the prompt body
- [ ] Blue/navy/teal/cyan in the negative prompt
- [ ] Only 3 colors referenced (black, white, gold — or the correct flat/gradient specification)
- [ ] Gold treatment specified (gradient for ads, flat for editorial/PDF)

### Composition and Spatial Language
- [ ] Spatial relationships described in natural language only (no pixel coordinates)
- [ ] Clear zones defined for text overlay areas
- [ ] Breathing room and generous spacing emphasized between elements
- [ ] If wide format (2:1): center square safe zone rule stated explicitly

### Toby (if present)
- [ ] Face accuracy instruction at TOP of prompt
- [ ] Face accuracy instruction referenced in the subject description block
- [ ] Face accuracy FINAL CHECK at BOTTOM of prompt
- [ ] User instructed which reference photo to attach
- [ ] Correct portrait block from Section 7 used verbatim

### Text Elements
- [ ] Every word of on-image text spelled out in quotation marks
- [ ] Text size hierarchy defined (1st largest, 2nd largest, etc.)
- [ ] Hybrid workflow decision made (text in Gemini or build in Canva)
- [ ] If hybrid: "No text in the image. Visual only." included in prompt
- [ ] If hybrid: clean dark space location specified for post-production text

### Negative Prompts
- [ ] Universal negative block included
- [ ] Portrait additions included (if Toby or any person is in the image)
- [ ] Typography additions included (if text appears in the image)
- [ ] Dark background additions included
- [ ] Situation-specific additions included based on the content type

### Final
- [ ] Prompt is under 300 words (excluding negative prompt)
- [ ] Fire/flames/embers exclusion present in both prompt body and negative prompt
- [ ] One compositional structure (not a parts list)
- [ ] Hybrid fallback note included for Prompt B and C book covers

---

*The Unshakable Investor | Gemini Master Prompting Playbook v2.0*
*Compiled: March 2026 | Source: All production sessions, failure logs, and iterative learnings*
*Primary reader: Claude AI assistant | Platform: Gemini Nano Banana Pro 2, web interface only*
