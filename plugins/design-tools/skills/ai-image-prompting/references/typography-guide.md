# Typography Guide for Ad Creatives

## Scale Systems

### Modular Scale Ratios

| Ratio | Name | Multiplier | Character |
|-------|------|------------|-----------|
| 1.067 | Minor Second | ×1.067 | Subtle, minimal |
| 1.125 | Major Second | ×1.125 | Gentle progression |
| 1.200 | Minor Third | ×1.2 | Balanced, readable |
| 1.250 | Major Third | ×1.25 | **Recommended for ads** |
| 1.333 | Perfect Fourth | ×1.333 | Clear hierarchy |
| 1.500 | Perfect Fifth | ×1.5 | **Strong impact** |
| 1.618 | Golden Ratio | ×1.618 | **Premium/luxury** |
| 2.000 | Octave | ×2 | Dramatic contrast |

---

## Ad Typography Specifications

### Major Third Scale (1.25) - Compact Designs

| Element | Size | Weight | Line Height |
|---------|------|--------|-------------|
| Display/Hero | 48px | 900 | 1.1 |
| Headline | 38px | 800 | 1.15 |
| Subhead | 31px | 600 | 1.2 |
| Body Large | 25px | 400 | 1.4 |
| Body | 20px | 400 | 1.5 |
| Caption | 16px | 400 | 1.5 |

### Perfect Fifth Scale (1.5) - Strong Impact

| Element | Size | Weight | Line Height |
|---------|------|--------|-------------|
| Display/Hero | 72px | 900 | 1.0 |
| Headline | 48px | 800 | 1.1 |
| Subhead | 32px | 600 | 1.2 |
| Body Large | 21px | 400 | 1.4 |
| Body | 16px | 400 | 1.5 |
| Caption | 12px | 400 | 1.5 |

### Golden Ratio Scale (1.618) - Premium/Luxury

| Element | Size | Weight | Line Height |
|---------|------|--------|-------------|
| Display/Hero | 89px | 900 | 1.0 |
| Headline | 55px | 800 | 1.05 |
| Subhead | 34px | 600 | 1.15 |
| Body Large | 21px | 400 | 1.4 |
| Body | 16px | 400 | 1.5 |
| Caption | 13px | 400 | 1.5 |

---

## Font Weight Reference

| Weight | Name | Use Case |
|--------|------|----------|
| 100 | Thin | Decorative only |
| 200 | Extra Light | Large display |
| 300 | Light | Subheads, elegant |
| 400 | Regular | Body text |
| 500 | Medium | Emphasized body |
| 600 | Semi Bold | Subheads, labels |
| 700 | Bold | Headlines, CTA |
| 800 | Extra Bold | Primary headlines |
| 900 | Black | Hero text, impact |

---

## Font Stacks for Different Tones

### Authority/Professional
```css
font-family: 'Montserrat', 'Helvetica Neue', Arial, sans-serif;
/* Alternative */
font-family: 'Poppins', 'Segoe UI', Tahoma, sans-serif;
```

### Luxury/Premium
```css
font-family: 'Playfair Display', 'Georgia', serif; /* Headlines */
font-family: 'Cormorant Garamond', 'Times New Roman', serif;
```

### Modern/Tech
```css
font-family: 'Inter', 'SF Pro Display', -apple-system, sans-serif;
font-family: 'DM Sans', 'Roboto', sans-serif;
```

### Friendly/Approachable
```css
font-family: 'Nunito', 'Open Sans', sans-serif;
font-family: 'Quicksand', 'Lato', sans-serif;
```

### Impact/Bold Statement
```css
font-family: 'Oswald', 'Impact', sans-serif;
font-family: 'Anton', 'Bebas Neue', sans-serif;
```

---

## AI Prompt Font Descriptions

### For Bold Headlines
```
bold sans-serif typography similar to Montserrat Black or Oswald,
uppercase letters with tight letter-spacing, high contrast against background
```

### For Luxury Feel
```
elegant serif typography similar to Playfair Display or Didot,
refined letterforms with dramatic thick-thin contrast, sophisticated spacing
```

### For Modern Tech
```
clean geometric sans-serif typography similar to Inter or SF Pro,
balanced letterforms, generous x-height, contemporary feel
```

### For Urgency
```
condensed bold sans-serif typography similar to Oswald or Impact,
tightly packed uppercase letters, maximum impact, immediate attention
```

---

## Ad Type Typography Specs

### Authority Figure Ads

```
HEADLINE: 48-72px
- Font: Bold sans-serif (Montserrat, Poppins)
- Weight: 800-900
- Color: #FFFFFF
- Transform: UPPERCASE
- Letter-spacing: 0.02em

SUBHEAD: 24-36px
- Font: Medium sans-serif
- Weight: 600
- Color: #D4AF37 (gold)
- Transform: Title Case
- Letter-spacing: 0.01em

BODY: 16-20px
- Font: Regular sans-serif
- Weight: 400
- Color: #FFFFFF (87% opacity)
- Line-height: 1.5

CTA: 18-24px
- Font: Bold sans-serif
- Weight: 700
- Color: #FFFFFF
- Transform: UPPERCASE
- Letter-spacing: 0.05em
```

### Value Stack Ads

```
VALUE NUMBER: 48-64px
- Font: Extra Bold sans-serif
- Weight: 800
- Color: #D4AF37
- Style: Tabular numbers

HEADLINE: 36-48px
- Weight: 800
- Color: #FFFFFF

BULLET POINTS: 18-24px
- Weight: 500
- Color: #FFFFFF
- Icon color: #D4AF37

STRIKETHROUGH PRICE: 24-32px
- Weight: 600
- Color: #888888
- Decoration: line-through

SALE PRICE: 32-48px
- Weight: 800
- Color: #00FF88 or #D4AF37
```

### Testimonial Ads

```
QUOTE: 24-32px
- Font: Italic serif or sans
- Weight: 400-500
- Color: #FFFFFF
- Style: Italic
- Quote marks: #D4AF37, 72px+

NAME: 18-24px
- Weight: 700
- Color: #FFFFFF

TITLE/COMPANY: 14-18px
- Weight: 400
- Color: #FFFFFF (70% opacity)
```

---

## Text Effects for Prompts

### Glow Effect (Headlines)
```css
text-shadow: 0 0 40px rgba(212, 175, 55, 0.5),
             0 0 80px rgba(212, 175, 55, 0.3);
```

Prompt language:
```
headline text with soft golden glow effect, luminous quality,
text appears to emit warm light against dark background
```

### Drop Shadow (Readability)
```css
text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
```

Prompt language:
```
text with subtle drop shadow for enhanced readability,
crisp letterforms with soft shadow separation from background
```

### Emboss/3D Effect
```css
text-shadow: 1px 1px 0px rgba(255,255,255,0.3),
             -1px -1px 0px rgba(0,0,0,0.3);
```

Prompt language:
```
slightly embossed text effect, subtle 3D quality,
letters appear raised from surface with highlight and shadow edges
```

---

## Character Limits by Format

### Facebook/Meta Ads

| Element | Hard Limit | Recommended |
|---------|------------|-------------|
| Primary Text | 125 chars | 80-100 |
| Headline | 40 chars | 25-30 |
| Description | 30 chars | 20-25 |
| CTA Button | 10 chars | 2-3 words |

### Within Creative (Image)

| Element | Max Words | Max Chars |
|---------|-----------|-----------|
| Hero Headline | 3-5 | 20-30 |
| Subhead | 5-10 | 40-60 |
| Value Prop | 8-12 | 50-70 |
| CTA | 2-4 | 15-20 |

---

## Responsive Typography (By Ad Size)

### Stories/Reels (1080×1920)
- Hero: 72-96px
- Subhead: 36-48px
- Body: 24-32px
- CTA: 28-36px

### Feed Square (1080×1080)
- Hero: 48-72px
- Subhead: 28-36px
- Body: 18-24px
- CTA: 22-28px

### Feed Portrait (1080×1350)
- Hero: 56-80px
- Subhead: 32-42px
- Body: 20-26px
- CTA: 24-32px

---

## Quick Reference: Prompt Typography

```
BOLD IMPACT HEADLINE:
"bold white sans-serif headline text in the style of Montserrat Black,
uppercase letters, tight tracking"

ELEGANT SUBHEAD:
"refined gold-colored subhead text #D4AF37, medium weight,
title case, slightly expanded letter-spacing"

CLEAN BODY:
"clean readable body text, white at 87% opacity,
comfortable line spacing, left-aligned"

URGENT CTA:
"bold uppercase call-to-action text, white letters on
deep red #8B0000 rounded button, wide letter-spacing"
```
