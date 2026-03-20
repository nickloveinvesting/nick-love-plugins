# Social Media Design Deep Dive

This reference provides comprehensive guidance for creating high-performing social media content via Canva MCP tools.

## Platform-Specific Design Types

| Platform | Design Type | Dimensions | Best For |
|----------|-------------|------------|----------|
| Instagram Feed | `instagram_post` | 1080×1080 | Quotes, announcements, carousels |
| Instagram Story | `your_story` | 1080×1920 | Behind-scenes, polls, urgency |
| Facebook Feed | `facebook_post` | 1200×630 | Links, events, long-form |
| Facebook Cover | `facebook_cover` | 820×312 | Brand presence |
| Twitter/X | `twitter_post` | 1600×900 | News, threads, engagement |
| YouTube Thumbnail | `youtube_thumbnail` | 1280×720 | Video click-through |
| YouTube Banner | `youtube_banner` | 2560×1440 | Channel branding |
| Pinterest | `pinterest_pin` | 1000×1500 | Tutorials, infographics |
| LinkedIn Cover | Use `facebook_cover` | 1584×396 | Professional branding |

## Query Structure for Social Media

### Essential Elements

```
Create a [design_type] for [platform].

AUDIENCE: [Who will see this - age, interests, pain points]
PURPOSE: [Awareness / Engagement / Conversion / Education]
TONE: [Professional / Casual / Urgent / Inspirational / Playful]

CONTENT:
- Headline: "[Exact headline text - max 6-8 words]"
- Subtext: "[Supporting text - 1-2 lines]"
- CTA: "[Call to action - button or text]"

VISUAL STYLE:
- Colors: [Specific colors or "match brand kit"]
- Imagery: [Photo style, illustration, abstract, etc.]
- Layout: [Text placement - left/center/overlay]

AVOID: [What NOT to include - busy backgrounds, small text, etc.]
```

### Platform-Specific Additions

**Instagram Post:**
```
HASHTAG STRATEGY: [3-5 relevant hashtags to inform design theme]
CAROUSEL: [If multi-image, specify slide count and flow]
FEED AESTHETIC: [How this fits with overall feed look]
```

**YouTube Thumbnail:**
```
VIDEO TOPIC: [What the video covers]
EMOTION: [Curiosity / Shock / Excitement / Trust]
FACE: [Include face? Expression if yes]
TEXT PLACEMENT: [Avoid YouTube timestamp area - bottom right]
```

**Story:**
```
INTERACTIVITY: [Poll / Quiz / Swipe-up hint / Countdown]
SEQUENCE: [If multi-story, specify flow]
TAP ZONES: [Clickable areas consideration]
```

## High-Converting Query Examples

### Instagram Announcement Post

```
Create an instagram_post for a webinar announcement.

AUDIENCE: Aspiring real estate investors, 25-45, frustrated with 9-5, seeking passive income
PURPOSE: Drive webinar registrations (conversion)
TONE: Professional but exciting, creates urgency

CONTENT:
- Headline: "FREE LIVE TRAINING"
- Subtext: "How to Buy Your First Rental Property in 90 Days (Even with No Experience)"
- CTA: "Save Your Spot 👇 Link in Bio"
- Date/Time: "Jan 15 @ 7PM CST"

VISUAL STYLE:
- Colors: Dark navy background, gold accents, white text
- Imagery: Clean, minimal - maybe subtle property silhouette
- Layout: Headline top, details center, CTA bottom

AVOID: Cluttered design, more than 3 font sizes, hard-to-read cursive
```

### YouTube Thumbnail

```
Create a youtube_thumbnail for educational content.

VIDEO TOPIC: "5 Mistakes That Keep You Poor (And How to Fix Them)"
AUDIENCE: Young professionals interested in personal finance

EMOTION: Curiosity + slight shock
FACE: Yes - surprised/concerned expression looking at "mistakes"
TEXT: 
- Main: "5 MONEY MISTAKES" (large, bold)
- Accent: "that keep you BROKE" (smaller, different color)

VISUAL STYLE:
- High contrast colors (red/yellow attention-grabbing)
- Person on left 1/3, text on right 2/3
- Number "5" should be prominent

AVOID: 
- Text in bottom-right (YouTube timestamp area)
- More than 5 words visible
- Busy background competing with face
```

### Facebook Event Cover

```
Create a facebook_cover for upcoming conference.

EVENT: Limitless Real Estate Conference 2026
AUDIENCE: Active real estate investors, professionals, 30-55

CONTENT:
- Event name: "LIMITLESS 2026"
- Tagline: "Where Investors Become Legends"
- Date: "March 15-17, 2026 | Dallas, TX"

VISUAL STYLE:
- Premium, conference feel - think TED Talk quality
- Dark background with spotlight effect
- Gold/bronze metallic accents
- Modern sans-serif typography

ELEMENTS TO INCLUDE:
- Subtle cityscape silhouette (Dallas skyline)
- Conference logo if available via brand kit

AVOID: Cheap stock photo look, too many speakers faces, cluttered text
```

## Design Psychology by Platform

### Instagram
- **Scroll-stopping**: First 0.5 seconds decide engagement
- **Pattern interrupt**: Bold colors or unexpected visuals
- **Text hierarchy**: Max 3 levels (headline, body, CTA)
- **Thumb zone**: Key info in center 80% of frame

### YouTube Thumbnails
- **Curiosity gap**: Promise value, don't reveal everything
- **Faces convert**: Human faces get 38% more clicks
- **Contrast is king**: Should be readable at 100px width
- **Complement title**: Don't repeat video title exactly

### Stories
- **Vertical real estate**: Use full 9:16 frame
- **Tap-through rate**: First frame determines if they continue
- **Native feel**: Overly polished can feel like ads (lower engagement)
- **Interactive elements**: Polls increase engagement 40%+

### Pinterest
- **Long-form**: Vertical pins outperform square
- **Text overlay**: Must be readable without clicking
- **How-to format**: Tutorial pins save 3x more
- **Fresh content**: Repin rate drops after 4 months

## Brand Consistency Workflow

```
1. list-brand-kits()
2. Select appropriate brand kit ID
3. Include in generate-design:
   - brand_kit_id: "kAFrPxMDrlE"
4. Query should reference brand elements:
   "Use brand colors and fonts for professional consistency"
5. Review generated options for brand alignment
```

## Batch Content Creation Pattern

For creating cohesive content series:

```
1. Create folder for campaign:
   create-folder("January 2026 Campaign")

2. Generate series with consistent query elements:
   - Same brand_kit_id
   - Same visual style description
   - Sequential content themes

3. For each design:
   - generate-design() with series-aware query
   - create-design-from-candidate()
   - move-item-to-folder()

4. Export batch:
   For each design_id:
   - export-design(format={type:"png", export_quality:"pro"})
```

## Content Calendar Integration

Suggested weekly posting structure with design types:

| Day | Platform | Design Type | Content Focus |
|-----|----------|-------------|---------------|
| Mon | Instagram | `instagram_post` | Motivation/Quote |
| Tue | YouTube | `youtube_thumbnail` | New video |
| Wed | Instagram | `your_story` | Behind-scenes |
| Thu | Facebook | `facebook_post` | Educational |
| Fri | Instagram | `instagram_post` | Success story |
| Sat | Pinterest | `pinterest_pin` | How-to/Tutorial |
| Sun | Instagram | `your_story` | Week recap/preview |

## Performance Optimization Tips

1. **A/B Testing**: Generate multiple versions with slight variations
2. **Text Readability**: Ensure readable at mobile size (test by zooming out)
3. **CTA Placement**: Bottom third for feed posts, swipe-up zone for stories
4. **Whitespace**: Don't fill every pixel - let design breathe
5. **Consistent Branding**: Same colors/fonts build recognition over time
