---
name: ai-image-prompting
description: Generate production-ready AI image prompts optimized for Facebook/Meta advertising with exact specifications for Gemini Imagen, Ideogram, DALL-E 3, Midjourney, FLUX.1, and Stable Diffusion.
---

# AI Ad Creative Prompt Engineering

> Generate production-ready AI image prompts optimized for Facebook/Meta advertising with exact specifications for Gemini Imagen, Ideogram, DALL-E 3, Midjourney, FLUX.1, and Stable Diffusion.

## ACTIVATION

When user requests ad creative generation, activate this skill to produce structured prompts with:
- Exact color values (hex codes)
- Precise dimensions and safe zones
- Model-specific syntax and parameters
- Typography hierarchy specifications
- Platform-compliant compositions

---

## CORE PROMPT ARCHITECTURE

### Universal Ad Creative Structure

```
[SCENE COMPOSITION]
Background: {gradient/solid/texture} + {hex colors}
Subject: {authority figure/product/lifestyle} + {positioning}
Lighting: {dramatic/soft/studio} + {direction}

[TYPOGRAPHY ZONES]
Headline: {font-weight} {size-ratio} {color} {position}
Subhead: {font-weight} {size-ratio} {color} {position}
CTA: {button-style} {color} {text}

[EFFECTS LAYER]
Shadows: {CSS-style shadow stack}
Glows: {color} {spread} {opacity}
Overlays: {gradient/vignette} {opacity}
```

---

## MODEL-SPECIFIC SYNTAX

### Gemini Imagen (Nano Banana / Nano Banana Pro)

> **Deep Dive:** See [gemini-imagen-advanced.md](references/gemini-imagen-advanced.md) for complete JSON schemas, all parameters, and 5 production-ready JSON templates.

**Model Tiers:**
| Model | Codename | Best For | Cost |
|-------|----------|----------|------|
| `gemini-3-pro-image-preview` | Nano Banana Pro | 4K, character consistency, multi-image fusion | Premium |
| `gemini-2.5-flash-image` | Nano Banana | Fast iteration, good text rendering | ~$0.039/img |
| `imagen-4.0-ultra-generate-001` | Imagen Ultra | Highest single-image fidelity | $0.06/img |
| `imagen-4.0-generate-001` | Imagen Standard | Balanced quality/speed | $0.04/img |
| `imagen-4.0-fast-generate-001` | Imagen Fast | Rapid prototyping | $0.02/img |

**Complete JSON Request (Vertex AI):**
```json
{
  "instances": [{"prompt": "YOUR_PROMPT"}],
  "parameters": {
    "sampleCount": 4,
    "aspectRatio": "9:16",
    "sampleImageSize": "2K",
    "enhancePrompt": true,
    "negativePrompt": "text, watermark, logo, amateur, blurry",
    "personGeneration": "allow_adult",
    "safetySetting": "block_medium_and_above",
    "outputOptions": {
      "mimeType": "image/png",
      "compressionQuality": 90
    }
  }
}
```

**Python SDK (Gemini 2.5/3 Pro):**
```python
from google import genai
from google.genai import types

client = genai.Client(api_key="YOUR_KEY")

response = client.models.generate_content(
    model="gemini-2.5-flash-image",  # or "gemini-3-pro-image-preview"
    contents="Your detailed prompt here",
    config=types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"],
        image_config=types.ImageConfig(
            aspect_ratio="9:16",
            image_size="2K"  # "4K" for Nano Banana Pro
        )
    )
)
```

**Key Parameters:**
| Parameter | Values | Notes |
|-----------|--------|-------|
| `aspectRatio` | 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9 | Extended in Gemini 2.5+ |
| `sampleImageSize` | "1K", "2K", "4K"* | *4K only Nano Banana Pro |
| `personGeneration` | "allow_adult", "allow_all", "dont_allow" | Controls people in output |
| `enhancePrompt` | true/false | AI improves your prompt |
| `seed` | 1-2147483647 | Deterministic output (requires watermark=false) |

**SLCSQ Prompt Framework:**
```
[SCENE]
Subject: Confident executive, 40s, tailored navy suit, burgundy pocket square
Background: Seamless gradient #1a1a3e to #0a0a1f, subtle luxury texture

[LIGHTING]
Key: Large softbox 45° camera-left, 1.5m distance
Fill: Silver reflector camera-right, 2:1 ratio
Rim: Golden #D4AF37 strip light, camera-right behind subject

[COMPOSITION]
Position: Left third, facing into negative space
Zones: Upper-right 30% for headline, lower-right for CTA
Focus: Eyes sharp, shallow DOF background

[STYLE]
Reference: Annie Leibovitz executive portraiture
Aesthetic: Authority, success, Fortune 500 quality

[QUALITY]
Resolution: 8K hyperdetailed, magazine print quality
Camera: Canon EOS R5, 85mm f/1.2L at f/2.8
Post: Subtle dodge/burn, clean retouch, color graded
```

**Nano Banana Pro Advanced Features:**
- **Multi-Image Reference:** Up to 14 images (6 objects + 5 humans + 3 style)
- **Character Consistency:** 95%+ accuracy across frames
- **Thought Signatures:** Pass between requests for multi-turn consistency
- **Google Search Grounding:** Real-time info integration

**Aspect Ratios:** 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9

---

### Ideogram (Best for Text Rendering)

**API Structure:**
```json
{
  "image_request": {
    "prompt": "[PROMPT]",
    "model": "V_2",
    "magic_prompt_option": "AUTO",
    "aspect_ratio": "ASPECT_9_16",
    "style_type": "REALISTIC"
  }
}
```

**Text-Heavy Prompt Pattern:**
```
Advertisement design with embedded text "[HEADLINE TEXT]" in bold
sans-serif white letters at top, "[SUBHEAD]" below in smaller gold
#D4AF37 text, dark cinematic background #1a1a3e to #0d0d1a gradient,
[SUBJECT], professional commercial photography style,
[CTA BUTTON: rounded rectangle, deep red #8B0000, white text]
```

**Style Types:** REALISTIC, DESIGN, RENDER_3D, ANIME
**Rendering Speed:** TURBO (fast), BALANCED, QUALITY (best)

---

### DALL-E 3

**Prompt Structure:**
```
[SUBJECT] + [ACTION/POSE] + [SETTING/BACKGROUND] + [MOOD/ATMOSPHERE] + [STYLE]
```

**Ad Creative Pattern:**
```
A confident professional [DESCRIPTION] standing in a powerful pose,
wearing [ATTIRE], against a deep cinematic gradient background
transitioning from midnight purple to near-black, dramatic golden
rim lighting from the left, photorealistic commercial advertisement
style, space preserved in upper third for text overlay,
high-end brand aesthetic, 8K resolution quality
```

**Best Practices:**
- 5-7 descriptive elements optimal
- Natural language (no weight syntax)
- Explicit style references improve consistency
- Specify negative space for text zones

---

### Midjourney

**Syntax Elements:**
- Multi-prompt: `prompt1 :: prompt2` (equal weight)
- Weighted: `element::2` (double importance)
- Negative: `--no element` or `element::-0.5`
- Parameters: `--ar 9:16 --s 500 --q 2`

**Ad Creative Pattern:**
```
professional advertisement::2, [SUBJECT DESCRIPTION]::1.5,
dark cinematic background #1a1a3e to black gradient::1.2,
dramatic side lighting::1, golden rim light accent::0.8,
commercial photography::1.5, high-end brand aesthetic::1,
clear text overlay zone upper frame::1
--ar 9:16 --s 750 --q 2 --no text, words, letters, watermark
```

**Key Parameters:**
- `--ar` Aspect ratio (9:16, 1:1, 4:5)
- `--s` Stylization (0-1000, higher = more artistic)
- `--q` Quality (0.25, 0.5, 1, 2)
- `--chaos` Variation (0-100)

---

### FLUX.1 (Excellent Text Rendering)

**Prompt Style:** Natural language, no weights, hierarchical description

**Ad Creative Pattern:**
```
Professional advertisement photograph for a premium brand campaign.

SCENE: A [SUBJECT DESCRIPTION] positioned using rule of thirds
against a dark cinematic gradient background flowing from deep
purple #1a1a3e at the top to near-black #0a0a0f at the bottom.

LIGHTING: Dramatic three-point setup with key light from upper-left,
golden rim light (#D4AF37) creating edge separation, subtle fill
from right to preserve shadow detail.

COMPOSITION: Subject occupies left two-thirds, clear negative space
in upper-right quadrant reserved for headline text overlay.
Lower section maintains breathing room for call-to-action button.

STYLE: Ultra-high-end commercial photography aesthetic,
hyperrealistic detail, professional retouching quality,
8K resolution clarity.

TEXT ELEMENTS: Display "[HEADLINE]" in bold white Impact-style
lettering, "[VALUE PROP]" in gold #D4AF37 accent text.
```

**Strengths:** Exceptional text accuracy, natural language understanding

---

### Stable Diffusion (AUTOMATIC1111/ComfyUI)

**Weight Syntax:**
- `(word:1.5)` - Explicit weight (0.1-2.0)
- `(word)` = 1.1x, `((word))` = 1.21x
- `[word]` = 0.9x, `[[word]]` = 0.81x

**Ad Creative Pattern:**
```
(professional advertisement:1.4), (commercial photography:1.3),
(confident professional person:1.2), [SUBJECT DETAILS],
(dark cinematic gradient background:1.3), deep purple #1a1a3e,
(dramatic side lighting:1.2), (golden rim light:1.1),
(high-end brand aesthetic:1.2), (8K detail:1.1),
(clear text overlay zone:1.1), upper frame composition

Negative prompt: (text:1.4), (watermark:1.4), (logo:1.3),
(low quality:1.3), (blurry:1.2), (amateur:1.2), cartoon, anime
```

**Recommended Settings:**
- Steps: 30-50
- CFG Scale: 7-9
- Sampler: DPM++ 2M Karras

---

## FACEBOOK AD SPECIFICATIONS

### Dimensions by Placement

| Placement | Dimensions | Aspect Ratio |
|-----------|------------|--------------|
| Feed Square | 1080×1080 | 1:1 |
| Feed Portrait | 1080×1350 | 4:5 |
| Stories/Reels | 1080×1920 | 9:16 |
| Carousel | 1080×1080 | 1:1 |
| Right Column | 1200×628 | 1.91:1 |

### Safe Zones (Critical)

**Stories/Reels (1080×1920):**
```
┌─────────────────────┐
│   TOP SAFE: 250px   │ ← Profile/UI overlay
│                     │
│                     │
│   CONTENT ZONE      │ ← 1420px safe area
│                     │
│                     │
│  BOTTOM SAFE: 250px │ ← CTA/swipe overlay
└─────────────────────┘
```

**Feed (1080×1350):**
```
┌─────────────────────┐
│  TOP MARGIN: 90px   │
│                     │
│   CONTENT ZONE      │ ← 1170px safe area
│                     │
│ BOTTOM MARGIN: 90px │
└─────────────────────┘
```

---

## COLOR SYSTEM

### High-Converting Ad Palette

| Color | Hex | Psychology | Usage |
|-------|-----|------------|-------|
| Authority Red | #8B0000 | Urgency, power | CTA buttons |
| Trust Blue | #1E3A5F | Security, trust | Corporate, finance |
| Wealth Gold | #D4AF37 | Premium, success | Accents, highlights |
| Deep Purple | #1a1a3e | Luxury, mystery | Backgrounds |
| Rich Teal | #0d4f4f | Growth, stability | Wellness, finance |
| Pure White | #FFFFFF | Clarity, clean | Headlines, text |

### Gradient Combinations

**Luxury Dark:**
```css
background: linear-gradient(180deg, #1a1a3e 0%, #0a0a1f 100%);
```

**Authority Power:**
```css
background: linear-gradient(135deg, #1a1a3e 0%, #3d0c0c 100%);
```

**Wealth Signal:**
```css
background: linear-gradient(180deg, #0d4f4f 0%, #1a1a3e 100%);
```

---

## TYPOGRAPHY HIERARCHY

### Scale Ratios

| Ratio | Name | Multiplier | Use Case |
|-------|------|------------|----------|
| 1.25 | Major Third | ×1.25 | Compact designs |
| 1.5 | Perfect Fifth | ×1.5 | Balanced hierarchy |
| 1.618 | Golden Ratio | ×1.618 | Premium/luxury |

### Ad Typography Stack

```
HEADLINE: 48-72px, Weight 800-900, White #FFFFFF
SUBHEAD:  24-36px, Weight 600-700, Gold #D4AF37
BODY:     16-20px, Weight 400-500, White 90% opacity
CTA:      18-24px, Weight 700, White on #8B0000
```

---

## SHADOW SYSTEM

### Elevation Layers (CSS Reference)

**Subtle Lift:**
```css
box-shadow: 0 2px 4px rgba(0,0,0,0.1);
```

**Medium Elevation:**
```css
box-shadow:
  0 4px 6px rgba(0,0,0,0.1),
  0 2px 4px rgba(0,0,0,0.06);
```

**Dramatic Depth:**
```css
box-shadow:
  0 10px 15px rgba(0,0,0,0.1),
  0 4px 6px rgba(0,0,0,0.05),
  0 2px 4px rgba(0,0,0,0.05);
```

**Text Glow (Headlines):**
```css
text-shadow: 0 0 40px rgba(212,175,55,0.5);
```

---

## PROMPT TEMPLATES BY AD TYPE

### 1. Authority Figure Ad

```
[MODEL-SPECIFIC PREFIX]

Professional advertisement featuring a confident [GENDER] [PROFESSION]
in their [AGE]s, wearing [PREMIUM ATTIRE: tailored suit/blazer],
standing in a powerful stance with arms crossed or one hand gesturing.

BACKGROUND: Dark cinematic gradient from #1a1a3e (top) to #0a0a1f (bottom)
LIGHTING: Dramatic Rembrandt lighting from upper-left, golden rim light
(#D4AF37) creating edge separation on right side
COMPOSITION: Subject positioned left-third, clear negative space
upper-right for headline overlay

ATMOSPHERE: Successful, authoritative, trustworthy
STYLE: High-end commercial photography, Fortune 500 executive portrait
QUALITY: 8K detail, professional retouching, magazine-worthy

[MODEL-SPECIFIC SUFFIX/PARAMETERS]
```

### 2. Product Showcase Ad

```
[MODEL-SPECIFIC PREFIX]

Premium product advertisement featuring [PRODUCT DESCRIPTION]
as hero element, floating or elegantly positioned at center.

BACKGROUND: Rich gradient from #0d4f4f to #1a1a3e with subtle
radial light burst behind product
LIGHTING: Studio three-point setup, soft key light, rim highlights
COMPOSITION: Product centered, space above for headline,
space below for value propositions

EFFECTS: Subtle reflection on glossy surface, product glow
STYLE: Apple-inspired minimalist product photography
QUALITY: Commercial catalog quality, precise edge definition

[MODEL-SPECIFIC SUFFIX/PARAMETERS]
```

### 3. Value Stack Ad

```
[MODEL-SPECIFIC PREFIX]

Advertisement layout with dark premium background #1a1a3e,
designed for value proposition display.

VISUAL ELEMENT: [RELEVANT IMAGERY] positioned left side (40% width)
TEXT ZONES:
- Headline zone top-right with ample padding
- Three bullet-point zones vertically stacked right side
- CTA button zone bottom-right

STYLE ELEMENTS:
- Gold #D4AF37 checkmarks or icons for value points
- White #FFFFFF headline text space
- Red #8B0000 CTA button zone
- Subtle vignette darkening at edges

[MODEL-SPECIFIC SUFFIX/PARAMETERS]
```

### 4. Testimonial Ad

```
[MODEL-SPECIFIC PREFIX]

Social proof advertisement featuring testimonial design:
SUBJECT: Friendly, relatable person [DEMOGRAPHIC] with genuine smile
BACKGROUND: Soft gradient, lighter than authority ads (#2a2a4e to #1a1a3e)
COMPOSITION: Subject positioned right, quote zone left

DESIGN ELEMENTS:
- Large quotation mark graphic zone (gold #D4AF37)
- Text zone for testimonial (white, italic style)
- Name/title zone below quote
- Subtle 5-star rating zone

MOOD: Trustworthy, authentic, approachable
LIGHTING: Soft, flattering beauty lighting

[MODEL-SPECIFIC SUFFIX/PARAMETERS]
```

### 5. Urgency/Scarcity Ad

```
[MODEL-SPECIFIC PREFIX]

High-urgency advertisement design:
BACKGROUND: Dark base with red accent gradient (#1a1a3e to #3d0c0c)
COMPOSITION: Dynamic diagonal energy, urgency visual cues

KEY ELEMENTS:
- Bold countdown/number zone (prominent placement)
- "LIMITED" or "EXCLUSIVE" badge zone
- Strong CTA zone with red #8B0000 treatment
- Lightning or energy accent elements (subtle, professional)

ATMOSPHERE: Urgent, exciting, exclusive opportunity
STYLE: Direct response advertising aesthetic
CONTRAST: High contrast between dark background and bright elements

[MODEL-SPECIFIC SUFFIX/PARAMETERS]
```

---

## QUALITY CHECKLIST

Before finalizing any prompt, verify:

- [ ] Aspect ratio matches placement (9:16 Stories, 1:1/4:5 Feed)
- [ ] Safe zones preserved for text overlays
- [ ] Color values specified as hex codes
- [ ] Model-specific syntax correctly applied
- [ ] Negative prompts exclude unwanted elements (text, watermarks)
- [ ] Lighting direction specified
- [ ] Background gradient includes start and end colors
- [ ] Typography zones clearly defined
- [ ] Style matches brand tier (luxury, professional, etc.)

---

## HYBRID WORKFLOW NOTE

For optimal results requiring precise text:
1. Generate base visual using any model
2. Use Ideogram or FLUX.1 for text-heavy versions
3. Or generate text-free base, add typography in Figma/Photoshop

This ensures highest quality for both imagery and typography.

---

## REFERENCES

- [json-schemas.md](references/json-schemas.md) - Complete API schemas
- [model-comparison.md](references/model-comparison.md) - Model strengths/limitations
- [color-systems.md](references/color-systems.md) - Extended color psychology
- [typography-guide.md](references/typography-guide.md) - Font stacks and ratios
- [platform-specs.md](references/platform-specs.md) - All platform dimensions
- [sources.md](references/sources.md) - Research sources

---

*Skill Version: 1.0 | Last Updated: 2024*
