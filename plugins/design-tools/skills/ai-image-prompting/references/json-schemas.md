# API JSON Schemas Reference

## Gemini Imagen 4.0

### Python SDK Request
```python
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_images(
    model='imagen-4.0-generate-001',
    prompt='Your prompt here',
    config=types.GenerateImagesConfig(
        number_of_images=1,      # 1-4 images
        aspect_ratio='9:16',      # Options below
        output_mime_type='image/png',  # or 'image/jpeg'
        # safety_filter_level='BLOCK_MEDIUM_AND_ABOVE'
    )
)

# Access images
for image in response.generated_images:
    image.image.show()  # Display
    image.image.save('output.png')  # Save
```

### Aspect Ratios
| Ratio | Use Case |
|-------|----------|
| `1:1` | Feed square, carousel |
| `3:4` | Portrait general |
| `4:3` | Landscape general |
| `4:5` | Feed portrait (Instagram style) |
| `9:16` | Stories, Reels, vertical |
| `16:9` | Landscape, video covers |

### Config Parameters
| Parameter | Type | Values | Default |
|-----------|------|--------|---------|
| number_of_images | int | 1-4 | 4 |
| aspect_ratio | string | See above | "1:1" |
| output_mime_type | string | "image/png", "image/jpeg" | "image/png" |
| safety_filter_level | string | BLOCK_NONE, BLOCK_LOW_AND_ABOVE, BLOCK_MEDIUM_AND_ABOVE, BLOCK_HIGH | BLOCK_MEDIUM_AND_ABOVE |

---

## Ideogram API

### REST Request
```json
POST https://api.ideogram.ai/generate

{
  "image_request": {
    "prompt": "Your detailed prompt here",
    "model": "V_2",
    "magic_prompt_option": "AUTO",
    "aspect_ratio": "ASPECT_9_16",
    "style_type": "REALISTIC",
    "rendering_speed": "BALANCED"
  }
}
```

### Headers
```
Api-Key: your-api-key
Content-Type: application/json
```

### Parameters
| Parameter | Values |
|-----------|--------|
| model | "V_1", "V_1_TURBO", "V_2", "V_2_TURBO" |
| magic_prompt_option | "AUTO", "ON", "OFF" |
| aspect_ratio | "ASPECT_1_1", "ASPECT_4_3", "ASPECT_3_4", "ASPECT_16_9", "ASPECT_9_16", "ASPECT_3_2", "ASPECT_2_3" |
| style_type | "REALISTIC", "DESIGN", "RENDER_3D", "ANIME", "GENERAL", "AUTO" |
| rendering_speed | "TURBO", "BALANCED", "QUALITY" |

### Response
```json
{
  "created": "2024-01-01T00:00:00Z",
  "data": [
    {
      "url": "https://...",
      "prompt": "final prompt used",
      "is_image_safe": true,
      "seed": 12345
    }
  ]
}
```

---

## DALL-E 3 (OpenAI)

### REST Request
```json
POST https://api.openai.com/v1/images/generations

{
  "model": "dall-e-3",
  "prompt": "Your detailed prompt here",
  "n": 1,
  "size": "1024x1792",
  "quality": "hd",
  "style": "vivid"
}
```

### Parameters
| Parameter | Values | Notes |
|-----------|--------|-------|
| size | "1024x1024", "1024x1792", "1792x1024" | Only these 3 |
| quality | "standard", "hd" | HD = more detail |
| style | "vivid", "natural" | Vivid = more dramatic |
| n | 1 | Only 1 for DALL-E 3 |

### Size Mapping
| Size | Use Case |
|------|----------|
| 1024×1024 | Feed square |
| 1024×1792 | Stories/Reels (closest to 9:16) |
| 1792×1024 | Landscape |

---

## Midjourney (Discord/API)

### Discord Command Format
```
/imagine prompt: [your prompt] --ar 9:16 --s 750 --q 2 --v 6
```

### Parameter Reference
| Parameter | Format | Range | Description |
|-----------|--------|-------|-------------|
| --ar | W:H | Any ratio | Aspect ratio |
| --s | 0-1000 | 0-1000 | Stylization |
| --q | 0.25-2 | 0.25, 0.5, 1, 2 | Quality |
| --chaos | 0-100 | 0-100 | Variation |
| --no | text | Any | Negative prompt |
| --v | 5, 5.1, 5.2, 6 | Version | Model version |
| --style | raw | raw | Less stylized |

### Multi-Prompt Syntax
```
subject one::2 subject two::1 background::0.5 --ar 9:16
```
- `::` separates prompt segments
- `::N` sets weight (default 1)
- `::−0.5` negative weight

---

## Stable Diffusion (AUTOMATIC1111 API)

### txt2img Request
```json
POST /sdapi/v1/txt2img

{
  "prompt": "(professional advertisement:1.4), your prompt here",
  "negative_prompt": "(text:1.4), (watermark:1.4), low quality",
  "steps": 35,
  "cfg_scale": 7.5,
  "width": 768,
  "height": 1344,
  "sampler_name": "DPM++ 2M Karras",
  "seed": -1,
  "batch_size": 1
}
```

### Weight Syntax in Prompt
```
(word:1.5)     # Explicit weight 0.1-2.0
(word)         # 1.1x weight
((word))       # 1.21x weight
[word]         # 0.9x weight
[[word]]       # 0.81x weight
```

### Recommended Settings
| Setting | Value | Notes |
|---------|-------|-------|
| steps | 30-50 | Higher = more detail |
| cfg_scale | 7-9 | Prompt adherence |
| sampler | DPM++ 2M Karras | Best quality |
| width×height | 768×1344 | 9:16 for SDXL |

---

## FLUX.1 (Replicate/BFL API)

### Replicate Request
```json
POST https://api.replicate.com/v1/predictions

{
  "version": "flux-1.1-pro",
  "input": {
    "prompt": "Your natural language prompt",
    "aspect_ratio": "9:16",
    "output_format": "png",
    "safety_tolerance": 2,
    "prompt_upsampling": true
  }
}
```

### Parameters
| Parameter | Values |
|-----------|--------|
| aspect_ratio | "1:1", "16:9", "21:9", "2:3", "3:2", "4:5", "5:4", "9:16", "9:21" |
| output_format | "png", "jpg", "webp" |
| safety_tolerance | 1-5 (higher = more permissive) |
| prompt_upsampling | true/false (enhance prompt) |

### BFL API Direct
```json
POST https://api.bfl.ml/v1/flux-pro-1.1

{
  "prompt": "Your prompt",
  "width": 768,
  "height": 1344,
  "steps": 30,
  "guidance": 3.5,
  "seed": -1
}
```

---

## Quick Reference: Ad Dimensions

| Platform | Format | Pixels | API Aspect |
|----------|--------|--------|------------|
| FB Feed Square | 1:1 | 1080×1080 | "1:1" |
| FB Feed Portrait | 4:5 | 1080×1350 | "4:5" |
| FB/IG Stories | 9:16 | 1080×1920 | "9:16" |
| FB Carousel | 1:1 | 1080×1080 | "1:1" |
| FB Right Column | 1.91:1 | 1200×628 | "16:9" (closest) |
