# Visual Design System for Viral Carousels

Complete design specifications for creating high-retention carousel content. Covers typography, color psychology, layout patterns, visual devices, platform safe zones, and the Squint Test.

---

## Table of Contents

1. [Non-Negotiable Design Rules](#non-negotiable-design-rules) (Lines 15-50)
2. [The Squint Test](#the-squint-test) (Lines 55-65)
3. [Typography System](#typography-system) (Lines 70-155)
4. [Color Psychology](#color-psychology) (Lines 160-240)
5. [Layout Patterns](#layout-patterns) (Lines 245-330)
6. [Visual Devices and Graphic Elements](#visual-devices) (Lines 335-400)
7. [Platform Technical Specifications](#platform-specs) (Lines 405-470)
8. [Common Design Mistakes](#common-design-mistakes) (Lines 475-510)
9. [Algorithm Signals and Metrics](#algorithm-signals) (Lines 515-580)

---

## Non-Negotiable Design Rules

| Rule | Specification | Why |
|------|--------------|-----|
| **Hook Text Size** | 70-100pt minimum for slide 1 headline | Tiny text gets ignored at scroll speed. Must be readable in 0.5 seconds. |
| **Word Count (Slide 1)** | Max 12 words (ideal: 8-10) | Forces clarity. If it requires zooming, viewer is gone. |
| **Contrast Ratio** | Minimum 4.5:1 text-to-background (WCAG AA) | Readable in dark mode, bright sunlight, and small screens. |
| **Safe Zone (TikTok)** | Text only in center 1080x1520px area | Top 150px and bottom 250px covered by UI overlays. |
| **Safe Zone (Instagram)** | Keep important text in top 60% | Bottom third partially covered by profile pic, like bar, caption preview. |
| **Swipe Indicator** | Subtle arrow, dots, or "Swipe" in bottom area | Increases swipe-through rate by 15-30%. |
| **Read Time Per Slide** | Under 5 seconds for body; under 0.7 seconds for hook | If the brain has to work to decode the slide, the viewer moves on. |
| **Brand Identifier** | Small headshot + name on every slide (consistent position) | Builds recognition across feed appearances. Top-left corner recommended. |
| **Font Stack** | Maximum 2 fonts: one bold display + one clean body | More than 2 = visual noise. |
| **Color Palette** | Max 3 colors across entire carousel | Cohesion signals professionalism. More colors = amateur signal. |
| **White Space Ratio** | 60% empty space / 40% content per slide | Clean slides outperform cluttered slides every time. |

---

## The Squint Test

Squint your eyes and look at the first slide. If you cannot instantly read the hook, the design fails.

This simulates real-world thumb scrolling speed where the brain processes visual information in milliseconds. The audience decides in under 0.7 seconds whether to stop or keep scrolling.

Apply the Squint Test to every slide 1 before publishing. If you have to think about what it says, rewrite or redesign.

---

## Typography System

Typography is the single most important design element for text-heavy carousel content. It replaces photography as the primary visual.

### Font Size Hierarchy

| Element | Minimum | Recommended | Notes |
|---------|---------|-------------|-------|
| **Slide 1 Headline** | 70pt | 85-100pt | This is the hook. It must dominate the slide. |
| **Body Slide Headlines** | 36pt | 40-50pt | Main point per slide. Bold weight. |
| **Supporting Text** | 24pt | 26-30pt | Secondary information. Regular or light weight. |
| **Captions / Source Text** | 16pt | 18-20pt | Fine print, attributions, meta text. |
| **CTA Text** | 30pt | 36-44pt | Must be prominent. Often in accent color. |

### Font Pairing Strategy

Two dominant patterns in high-performing carousels:

**Option A: Bold Serif + Clean Sans-Serif**
- Headline: Bold serif (Playfair Display, DM Serif) creates authority and gravitas
- Body: Clean sans-serif (Inter, Montserrat, Helvetica) for readability
- Best for: Premium positioning, coaching, thought leadership

**Option B: Heavy Sans-Serif + Light Sans-Serif**
- Headline: Extra Bold sans-serif (Montserrat Bold, Inter Black)
- Body: Regular weight of the same family or complementary sans
- Best for: Modern, clean, Instagram-native aesthetic

### Font Weight as Visual Hierarchy

Font weight does more work than font size in most carousel designs:

- **Black/ExtraBold (800-900):** Hook headlines only. One per slide maximum.
- **Bold (700):** Key phrases, stats, or the single takeaway on a slide.
- **SemiBold (600):** Subheadings, labels, category markers.
- **Regular (400):** Body text, explanations, supporting context.
- **Light (300):** Fine print, disclaimers, source citations.

Varying weight within a single slide creates natural reading flow without needing multiple font sizes.

### The ALL CAPS Rule

Avoid formatting blocks of text in ALL CAPS. The brain reads by recognizing word shapes (silhouettes), not individual letters. The variance between ascending letters (d, h, k, l), descending letters (g, y, p, q), and short letters (a, e, n, s) creates distinct word silhouettes. ALL CAPS homogenizes these shapes into uniform rectangular blocks, destroying the silhouette and slowing reading speed significantly.

ALL CAPS is acceptable only for: single-word labels ("MYTH:", "STEP 1"), short emphasis phrases (3 words max), or brand names. Never for headlines or body text.

### Letter Spacing and Line Height

- **Headlines:** Tight letter spacing (-0.5 to -1%). Tight tracking on large text creates visual density and impact.
- **Body text:** Normal or slightly loose (+0.5%). Improves readability on mobile.
- **Line height for headlines:** 1.0 to 1.1x font size (tight). Keeps multi-line headlines compact.
- **Line height for body text:** 1.4 to 1.6x font size (generous). Prevents wall-of-text feeling.

---

## Color Psychology

Color triggers subconscious reactions before conscious reading. The right palette creates emotional context before the viewer processes a single word.

### Color Associations for Business/Coaching Carousels

| Color | Psychological Trigger | Best Use Case |
|-------|----------------------|---------------|
| **Black / Obsidian** | Authority, sophistication, power | Backgrounds for premium positioning |
| **White** | Clarity, cleanliness, trust | Text-first slides, clean information delivery |
| **Gold / Amber** | Success, premium quality, achievement | Accent for stats, CTAs, highlighted phrases |
| **Red / Deep Crimson** | Urgency, passion, importance | CTA slides, warning/mistake hooks |
| **Teal / Mint** | Freshness, differentiation, approachability | Accent color, stands out against black/white |
| **Navy / Dark Blue** | Trust, stability, professionalism | Alternative to black for less intense premium feel |
| **Orange / Marigold** | Optimism, energy, creativity | Educational content, transformation moments |

### The Two Dominant Color Strategies

**Strategy 1: Light Background (Most Common in Coaching)**
- Background: White or off-white (#FFFFFF or #F5F5F0)
- Primary text: Black or near-black (#1A1A1A or #0B0B0F)
- Accent: One bold color for highlights, underlines, callouts
- Works because it looks like a professional presentation, not an ad.

**Strategy 2: Dark Background (Brand Differentiation)**
- Background: Obsidian (#050505 or #0B0B0F)
- Primary text: White (#FFFFFF)
- Accent: Gold gradient (#FFD700 → #FFA500 → #FF4500) or single gold (#D4A843)
- Dark carousels stand out in feeds dominated by white backgrounds. Every slide becomes a branded touchpoint.

### Color Progression Across Slides

Smart creators use subtle color shifts to create visual momentum:
- Start with neutral/calm backgrounds for the hook (let the words do the work)
- Introduce accent colors progressively as content builds
- Use the boldest color treatment on the CTA slide
- Creates a visual "crescendo" that mirrors the narrative arc

---

## Layout Patterns

### Eye-Scanning Patterns

- **Z-Pattern:** Top-left → top-right → diagonal → bottom-left → bottom-right. Best for slides with minimal text and clear CTA. Place headline top-left, visual element top-right, supporting text bottom-left, CTA/arrow bottom-right.
- **F-Pattern:** Left-aligned scanning: across the top, then down the left side. Best for text-heavy educational slides.

### Three Layout Templates

**Template 1: Centered Statement**
- Large headline centered vertically
- One or two lines of supporting text below
- Brand identifier in top-left corner
- Swipe indicator in bottom area
- **Use on:** Hook slides, contrarian takes, bold claims

**Template 2: Progressive List**
- Headline at top
- Numbered or bulleted items stacked vertically with accent elements (colored dots, icons, numbered badges)
- Each item in its own "card" or "bubble" visual container
- **Use on:** Step-by-step slides, listicles, mistake breakdowns

**Template 3: Split Frame**
- Left side: Bold text headline or statistic
- Right side: Supporting image, icon, or graphic element
- Or: Top 60% text, bottom 40% visual proof
- **Use on:** Proof slides, data slides, before/after comparisons

### Visual Flow Between Slides

A carousel is not a collection of independent slides. It must feel like a continuous experience:

- **Consistent margins and padding** across all slides (same text position, same spacing)
- **Repeating accent element** in the same position on every slide (colored bar, numbered badge, icon)
- **Progressive numbering or labeling** that signals progress ("Step 1 of 5," page dots)
- **Visual cues that pull forward:** partial text cut off at right edge, arrows pointing right, "continued" indicators
- **Alternating layouts** to prevent monotony: statement → list → proof → statement

---

## Visual Devices and Graphic Elements

### Elements That Increase Engagement

| Element | Purpose | Execution |
|---------|---------|-----------|
| **Highlight / Underline** | Draws attention to key phrase | Colored bar behind text or hand-drawn underline effect |
| **Numbered Badges** | Signals structured content, progress | Colored circle with number. Same position each slide. |
| **Bubble / Card Containers** | Groups related items, creates visual separation | Rounded rectangle with subtle border or shadow. |
| **Progress Dots** | Shows position within carousel, encourages completion | Small colored dots at bottom. Active dot filled, others outlined. |
| **Directional Arrows** | Explicit swipe signal | Subtle arrow in bottom-right or embedded in CTA. |
| **Creator Headshot** | Builds trust and recognition | Small circular photo. Top-left or bottom-left. Same position every slide. |
| **Icon / Emoji Accent** | Adds visual interest to text-heavy slides | One icon per slide maximum. Must reinforce the point. |
| **Pull Quotes / Stat Callouts** | Highlights most important number or phrase | Larger size, different color, or enclosed in visual container. |
| **Gradient Text** | Premium feel on dark backgrounds | Apply gradient to headline text only. |
| **Subtle Background Texture** | Prevents flat/sterile feeling | Very light noise, grain, or paper texture at 5-10% opacity. |

### Elements to Avoid

- Stock photos that feel generic (kills credibility)
- More than 2 emojis per slide (looks spammy)
- Drop shadows on text (2015 aesthetic)
- Gradients as backgrounds (gradient text = good, gradient background = amateur)
- Busy patterns or textures competing with text
- Clip art or low-quality icons (use Lucide, Phosphor, or Heroicons)
- Borders around every element (over-containing creates clutter)

---

## Platform Technical Specifications

### TikTok Photo Mode

| Spec | Details |
|------|---------|
| **Dimensions** | 1080 x 1920 pixels (9:16 vertical) |
| **Min/Max Images** | 2 minimum, 35 maximum |
| **Optimal Slide Count** | 5-10 for engagement; 4-8 for completion |
| **Format** | JPEG or PNG (high quality; TikTok compresses) |
| **Audio** | Add trending sound for discovery boost |
| **Upload Method** | Native Photo Mode (not video slideshow) |
| **Text Indexing** | TikTok OCR indexes text on slides for search |
| **Alt Text** | Use for keyword-rich descriptions (accessibility + SEO) |
| **Post-Publish Editing** | Not possible. Finalize before publishing. |

**Production note:** Always design externally (Canva, Figma) for maximum control, then upload as individual images. External graphics consistently outperform TikTok's native text editor.

### Precise TikTok Safe Zones

The full canvas is 1080x1920, but UI overlays consume significant area:

| UI Element | Pixel Intrusion | Action |
|------------|----------------|--------|
| **Top Band** (username, sound label) | Top 150-250px | No text. Collision with handle and audio title. |
| **Right Edge** (like, comment, share icons) | Right 120px | No text or focal imagery. Primary interaction zone. |
| **Bottom Area** (caption, CTA, progress dots) | Bottom 350-480px | No text. Dynamic, expands with caption length. |
| **Left Edge** (padding) | Left 120px | Avoid edge-to-edge text for clean aesthetic. |
| **Optimal Safe Zone** | **840 x 1280 pixels (centered)** | **ALL critical text, images, and CTAs must fit within this box.** |

The 840x1280 safe zone is the true design canvas. Anything outside it risks being covered by UI elements on different device sizes.

### Audio Strategy for Carousels

TikTok is a sound-on environment. Neglecting audio is a massive missed opportunity for reach. Posts with background music receive 98%+ more views than silent posts.

**Trending Audio:** Syncing to a rising audio track signals trend participation. The algorithm provides visibility boost to content using trending sounds. Users actively search for content associated with popular sounds.

**Mood Matching:**
- High-tension myth-busting hooks → driving, percussive beats
- Educational list-based carousels → ambient, lo-fi music (lowers cognitive anxiety, encourages dwelling on text)
- Story arc / transformation → emotional, building instrumentals

**Voiceover Integration:** Photo Mode supports voiceovers recorded over the image sequence. Narrating slide text creates a dual-sensory experience. Retains users who prefer auditory processing, stacks dwell time metrics, ensures message absorption even without active reading.

### OCR Text Indexing and TikTok SEO

TikTok uses Optical Character Recognition to literally read text on carousel images. The algorithm extracts keywords from slide text to categorize and surface posts in search results.

**SEO Integration Points:**
1. **Text on slides:** Visible, high-contrast keywords embedded in typography
2. **Post caption:** Keywords the target audience actually searches
3. **Alt text:** Keyword-rich descriptions for each image (accessibility + SEO)
4. **Hashtags:** Mix broad, niche, and trending
5. **SEO video title:** Additional semantic data for algorithm categorization

Every carousel becomes a search-rankable asset. Design with search intent, not just feed browsing.

### Engineering Reverse Swipes

Reverse swipes (swiping backward to re-read a previous slide) are one of the strongest positive signals for carousel distribution. The algorithm interprets this as: content so dense and valuable it demands secondary processing.

**Tactics to engineer reverse swipes:**
- Include highly technical list-based slides that reward re-reading
- Reference earlier slide content on later slides ("Remember the formula from Step 2?")
- Add subtle visual details or data points that users notice on second viewing
- Use text overlays: "Wait — swipe back if you missed the core formula on Step 2"
- Create progressive frameworks where later steps build on earlier ones

This directly instructs the user to feed the algorithm the exact positive signal it seeks.

### Instagram Carousel

| Spec | Details |
|------|---------|
| **Dimensions** | 1080 x 1350 (4:5) recommended; 1080 x 1080 (1:1) also works |
| **Max Images** | Up to 20 per carousel |
| **Optimal Slide Count** | 5-8 slides |
| **Re-Serving** | Instagram re-shows carousels starting from later slides |
| **Safe Zone** | Keep important text in top 60% of image |

### Cross-Posting Workflow

1. Design at 1080x1920 for TikTok first (most restrictive safe zones)
2. Adjust to 1080x1350 for Instagram (reposition text within safe zones)
3. Adapt caption for each platform's search behavior
4. Use platform-native posting for each (no scheduling tools that strip quality)

### TikTok SEO for Carousels

TikTok functions as a search engine. The algorithm scans three text sources:

1. **Post Caption:** Include keywords your target audience searches
2. **Text On Images:** Text overlays on slides are indexed. Clear, readable fonts with strategic keyword placement.
3. **Hashtags:** Mix broad, niche, and trending

### Algorithm Distribution Waves (TikTok)

1. **Small batch test:** Shows to 200-500 people (mostly followers and similar-content engagers)
2. **Signal collection:** Watches four key signals (STR, dwell time, reverse swipes, completion rate)
3. **Decision point:** Strong signals = push to larger group. Weak = distribution stops.
4. **Expanding waves:** Each wave larger than the last, as long as engagement holds.

Some carousels take off hours after posting because they pass wave after wave of algorithmic testing.

---

## Common Design Mistakes

These are the most frequent issues that reduce carousel performance:

1. **Cramped layouts** with insufficient white space. Slides should breathe.
2. **Too much text per slide.** One idea per slide. If it reads like a paragraph, split it.
3. **Low contrast** between text and background. Test on a phone at arm's length.
4. **Multiple competing focal points.** One primary element per slide.
5. **Overuse of decorative fonts** for body copy. Harder to read at small sizes. Limit script fonts to small accent words.
6. **Inconsistent filters, fonts, and aspect ratios.** Creates jarring experience. Use templates.
7. **Poor image quality.** Blurry or low-resolution uploads harm credibility, especially full-screen on TikTok.
8. **Ignoring safe zones.** Text hidden behind UI overlays is wasted effort.
9. **No swipe indicator.** Viewers may not realize there are more slides. Always include visual cue.
10. **Overloading the CTA slide.** One action, not three. Clear, large, unmissable.

---

## Algorithm Signals and Metrics

### The Four Signals That Determine Distribution

| Signal | What It Measures | Target |
|--------|-----------------|--------|
| **Swipe-Through Rate (STR)** | % of viewers who swipe past slide 1 | 60%+ |
| **Dwell Time Per Slide** | Seconds spent on each slide | 3-5 seconds |
| **Reverse Swipes** | Viewers swiping backward to re-read | Any occurrence is a strong positive signal |
| **Completion Rate** | % of viewers who reach the last slide | 70%+ |

### Additional High-Value Signals

- **Saves:** Strongest quality signal in 2026. Design for save-worthy content.
- **Shares:** Fastest path to viral distribution. Each share introduces content to a new audience.
- **Comments:** Debate-style comments > compliments. Questions and contrarian hooks drive highest volume.
- **Reverse Swipe Rate:** Content so valuable viewers go back to re-read. Excellent signal.

### Performance Data Points

| Metric | Data Point | Source |
|--------|-----------|--------|
| TikTok carousels vs video | 81% more engagement | StackInfluence 2025 |
| TikTok carousel comments vs video | 2.9x more | TikTok internal data |
| TikTok carousel likes vs video | 1.9x more | TikTok internal data |
| Instagram carousel reach vs single images | 1.9x higher | Hootsuite + Later 2025 |
| Instagram carousel engagement vs other formats | 3x more | Hootsuite Digital Trends 2025 |
| High-swipe carousels non-follower distribution | 3-5x more | Meta 2024 internal report |
| Swipe indicator impact on STR | 15-30% increase | Later 2025 study |

### Tracking Protocol

Track performance by:
- Hook type (which patterns produce highest STR)
- Content topic (which subjects drive most saves)
- Slide count (optimal length for your audience)
- Design style (dark vs light, serif vs sans)
- Posting time (platform-specific windows)

Repeated testing over 4-8 weeks refines intuition about what produces viral or high-view posts for a specific audience.

### Design Tools

| Tool | Best For |
|------|----------|
| **Canva** | Fast production, templates, brand kit management |
| **Figma** | Precise layout control, multi-slide overview, collaboration |
| **Adobe Illustrator** | Custom graphics, premium icon work |
| **Gemini / AI Image Gen** | Background images, lifestyle imagery (overlay text in Canva) |
| **PostNitro / aiCarousels** | AI-assisted rapid drafts (always refine manually) |
