# Platform Specifications for Ad Creatives

## Facebook/Meta Ad Dimensions

### Feed Placements

| Format | Dimensions | Aspect Ratio | Max File Size |
|--------|------------|--------------|---------------|
| Feed Square | 1080×1080 | 1:1 | 30MB |
| Feed Portrait | 1080×1350 | 4:5 | 30MB |
| Feed Landscape | 1200×628 | 1.91:1 | 30MB |
| Carousel | 1080×1080 | 1:1 | 30MB each |
| Collection | 1080×1080 | 1:1 | 30MB |

### Stories & Reels

| Format | Dimensions | Aspect Ratio | Duration |
|--------|------------|--------------|----------|
| Stories | 1080×1920 | 9:16 | 15 sec max |
| Reels | 1080×1920 | 9:16 | 90 sec max |
| In-Stream Video | 1080×1920 | 9:16 | 15 sec optimal |

### Other Placements

| Placement | Dimensions | Aspect Ratio |
|-----------|------------|--------------|
| Right Column | 1200×628 | 1.91:1 |
| Instant Article | 1200×628 | 1.91:1 |
| Marketplace | 1080×1080 | 1:1 |
| Search Results | 1080×1080 | 1:1 |

---

## Safe Zones (Critical)

### Stories/Reels (1080×1920)

```
┌─────────────────────────────┐
│                             │
│   TOP UNSAFE ZONE: 250px    │  ← Profile pic, name, time
│   (14% of height)           │
│                             │
├─────────────────────────────┤
│                             │
│                             │
│                             │
│     SAFE CONTENT ZONE       │
│     1420px height           │
│     (74% of height)         │
│                             │
│                             │
│                             │
├─────────────────────────────┤
│                             │
│  BOTTOM UNSAFE ZONE: 250px  │  ← CTA button, swipe up
│  (14% of height)            │
│                             │
└─────────────────────────────┘

Side margins: 72px each (7% width)
```

**Pixel-Perfect Safe Zone:**
- Top: y > 250px
- Bottom: y < 1670px
- Left: x > 72px
- Right: x < 1008px
- Safe area: 936px × 1420px centered

### Feed Portrait (1080×1350)

```
┌─────────────────────────────┐
│   TOP MARGIN: 90px (7%)     │
├─────────────────────────────┤
│                             │
│     SAFE CONTENT ZONE       │
│     1170px height           │
│     (86% of height)         │
│                             │
├─────────────────────────────┤
│  BOTTOM MARGIN: 90px (7%)   │
└─────────────────────────────┘

Side margins: 54px each (5% width)
```

### Feed Square (1080×1080)

```
┌─────────────────────────────┐
│   TOP MARGIN: 54px (5%)     │
├─────────────────────────────┤
│                             │
│     SAFE CONTENT ZONE       │
│     972px × 972px           │
│     (90% of dimensions)     │
│                             │
├─────────────────────────────┤
│  BOTTOM MARGIN: 54px (5%)   │
└─────────────────────────────┘
```

---

## Text Overlay Guidelines

### Facebook 20% Text Rule
- **No longer enforced** as hard rejection
- Algorithm may still reduce reach for heavy text
- Best practice: Keep text under 20% of image area

### Recommended Text Zones

**Stories/Reels:**
```
Headline Zone:
- Y position: 280-500px from top
- Width: 936px (with margins)
- Max height: 200px

CTA Zone:
- Y position: 1300-1550px from top
- Centered horizontally
- Max height: 150px
```

**Feed Portrait:**
```
Headline Zone:
- Y position: 120-400px
- Full width minus margins
- Max 2-3 lines

Value Props:
- Y position: 450-1000px
- Left-aligned with 60px margin

CTA Zone:
- Y position: 1050-1250px
- Centered or right-aligned
```

---

## Image Quality Requirements

### Resolution

| Minimum | Recommended | Maximum |
|---------|-------------|---------|
| 600×600 | 1080×1080+ | 2048×2048 |

### File Formats

| Format | Best For | Max Size |
|--------|----------|----------|
| JPG | Photos | 30MB |
| PNG | Graphics/Text | 30MB |
| GIF | Animations | 8MB |
| MP4 | Video | 4GB |

### Compression Guidelines
- JPEG quality: 80-90%
- PNG: Use PNG-8 for graphics, PNG-24 for photos with transparency
- Avoid artifacts in gradient areas

---

## Video Specifications

### Stories/Reels Video

| Spec | Requirement |
|------|-------------|
| Resolution | 1080×1920 (9:16) |
| Frame Rate | 30fps (recommended) |
| Codec | H.264 |
| Audio | AAC, 128kbps+ |
| Duration | 15-60 seconds |

### Feed Video

| Spec | Requirement |
|------|-------------|
| Resolution | 1080×1080 or 1080×1350 |
| Frame Rate | 30fps |
| Max Duration | 240 minutes |
| Optimal | 15-30 seconds |

---

## Instagram Specifications

### Feed

| Format | Dimensions | Ratio |
|--------|------------|-------|
| Square | 1080×1080 | 1:1 |
| Portrait | 1080×1350 | 4:5 |
| Landscape | 1080×608 | 1.91:1 |

### Stories/Reels
- Same as Facebook: 1080×1920 (9:16)
- Same safe zones apply

### Carousel
- Up to 10 images/videos
- Consistent aspect ratio required
- 1080×1080 recommended

---

## Cross-Platform Quick Reference

| Platform | Best Format | Dimensions |
|----------|-------------|------------|
| FB Feed | Portrait | 1080×1350 |
| FB Stories | Vertical | 1080×1920 |
| IG Feed | Square | 1080×1080 |
| IG Stories | Vertical | 1080×1920 |
| LinkedIn | Landscape | 1200×628 |
| Twitter | Landscape | 1200×675 |
| Pinterest | Vertical | 1000×1500 |

---

## AI Generation Target Sizes

### For Stories/Reels (9:16)

| Model | Setting | Output |
|-------|---------|--------|
| Gemini | aspect_ratio: "9:16" | 1024×1820 |
| DALL-E 3 | 1024x1792 | 1024×1792 |
| Midjourney | --ar 9:16 | ~1024×1820 |
| FLUX | aspect_ratio: "9:16" | 768×1344 |
| SD XL | 768×1344 | 768×1344 |

**Note:** Upscale AI output to 1080×1920 for final delivery

### For Feed Square (1:1)

| Model | Setting | Output |
|-------|---------|--------|
| Gemini | aspect_ratio: "1:1" | 1024×1024 |
| DALL-E 3 | 1024x1024 | 1024×1024 |
| Midjourney | --ar 1:1 | 1024×1024 |
| FLUX | aspect_ratio: "1:1" | 1024×1024 |
| SD XL | 1024×1024 | 1024×1024 |

### For Feed Portrait (4:5)

| Model | Setting | Output |
|-------|---------|--------|
| Gemini | aspect_ratio: "4:5" | ~1024×1280 |
| Midjourney | --ar 4:5 | ~1024×1280 |
| FLUX | aspect_ratio: "4:5" | ~1024×1280 |

---

## Prompt Template: Dimension Aware

```
[For Stories/Reels 9:16]
...composition optimized for vertical 9:16 format,
subject positioned in center-left of frame,
clear negative space in top 15% for UI overlay zones,
clear negative space in bottom 15% for CTA overlay zones,
primary content within central 70% vertical safe zone...

[For Feed Square 1:1]
...composition optimized for square 1:1 format,
balanced subject placement using rule of thirds,
5% margin safe zone around all edges,
centered focal point with supporting elements in quadrants...

[For Feed Portrait 4:5]
...composition optimized for portrait 4:5 format,
vertical emphasis with subject in upper two-thirds,
breathing room maintained at top and bottom 7%,
headline zone reserved in upper quarter...
```
