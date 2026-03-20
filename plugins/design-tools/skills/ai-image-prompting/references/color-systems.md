# Color Systems for Ad Creatives

## Psychology-Driven Color Selection

### Primary Conversion Colors

| Color | Hex | RGB | Psychology | Best Use |
|-------|-----|-----|------------|----------|
| Authority Red | #8B0000 | 139,0,0 | Urgency, power, action | CTA buttons, limited offers |
| Trust Blue | #1E3A5F | 30,58,95 | Security, reliability | Finance, corporate, tech |
| Wealth Gold | #D4AF37 | 212,175,55 | Premium, success, value | Accents, highlights, luxury |
| Deep Purple | #1a1a3e | 26,26,62 | Luxury, mystery, wisdom | Backgrounds, high-end |
| Rich Teal | #0d4f4f | 13,79,79 | Growth, balance, health | Wellness, finance, eco |
| Clean White | #FFFFFF | 255,255,255 | Purity, clarity, space | Text, headlines, contrast |

---

## Research-Backed Insights

### Color Impact on Conversions

**Red CTA Buttons:**
- 21-40% higher CTR than green in A/B tests
- Creates urgency without explicit urgency language
- Works best on dark backgrounds

**Blue for Trust:**
- 90% of snap judgments about products based on color alone
- Blue associated with trust in financial services (80%+ of banks)
- Reduces anxiety in high-ticket purchases

**Gold/Yellow Accents:**
- Draws eye without overwhelming
- Associated with premium/luxury positioning
- 14% more likely to be noticed than neutral tones

---

## Ad Background Palettes

### Luxury Dark (Most Versatile)
```css
/* Primary gradient */
background: linear-gradient(180deg, #1a1a3e 0%, #0a0a1f 100%);

/* With purple accent */
background: linear-gradient(180deg, #1a1a3e 0%, #2d1f3d 50%, #0a0a1f 100%);

/* Hex stops for prompts */
Start: #1a1a3e (deep purple)
End: #0a0a1f (near black)
```

### Authority Power
```css
/* Red undertone */
background: linear-gradient(135deg, #1a1a3e 0%, #3d0c0c 100%);

/* Stronger red */
background: linear-gradient(180deg, #2a1a2e 0%, #4a0f0f 50%, #0a0505 100%);

/* Hex stops */
Start: #1a1a3e or #2a1a2e
Mid: #3d0c0c or #4a0f0f
End: #0a0a1f or #0a0505
```

### Wealth/Premium Teal
```css
/* Teal to purple */
background: linear-gradient(180deg, #0d4f4f 0%, #1a1a3e 100%);

/* Deeper variant */
background: linear-gradient(180deg, #0a3a3a 0%, #1a1a3e 50%, #0a0a1f 100%);

/* Hex stops */
Start: #0d4f4f or #0a3a3a
Mid: #1a1a3e
End: #0a0a1f
```

### Trust/Corporate Blue
```css
/* Professional blue */
background: linear-gradient(180deg, #1E3A5F 0%, #0f1f33 100%);

/* With subtle warmth */
background: linear-gradient(180deg, #1E3A5F 0%, #1a2a3f 50%, #0a1525 100%);
```

---

## Text Color Specifications

### On Dark Backgrounds

| Element | Color | Hex | Opacity |
|---------|-------|-----|---------|
| Headline | Pure White | #FFFFFF | 100% |
| Subhead | Warm White | #F5F5F5 | 100% |
| Body Text | Soft White | #FFFFFF | 87% |
| Secondary | Light Gray | #B0B0B0 | 100% |
| Accent Text | Gold | #D4AF37 | 100% |
| Highlight | Bright Gold | #FFD700 | 100% |

### CTA Button Colors

| Style | Background | Text | Border |
|-------|------------|------|--------|
| Primary | #8B0000 | #FFFFFF | none |
| Primary Hover | #A50000 | #FFFFFF | none |
| Secondary | transparent | #D4AF37 | #D4AF37 1px |
| Secondary Hover | #D4AF37 | #1a1a3e | #D4AF37 1px |
| Urgent | #FF0000 | #FFFFFF | none |

---

## Color Combinations by Ad Type

### Authority/Expertise Ads
```
Background: #1a1a3e → #0a0a1f gradient
Headline: #FFFFFF
Subhead: #D4AF37
Body: #FFFFFF 87%
CTA: #8B0000 bg, #FFFFFF text
Accent glow: #D4AF37 20% opacity
```

### Financial/Investment Ads
```
Background: #1E3A5F → #0f1f33 gradient
Headline: #FFFFFF
Numbers: #00FF88 (gains) or #D4AF37
Body: #E0E0E0
CTA: #0d4f4f bg, #FFFFFF text
Trust badge: #D4AF37
```

### Health/Wellness Ads
```
Background: #0d4f4f → #1a1a3e gradient
Headline: #FFFFFF
Accent: #7FFFD4 (aquamarine)
Body: #E8F5E9 (soft green-white)
CTA: #2E7D32 bg, #FFFFFF text
```

### Luxury/Premium Ads
```
Background: #0a0a0a → #1a1a3e gradient
Headline: #D4AF37
Subhead: #FFFFFF
Body: #C0C0C0
CTA: #D4AF37 bg, #0a0a0a text
Borders: #D4AF37 1px
```

### Urgency/Scarcity Ads
```
Background: #1a1a3e → #3d0c0c gradient
Headline: #FF4444 or #FFFFFF
Timer/Numbers: #FF0000
Body: #FFFFFF
CTA: #FF0000 bg, #FFFFFF text
Pulse effect: #FF0000 glow animation
```

---

## Prompt-Ready Color Blocks

### Copy-Paste for Prompts

**Luxury Dark Background:**
```
dark cinematic gradient background transitioning from deep purple #1a1a3e at the top to near-black #0a0a1f at the bottom
```

**Authority Red Accent:**
```
deep crimson red #8B0000 accent elements, reminiscent of luxury automotive or premium wine branding
```

**Gold Highlight:**
```
rich gold #D4AF37 metallic accents and highlights, catching dramatic lighting
```

**Trust Teal:**
```
sophisticated teal #0d4f4f undertones suggesting stability and growth
```

---

## Accessibility Considerations

### Contrast Ratios (WCAG AA)

| Text Size | Minimum Ratio | Recommended |
|-----------|---------------|-------------|
| Large (18px+) | 3:1 | 4.5:1 |
| Normal | 4.5:1 | 7:1 |

### Safe Combinations on Dark

| Background | Text | Ratio | Pass |
|------------|------|-------|------|
| #1a1a3e | #FFFFFF | 12.6:1 | ✅ AAA |
| #1a1a3e | #D4AF37 | 6.8:1 | ✅ AA |
| #0a0a1f | #FFFFFF | 18.1:1 | ✅ AAA |
| #8B0000 | #FFFFFF | 7.2:1 | ✅ AAA |

---

## Industry Color Benchmarks

### Finance/Investment
- Primary: Navy #1E3A5F, Forest #2E5A3E
- Accent: Gold #D4AF37, Green #00C853
- Avoid: Bright reds (loss association)

### Health/Medical
- Primary: Teal #0d4f4f, Blue #2196F3
- Accent: Green #4CAF50, White
- Avoid: Dark reds, harsh yellows

### Tech/SaaS
- Primary: Blue #2196F3, Purple #7C4DFF
- Accent: Cyan #00BCD4, White
- Neutral: Grays #424242 → #FAFAFA

### E-commerce/Retail
- Primary: Brand-specific
- CTA: Red #FF5722, Orange #FF9800
- Urgency: Red #F44336, Yellow #FFEB3B

### Coaching/Education
- Primary: Purple #6A1B9A, Blue #1976D2
- Accent: Gold #FFD700, Orange #FF9800
- Trust: Teal #00897B
