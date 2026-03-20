# Gemini Imagen Advanced Reference
## Complete JSON Schema & Professional Techniques

> Cutting-edge techniques for Google Gemini Imagen 4.0, Gemini 2.5 Flash Image (Nano Banana), and Gemini 3 Pro Image (Nano Banana Pro)

---

## Model Hierarchy

| Model | Codename | Strengths | Cost |
|-------|----------|-----------|------|
| `gemini-3-pro-image-preview` | Nano Banana Pro | Best quality, character consistency, 4K, multi-image fusion | Premium |
| `gemini-2.5-flash-image` | Nano Banana | Fast, good quality, text rendering | ~$0.039/image |
| `imagen-4.0-ultra-generate-001` | Imagen Ultra | Highest fidelity single images | $0.06/image |
| `imagen-4.0-generate-001` | Imagen Standard | Balanced quality/speed | $0.04/image |
| `imagen-4.0-fast-generate-001` | Imagen Fast | Quick iterations | $0.02/image |

---

## Complete JSON Schema

### Imagen 4.0 API (Vertex AI)

```json
{
  "instances": [
    {
      "prompt": "string (required)"
    }
  ],
  "parameters": {
    "sampleCount": 1,
    "aspectRatio": "9:16",
    "sampleImageSize": "2K",
    "seed": 2147483647,
    "addWatermark": false,
    "enhancePrompt": true,
    "negativePrompt": "string",
    "language": "en",
    "personGeneration": "allow_adult",
    "safetySetting": "block_medium_and_above",
    "includeRaiReason": true,
    "includeSafetyAttributes": true,
    "outputOptions": {
      "mimeType": "image/png",
      "compressionQuality": 90
    },
    "storageUri": "gs://bucket/path/"
  }
}
```

### Gemini 2.5 Flash / 3 Pro Image (Python SDK)

```python
from google import genai
from google.genai import types

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_content(
    model="gemini-2.5-flash-image",  # or "gemini-3-pro-image-preview"
    contents="Your detailed prompt here",
    config=types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"],
        image_config=types.ImageConfig(
            aspect_ratio="9:16",
            image_size="2K"  # or "4K" for Nano Banana Pro
        )
    )
)

# Access generated image
for part in response.candidates[0].content.parts:
    if part.inline_data:
        image_data = part.inline_data.data
        mime_type = part.inline_data.mime_type
```

---

## Parameter Reference

### Core Parameters

| Parameter | Type | Values | Default | Notes |
|-----------|------|--------|---------|-------|
| `sampleCount` / `number_of_images` | int | 1-4 | 4 | Images per request |
| `aspectRatio` / `aspect_ratio` | string | See below | "1:1" | Output dimensions |
| `sampleImageSize` / `image_size` | string | "1K", "2K", "4K"* | "1K" | *4K only Nano Banana Pro |
| `seed` | uint32 | 1-2147483647 | random | Deterministic output |
| `addWatermark` / `add_watermark` | bool | true/false | true | SynthID watermark |
| `enhancePrompt` / `enhance_prompt` | bool | true/false | true | AI prompt improvement |
| `negativePrompt` / `negative_prompt` | string | any | null | What to avoid |
| `language` | string | See below | "auto" | Prompt language |

### Aspect Ratios by Model

**Imagen 4.0:**
- `"1:1"` - Square (1024×1024)
- `"3:4"` - Portrait
- `"4:3"` - Landscape
- `"9:16"` - Vertical/Stories (576×1024)
- `"16:9"` - Horizontal/Video

**Gemini 2.5 Flash / 3 Pro (Extended):**
- `"1:1"`, `"2:3"`, `"3:2"`, `"3:4"`, `"4:3"`
- `"4:5"`, `"5:4"`, `"9:16"`, `"16:9"`, `"21:9"`

### Safety & Person Settings

| Parameter | Values | Description |
|-----------|--------|-------------|
| `personGeneration` | `"allow_adult"` | Adults only, no celebrities (default) |
| | `"allow_all"` | All people including children |
| | `"dont_allow"` | No people or faces |
| `safetySetting` | `"block_none"` | No filtering |
| | `"block_only_high"` | Block severe only |
| | `"block_medium_and_above"` | Moderate filtering (default) |
| | `"block_low_and_above"` | Strictest filtering |

### Language Codes

```
"auto", "en", "zh", "zh-CN", "zh-TW", "hi", "ja", "ko", "pt", "es"
```

### Output Options

```json
"outputOptions": {
  "mimeType": "image/png",      // or "image/jpeg"
  "compressionQuality": 90      // 0-100, JPEG only, default 75
}
```

---

## Gemini 3 Pro Image (Nano Banana Pro) Advanced Features

### Multi-Image Reference System

```python
# Up to 14 reference images total:
# - 6 object reference images (high-fidelity props/items)
# - 5 human reference images (character consistency)
# - 3 additional style/context references

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents=[
        types.Content(
            parts=[
                types.Part(text="Create a marketing image with these elements:"),
                types.Part(inline_data=types.Blob(
                    mime_type="image/jpeg",
                    data=reference_image_1_bytes
                )),
                types.Part(inline_data=types.Blob(
                    mime_type="image/jpeg",
                    data=character_reference_bytes
                )),
                types.Part(text="""
                    Combine the product from image 1 with the character
                    from image 2 in a professional advertisement setting.
                    Dark cinematic background #1a1a3e to #0a0a1f gradient.
                    Character positioned left, product hero right.
                    Dramatic golden rim lighting.
                """)
            ]
        )
    ],
    config=types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"],
        image_config=types.ImageConfig(
            aspect_ratio="9:16",
            image_size="4K"
        )
    )
)
```

### Thought Signatures (Multi-Turn Consistency)

```python
# First generation
response1 = client.models.generate_content(...)
thought_signature = None

for part in response1.candidates[0].content.parts:
    if hasattr(part, 'thought') and part.thought:
        thought_signature = part.thought_signature

# Subsequent refinements - pass thought signature back
response2 = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents=[
        types.Content(
            parts=[
                types.Part(thought_signature=thought_signature),
                types.Part(text="Now adjust the lighting to be warmer...")
            ]
        )
    ],
    config=...
)
```

### Google Search Grounding

```python
# Enable real-time information in image generation
response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents="Create an advertisement showing today's weather in New York",
    config=types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"],
        tools=[{"google_search": {}}]
    )
)

# Response includes grounding metadata
grounding_info = response.candidates[0].grounding_metadata
```

---

## Professional Ad Creative JSON Templates

### Template 1: Authority Figure Ad

```json
{
  "instances": [{
    "prompt": "Professional advertisement photograph featuring a confident executive in their 40s wearing a tailored navy suit, standing in a powerful stance with arms crossed. BACKGROUND: Dark cinematic gradient from deep purple #1a1a3e at top transitioning to near-black #0a0a1f at bottom. LIGHTING: Dramatic Rembrandt three-point setup with key light from upper-left at 45 degrees, golden rim light #D4AF37 creating edge separation on subject's right side, subtle fill from right preserving shadow detail. COMPOSITION: Subject positioned on left third using rule of thirds, clear negative space in upper-right quadrant reserved for headline text overlay, lower-right clear for CTA button zone. ATMOSPHERE: Successful, authoritative, trustworthy executive portrait. STYLE: Ultra high-end commercial photography, Fortune 500 executive portrait aesthetic, magazine advertising quality. QUALITY: 8K hyperdetailed texture, professional retouching, razor-sharp focus on eyes, subtle skin texture preserved. CAMERA: Shot with Sony Alpha 1, 85mm f/1.4 GM lens, shallow depth of field with background blur."
  }],
  "parameters": {
    "sampleCount": 4,
    "aspectRatio": "9:16",
    "sampleImageSize": "2K",
    "enhancePrompt": true,
    "personGeneration": "allow_adult",
    "safetySetting": "block_medium_and_above",
    "negativePrompt": "text, words, letters, watermark, logo, signature, amateur, low quality, blurry, distorted face, extra limbs, cartoon, anime, illustration",
    "outputOptions": {
      "mimeType": "image/png"
    }
  }
}
```

### Template 2: Product Showcase Ad

```json
{
  "instances": [{
    "prompt": "Premium product advertisement photograph featuring a luxury skincare bottle as hero element, floating elegantly at center with subtle reflection below. BACKGROUND: Rich gradient from sophisticated teal #0d4f4f at top to deep purple #1a1a3e at bottom, with subtle radial light burst emanating from behind product creating depth and focus. LIGHTING: Professional studio three-point softbox setup, soft diffused key light from upper-left, crisp rim highlights defining product edges, subtle bounce fill from below. COMPOSITION: Product perfectly centered, generous negative space above for headline overlay (top 25%), space below for value propositions and CTA (bottom 30%), product occupies central 45% of frame. EFFECTS: Subtle product glow suggesting premium quality, clean reflection on glossy invisible surface below, no harsh shadows. STYLE: Apple-inspired minimalist product photography, ultra-clean high-end cosmetic advertising aesthetic. QUALITY: 8K commercial catalog quality, precise edge definition, crystal-clear product detail, professional color grading. CAMERA: Phase One IQ4 150MP, 120mm macro lens, f/11 for maximum sharpness, focus stacked."
  }],
  "parameters": {
    "sampleCount": 4,
    "aspectRatio": "4:5",
    "sampleImageSize": "2K",
    "enhancePrompt": true,
    "personGeneration": "dont_allow",
    "negativePrompt": "people, hands, text, words, cluttered background, harsh shadows, reflections of photographer, dust, scratches, fingerprints, amateur lighting",
    "outputOptions": {
      "mimeType": "image/png"
    }
  }
}
```

### Template 3: Value Stack Layout

```json
{
  "instances": [{
    "prompt": "Advertisement layout design with dark premium background gradient from #1a1a3e to #0a0a1f, designed for value proposition display. VISUAL ELEMENTS: Subtle geometric pattern overlay at 5% opacity suggesting sophistication, elegant diagonal light rays from upper-left corner at 10% opacity. LAYOUT ZONES: Left side (40% width) reserved for lifestyle imagery zone with soft vignette border, right side structured for text hierarchy. TEXT ZONES MARKED: Large headline zone in upper-right with ample breathing room, three distinct bullet-point zones vertically stacked on right side with consistent spacing, prominent CTA button zone in bottom-right. ACCENT ELEMENTS: Subtle gold #D4AF37 decorative line separating zones, small checkmark icon placeholders in gold for value points, rounded rectangle CTA button zone outlined in deep red #8B0000. ATMOSPHERE: Premium, exclusive, high-value offer presentation. STYLE: Direct response advertising meets luxury brand aesthetic, clean and scannable layout hierarchy. QUALITY: Sharp vector-like edges on all design elements, smooth gradients, no banding."
  }],
  "parameters": {
    "sampleCount": 4,
    "aspectRatio": "9:16",
    "sampleImageSize": "2K",
    "enhancePrompt": true,
    "personGeneration": "dont_allow",
    "negativePrompt": "actual text, readable words, specific letters, faces, people, cluttered, busy, amateur design, gradients with banding",
    "outputOptions": {
      "mimeType": "image/png"
    }
  }
}
```

### Template 4: Testimonial Social Proof

```json
{
  "instances": [{
    "prompt": "Social proof advertisement design featuring testimonial layout. SUBJECT: Friendly, relatable professional woman in her 30s with genuine warm smile, natural makeup, wearing smart casual attire (blazer over simple top), positioned on right side of frame. BACKGROUND: Soft gradient lighter than typical authority ads, transitioning from warm purple #2a2a4e at edges to #1a1a3e center, creating approachable atmosphere. COMPOSITION: Subject on right third looking slightly toward center, large empty quote zone on left side (60% width) for testimonial text overlay, space for oversized quotation mark graphic in gold #D4AF37 upper-left. ZONES: Name and title zone below quote area, small 5-star rating graphic zone, company logo placeholder zone. LIGHTING: Soft, flattering beauty lighting setup, butterfly light from front-above, gentle fill eliminating harsh shadows, subtle rim light for separation. MOOD: Trustworthy, authentic, relatable, genuine success story. STYLE: Professional testimonial advertising, lifestyle portrait meets commercial aesthetic. QUALITY: Natural skin texture, authentic expression, 4K detail."
  }],
  "parameters": {
    "sampleCount": 4,
    "aspectRatio": "1:1",
    "sampleImageSize": "2K",
    "enhancePrompt": true,
    "personGeneration": "allow_adult",
    "safetySetting": "block_medium_and_above",
    "negativePrompt": "text, words, overly perfect skin, plastic looking, fake smile, stock photo feel, stiff pose, harsh lighting, unflattering angles",
    "outputOptions": {
      "mimeType": "image/png"
    }
  }
}
```

### Template 5: Urgency/Scarcity

```json
{
  "instances": [{
    "prompt": "High-urgency advertisement design with dynamic energy. BACKGROUND: Dark base with dramatic red accent gradient flowing from #1a1a3e through #3d0c0c to #4a0f0f, creating urgency atmosphere without overwhelming. COMPOSITION: Dynamic diagonal energy lines suggesting movement and immediacy, asymmetrical balance creating visual tension. KEY ZONES: Large central zone for countdown timer or bold number display, prominent 'LIMITED' or 'EXCLUSIVE' badge zone in upper area with gold #D4AF37 border, strong CTA zone in lower-center with deep red #8B0000 background, secondary urgency text zone. ACCENT ELEMENTS: Subtle lightning bolt or energy burst graphics (professional, not cartoonish), sharp geometric shapes suggesting speed, metallic gold accent lines at 15% opacity. LIGHTING EFFECTS: Dramatic spotlight effect on central focal zone, edge glow in warning colors, subtle pulsing energy suggestion. ATMOSPHERE: Urgent, exciting, exclusive limited-time opportunity. STYLE: Direct response advertising with premium execution, casino/luxury meets scarcity marketing. QUALITY: Clean edges, no artifacts, smooth gradients, high contrast between dark and accent elements."
  }],
  "parameters": {
    "sampleCount": 4,
    "aspectRatio": "9:16",
    "sampleImageSize": "2K",
    "enhancePrompt": true,
    "personGeneration": "dont_allow",
    "negativePrompt": "text, numbers, countdown, cheesy graphics, cartoonish elements, clip art, low quality effects, busy cluttered design, illegible elements",
    "outputOptions": {
      "mimeType": "image/png"
    }
  }
}
```

---

## Structured Prompt Framework

### The SCENE-LIGHT-COMPOSE-STYLE-QUALITY (SLCSQ) Framework

```
[SCENE]
Subject: {detailed subject description}
Background: {gradient/environment with hex colors}
Props/Elements: {supporting visual elements}

[LIGHTING]
Key Light: {type, direction, intensity}
Fill Light: {type, direction, ratio}
Rim/Accent: {color, position, effect}
Ambient: {overall mood lighting}

[COMPOSITION]
Subject Position: {rule of thirds placement}
Negative Space: {zones reserved for text}
Focal Point: {primary attention area}
Balance: {symmetrical/asymmetrical}

[STYLE]
Reference: {photography style/genre}
Aesthetic: {brand/mood keywords}
Execution: {commercial/editorial/etc}

[QUALITY]
Resolution: {detail level}
Camera: {equipment simulation}
Post-Processing: {editing style}
```

### Example Using SLCSQ Framework

```
[SCENE]
Subject: Confident male entrepreneur, early 40s, silver-touched hair,
wearing charcoal three-piece suit with burgundy pocket square
Background: Seamless gradient #1a1a3e to #0a0a1f with subtle
texture overlay suggesting luxury
Props: None, clean executive portrait

[LIGHTING]
Key Light: Large softbox, 45° camera-left, 1.5m from subject
Fill Light: Silver reflector camera-right, 2:1 ratio
Rim/Accent: Golden #D4AF37 strip light, camera-right behind subject
Ambient: Dark, moody, controlled studio environment

[COMPOSITION]
Subject Position: Left third, facing camera-right into negative space
Negative Space: Upper-right 30% clear for headline, lower-right for CTA
Focal Point: Subject's eyes
Balance: Asymmetrical with visual weight left

[STYLE]
Reference: Annie Leibovitz executive portraiture
Aesthetic: Authority, success, trustworthiness, premium
Execution: High-end commercial advertising, Forbes cover quality

[QUALITY]
Resolution: 8K hyperdetailed, magazine print quality
Camera: Canon EOS R5, 85mm f/1.2L, shot at f/2.8
Post-Processing: Subtle dodge/burn, clean skin retouch, color graded
```

---

## Semantic Negative Prompting

### Instead of "no X", describe the positive alternative:

| Bad Negative | Good Semantic Alternative |
|--------------|---------------------------|
| "no cars" | "empty, deserted street with clear pavement" |
| "no people" | "solitary product in pristine empty studio" |
| "no text" | "clean uncluttered background without graphics" |
| "no blur" | "tack-sharp focus throughout, high clarity" |
| "no wrinkles" | "smooth, pressed, freshly tailored garment" |

### Effective Negative Prompt Structure

```
negativePrompt: "text, words, letters, watermark, logo,
signature, amateur photography, smartphone quality,
harsh direct flash, unflattering angles, cluttered
background, distracting elements, oversaturated colors,
HDR artifacts, chromatic aberration, noise, grain,
compression artifacts, stock photo aesthetic"
```

---

## Professional Photography Terms for Prompts

### Lighting Setups
- **Rembrandt lighting**: Triangle of light on cheek
- **Butterfly lighting**: Shadow under nose, glamour
- **Split lighting**: Half face lit, dramatic
- **Loop lighting**: Small shadow from nose, flattering
- **Broad lighting**: Lit side toward camera
- **Short lighting**: Shadow side toward camera

### Camera/Lens References
- **85mm f/1.4**: Portrait, shallow DOF
- **35mm f/1.4**: Environmental portrait
- **50mm f/1.2**: Natural perspective
- **70-200mm f/2.8**: Compressed background
- **24mm f/1.4**: Wide environmental

### Quality Descriptors
- "8K hyperdetailed texture"
- "razor-sharp focus"
- "professional color grading"
- "magazine print quality"
- "commercial catalog standard"
- "studio-controlled lighting"
- "subtle skin texture preserved"

---

## API Response Handling

### Full Response Structure

```json
{
  "predictions": [
    {
      "bytesBase64Encoded": "iVBORw0KGgo...",
      "mimeType": "image/png",
      "prompt": "Enhanced prompt if enhancePrompt=true",
      "raiFilteredReason": "null or reason if blocked",
      "safetyAttributes": {
        "categories": ["Adult", "Violence", "Medical"],
        "scores": [0.1, 0.0, 0.0]
      }
    }
  ],
  "modelVersion": "imagen-4.0-generate-001"
}
```

### Python Decoding

```python
import base64
from PIL import Image
from io import BytesIO

# From Vertex AI response
for prediction in response.predictions:
    image_bytes = base64.b64decode(prediction["bytesBase64Encoded"])
    image = Image.open(BytesIO(image_bytes))
    image.save(f"output_{index}.png")

# From Gemini SDK response
for part in response.candidates[0].content.parts:
    if part.inline_data:
        image_bytes = part.inline_data.data
        image = Image.open(BytesIO(image_bytes))
```

---

## Deterministic Generation (Seed Usage)

```json
{
  "parameters": {
    "seed": 42,
    "addWatermark": false,
    "enhancePrompt": false
  }
}
```

**Requirements:**
- `addWatermark` must be `false`
- `enhancePrompt` should be `false` for true determinism
- Same seed + same prompt = identical output

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Safety filter blocking | Lower `safetySetting` to `"block_only_high"` |
| Inconsistent results | Disable `enhancePrompt`, use explicit prompts |
| Text rendering poor | Use Gemini 3 Pro Image, explicit font descriptions |
| Character drift in multi-turn | Pass `thought_signature` between requests |
| Complex prompt ignored (Fast model) | Set `enhancePrompt: false` |
| Faces blocked | Check `personGeneration` setting |

---

## Sources

- [Gemini Image Generation API](https://ai.google.dev/gemini-api/docs/image-generation)
- [Imagen API Reference (Vertex AI)](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api)
- [Gemini 3 Pro Image (Nano Banana Pro)](https://deepmind.google/models/gemini-image/pro/)
- [Google Developers Blog - Prompting Best Practices](https://developers.googleblog.com/en/how-to-prompt-gemini-2-5-flash-image-generation-for-the-best-results/)
- [Prompting Strategies - Google AI](https://ai.google.dev/gemini-api/docs/prompting-strategies)
