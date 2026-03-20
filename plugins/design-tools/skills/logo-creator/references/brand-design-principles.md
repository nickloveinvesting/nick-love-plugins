# Brand Design Principles Reference

Supplemental design intelligence for the logo creator. Read this when the user needs deeper direction on design theory, color, typography, or composition.

---

## Why Most AI Logos Fail

AI image generators default to what they've seen most: generic, slightly-dated, gradient-heavy icons. Fighting this requires:

1. **Over-specifying constraints** — Tell it what NOT to do as much as what to do
2. **Forcing simplicity** — Add "favicon-scale", "32x32 readability", "single concept"
3. **Specifying era** — "2024 minimal design", "timeless not trendy", "no 2010s skeuomorphism"
4. **Removing AI defaults** — Explicitly: "no drop shadows", "no gradients", "no bevels", "no lens flares"

---

## Color Psychology for Logos

### By Industry

| Industry | Dominant Colors | Why |
|----------|----------------|-----|
| Finance/Legal | Navy, dark green, black, gold | Trust, stability, authority |
| Health/Wellness | Green, teal, soft blue, white | Life, calm, cleanliness |
| Tech/SaaS | Blue, purple, dark/black | Innovation, intelligence |
| Food/Consumer | Red, orange, yellow, warm tones | Appetite, energy, warmth |
| Real Estate | Navy, dark green, gold, brown | Trust, grounded, premium |
| Education | Blue, purple, green | Knowledge, growth |
| Fitness | Black, red, orange, neon | Power, energy, performance |
| Luxury | Black, gold, deep navy, white | Exclusivity, refinement |
| Creative/Agency | Bold primaries, black, unexpected combos | Creativity, boldness |

### Color Count Rules
- **1 color** — Most versatile, most professional
- **2 colors** — Strong contrast pair, primary + accent
- **3 colors** — Maximum for a logo that still prints cleanly
- **4+ colors** — Only justified for very specific brand contexts (Olympic rings, Google)

### High-Contrast Pairs That Work
- Navy + Gold
- Black + Orange
- Dark Green + White
- Deep Purple + Yellow
- Charcoal + Teal
- Black + Red

---

## Typography in Logos

When the logo includes a wordmark or lettermark:

### Font Personality Map
| Type | Personality | Brand Fit |
|------|-------------|-----------|
| Geometric sans (Futura, Montserrat) | Modern, clean, confident | Tech, startups, minimal brands |
| Humanist sans (Gill Sans, Optima) | Friendly, approachable | Healthcare, education, community |
| Serif (Garamond, Times) | Traditional, authoritative | Law, finance, academia, luxury |
| Slab serif (Rockwell, Clarendon) | Bold, reliable, industrial | Construction, tools, outdoor, craft |
| Script | Personal, artistic, elegant | Beauty, fashion, food, personal brands |
| Display/Custom | Unique, memorable | Any brand that can afford custom type |

### Lettermark Rules
- Use uppercase for authority, lowercase for approachability
- Custom ligatures or overlaps make lettermarks distinctive
- Negative space tricks (FedEx arrow, Amazon smile) create depth without complexity
- Avoid more than 2-3 letters in a mark

---

## Composition Principles

### Visual Weight
A logo needs to feel balanced. Common pitfalls:
- Icon is too large vs. wordmark (or vice versa)
- Excessive padding on one side
- Asymmetric mark that reads as a mistake, not a choice

### Negative Space
The best logos use negative space actively:
- FedEx: arrow hidden between E and x
- NBC: peacock in the colorful lines
- Amazon: smile pointing A to Z
- WWF: panda from shapes

Prompt for this with: "clever negative space", "hidden meaning", "dual-concept logomark"

### Safe Zone
A logo needs breathing room. The crop_logo.py script handles this with 5px padding. Don't go below 3px.

---

## Logo Families / System Thinking

If the brand will need multiple versions, plan for:

1. **Primary mark** — Full logo with icon + wordmark
2. **Stacked version** — Icon above text (for square contexts)
3. **Horizontal version** — Icon beside text (for navigation bars)
4. **Icon only** — For favicons, app icons, profile photos
5. **Wordmark only** — For contexts where the icon alone won't be recognized

Not all brands need all five. But it's worth noting which versions will be needed early, as it affects prompt direction (standalone icon vs. integrated mark).

---

## Real-World Logo Analysis Framework

When evaluating a logo candidate, run this mental checklist:

**Memorability Test**
— Could someone sketch this after seeing it once?
— Does it have a single visual idea, or multiple competing elements?

**Reproduction Test**
— Does it work embroidered on a shirt? (removes fine detail)
— Does it work on a pen or small merchandise? (forces simplicity)
— Does it work in a single ink color? (removes color dependency)

**Context Test**
— Does it fit the industry without blending in?
— Would it look credible next to competitors?
— Does it attract the right audience and repel the wrong one?

**Timelessness Test**
— Would this have looked intentional in 2010?
— Would it still look intentional in 2035?
— Are you using any effects that will feel dated in 3 years?

---

## Competitive Differentiation

Before finalizing any logo, check what competitors look like. Key differentiators:

- **Color** — If all competitors use blue, consider being the brand that doesn't
- **Style** — If everyone is minimal, a bold emblem stands out
- **Concept** — If competitors use abstract shapes, a literal/mascot approach differentiates
- **Weight** — If the market is busy, being the cleanest wins attention

Ask the user: "What do your top 3 competitors' logos look like?" Then make sure the final logo is visually distinct from all three.

---

## Prompt Modifiers by Brand Archetype

### The Hero (Bold, Confident, Takes Charge)
Add: `strong, powerful, commanding, geometric precision, bold weight, high contrast`
Avoid: `soft, rounded, pastel, friendly curves`

### The Sage (Expert, Knowledgeable, Trustworthy)
Add: `refined, authoritative, clean lines, structured, established, precise`
Avoid: `playful, colorful, loose, energetic`

### The Creator (Innovative, Artistic, Original)
Add: `creative, unexpected, clever negative space, original concept, artistic`
Avoid: `corporate, generic, expected, safe`

### The Jester (Fun, Playful, Entertains)
Add: `energetic, fun, dynamic, expressive, character-driven, bright colors`
Avoid: `serious, minimal, cold, formal`

### The Caregiver (Nurturing, Supportive, Safe)
Add: `warm, approachable, rounded forms, soft colors, friendly, open`
Avoid: `sharp, cold, aggressive, complex`

### The Ruler (Premium, Prestigious, Exclusive)
Add: `luxurious, premium, elegant, refined, gold or deep tones, sophisticated`
Avoid: `casual, bright, playful, trendy`
