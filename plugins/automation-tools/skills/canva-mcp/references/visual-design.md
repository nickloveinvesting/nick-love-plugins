# Presentation Visual Design Reference

This reference teaches how to describe visual styles, layouts, colors, typography, and assets when prompting Canva presentation generation.

## Visual Style Vocabulary

Use these terms in your query's **Style Guide** section to control the overall look:

### Overall Aesthetic

| Style | Description | Best For |
|-------|-------------|----------|
| **Minimalist** | Lots of whitespace, single focal point, clean lines | Tech, luxury, modern brands |
| **Bold/Dynamic** | Strong colors, large text, high contrast | Sales, motivation, events |
| **Corporate** | Professional, structured, conservative colors | B2B, finance, enterprise |
| **Creative** | Asymmetric layouts, artistic elements, playful | Design, marketing, startups |
| **Editorial** | Magazine-style, elegant typography, refined | Thought leadership, reports |
| **Cinematic** | Dark backgrounds, dramatic lighting, film-like | Keynotes, product launches |
| **Flat Design** | 2D elements, solid colors, no shadows | Tech, apps, modern UI |
| **Gradient** | Color transitions, depth, modern feel | Tech, creative, premium |
| **Illustrated** | Custom illustrations, hand-drawn feel | Education, storytelling |
| **Photo-Forward** | Large imagery, minimal text overlay | Lifestyle, travel, events |

### Example Style Guide Descriptions

```
# Minimalist Tech
"Clean minimalist style with generous whitespace. Dark charcoal (#2D2D2D) 
backgrounds with white text. Single accent color (electric blue #0066FF). 
Modern sans-serif typography. One idea per slide maximum."

# Bold Sales Deck
"High-energy bold design with strong color blocks. Deep red and gold color 
scheme. Large impactful headlines. Dynamic angles and geometric shapes. 
Each slide should command attention."

# Corporate Professional
"Polished corporate aesthetic. Navy blue and white primary palette with 
silver accents. Clean grid layouts. Professional stock photography of 
business settings. Conservative but modern."

# Creative Agency
"Artistic and unconventional. Asymmetric layouts that break the grid. 
Bold color combinations (coral + teal). Mix of photography and abstract 
elements. Playful but sophisticated typography."
```

---

## Color Scheme Language

### How to Specify Colors

```
# By Name (general guidance)
"Navy blue primary with gold accents"
"Earth tones - warm browns, forest greens, cream"
"Monochromatic blue palette ranging from sky to midnight"

# By Hex Code (precise control)
"Primary: #1A1A2E (deep navy), Accent: #E94560 (coral red), 
Background: #F5F5F5 (off-white)"

# By Reference
"Match the Unshakable brand kit colors"
"Similar to Apple's presentation style - white backgrounds, 
black text, minimal color accents"

# By Mood
"Warm and inviting - sunset oranges, warm yellows"
"Cool and professional - steel blues, silver grays"
"Bold and energetic - electric colors, high saturation"
```

### Color Scheme Types

| Type | Description | Query Language |
|------|-------------|----------------|
| **Monochromatic** | Single color, multiple shades | "Monochromatic blue scheme from light to dark" |
| **Complementary** | Opposite on color wheel | "Complementary orange and blue for high contrast" |
| **Analogous** | Adjacent colors | "Analogous warm palette - red, orange, yellow" |
| **Triadic** | Three evenly spaced | "Triadic scheme with primary colors" |
| **Split-Complementary** | One + two adjacent to complement | "Navy with coral and gold accents" |
| **Dark Mode** | Dark backgrounds, light text | "Dark mode with charcoal background, white text" |
| **Light Mode** | Light backgrounds, dark text | "Clean white backgrounds with dark gray text" |

### Background Specifications

```
# Solid
"Solid white background" / "Solid dark navy (#1A1A2E) background"

# Gradient
"Subtle gradient from white to light gray"
"Bold diagonal gradient from purple to pink"
"Radial gradient with dark center fading to edges"

# Textured
"Subtle paper texture background"
"Light geometric pattern in background"
"Soft noise texture for depth"

# Image-Based
"Full-bleed professional photography backgrounds"
"Blurred/frosted background images with text overlay"
"Split background - image on left, solid color on right"
```

---

## Typography Guidance

### Font Style Descriptions

```
# Sans-Serif (Modern, Clean)
"Modern sans-serif like Montserrat or Poppins"
"Clean geometric sans-serif typography"
"Bold condensed sans-serif for headlines"

# Serif (Traditional, Elegant)
"Elegant serif for headlines, clean sans for body"
"Editorial serif typography for sophisticated feel"
"Classic serif with modern spacing"

# Display/Decorative
"Bold display font for headlines only"
"Impactful condensed headline typography"

# Mixed
"Contrast serif headlines with sans-serif body text"
"Script accent font for emphasis words only"
```

### Text Hierarchy

```
"Strong text hierarchy: 
 - Headlines: 60pt+ bold, maximum impact
 - Subheads: 32pt medium weight
 - Body: 24pt regular weight
 - Caption: 18pt light weight"

"Minimal text approach:
 - One headline per slide (5-7 words max)
 - Key phrases only, no paragraphs
 - Let visuals tell the story"

"Text-forward design:
 - Readable body text at 20pt minimum
 - Clear bullet formatting
 - Generous line spacing (1.5x)"
```

---

## Layout Patterns

### Slide Layout Types

Use these terms to specify how content should be arranged:

```
# Full-Bleed Image
"Full-bleed background image with text overlay in bottom third"
"Edge-to-edge photography with centered headline"

# Split Layout
"50/50 split - image left, content right"
"60/40 split - larger content area on left"
"Vertical split with image top, text bottom"

# Grid Layout
"2x2 grid for comparing 4 concepts"
"3-column layout for features/benefits"
"Icon grid with 6 elements"

# Centered
"Centered single message with ample whitespace"
"Center-aligned quote with attribution below"

# Asymmetric
"Offset layout with content at rule of thirds"
"Diagonal composition with dynamic angles"

# Sidebar
"Content with thin sidebar for navigation/branding"
"Wide content area with narrow accent stripe"
```

### Layout Specifications by Slide Type

| Slide Type | Recommended Layout | Visual Elements |
|------------|-------------------|-----------------|
| Title slide | Centered, minimal | Logo, title, subtitle, speaker name |
| Agenda | Left-aligned list | Numbered items, icons optional |
| Section divider | Centered, bold | Section number, title, subtle imagery |
| Content | Split or grid | Headline, bullets, supporting visual |
| Quote | Centered | Large quote marks, attribution |
| Statistics | Grid or centered | Large numbers, supporting context |
| Comparison | 2-column or table | Side-by-side elements |
| Timeline | Horizontal flow | Connected points, dates |
| Team | Grid | Photos, names, titles |
| CTA | Centered | Clear action, contact info |

---

## Adding Logos and Assets

### Logo Placement Options

```
# In Query - Describe Placement
"Company logo in top-right corner of every slide as watermark"
"Logo centered on title slide, small in footer on content slides"
"Logo as transparent overlay in bottom-left corner"
"White version of logo on dark slides, dark on light slides"

# Logo Sizing
"Logo at 120px width maximum"
"Small logo mark (icon only) in corners"
"Full logo lockup on title and closing slides only"
```

### Using Assets (Images/Graphics)

**Step 1: Upload assets first**
```python
upload-asset-from-url(
  url="https://example.com/company-logo.png",
  name="company_logo"
)
# Returns: asset_id = "MAG9TxdnD2o"
```

**Step 2: Reference in generate-design**
```python
generate-design(
  query="...",
  design_type="presentation",
  brand_kit_id="kAFrPxMDrlE",
  asset_ids=["MAG9TxdnD2o", "MAG7-a-HDko", "MAG51FB1PHM"]
)
```

**Step 3: Describe placement in query**
```
ASSET USAGE:
- Asset #1 (company logo): Top-right corner on all slides, 100px width
- Asset #2 (hero image): Full-bleed on slide 1 with dark overlay
- Asset #3 (team photo): Slide 8, right half of split layout
- Asset #4 (product screenshot): Slide 5, centered with subtle shadow
```

### Image Style Descriptions

```
# Photography Style
"Professional corporate photography - diverse teams in modern offices"
"Candid lifestyle photography, natural lighting"
"High-contrast dramatic photography with dark mood"
"Bright, airy photography with white backgrounds"

# Treatment
"Images with dark overlay (70% opacity) for text readability"
"Desaturated/muted image treatment for cohesive look"
"Duotone image effect using brand colors"
"Images with rounded corners (16px radius)"

# Composition
"Photography with subject on left third, text space on right"
"Close-up/detail shots for texture slides"
"Wide establishing shots for section dividers"
```

---

## Slide-by-Slide Visual Specifications

### Title Slide

```
**Slide 1 — "Main Presentation Title"**
...
**Visuals:** 
- Layout: Centered, minimal elements
- Background: Dark gradient or full-bleed branded image with 60% dark overlay
- Logo: Centered above title, 150px width
- Typography: Title in bold display font (72pt), subtitle in light weight (28pt)
- Accent: Thin gold line below title
- Footer: Date and presenter name, 16pt, bottom-left
```

### Section Divider Slide

```
**Slide 5 — "Section: Market Analysis"**
...
**Visuals:**
- Layout: Centered single message
- Background: Solid brand color (navy) or dramatic photo with heavy overlay
- Typography: Section number small (24pt) above, section title large (60pt) below
- Accent: Geometric shape or subtle pattern in corners
- Transition effect: Consider fade-in animation
```

### Data/Statistics Slide

```
**Slide 7 — "47% Revenue Growth in Q3"**
...
**Visuals:**
- Layout: Large number left (40% width), context right (60% width)
- The "47%" should be massive - 200pt+ in accent color
- Supporting text in 24pt, positioned as brief explanation
- Subtle upward arrow or growth icon integrated
- Background: Clean white with thin colored accent bar at bottom
```

### Comparison Slide

```
**Slide 9 — "Before vs. After: The Transformation"**
...
**Visuals:**
- Layout: True 50/50 split with thin vertical divider
- Left side: "Before" with muted/grayscale treatment
- Right side: "After" with full color/vibrant
- Icons or images in each column
- Consistent vertical alignment across both sides
- Labels "BEFORE" and "AFTER" as small caps headers
```

### Quote Slide

```
**Slide 12 — "What Our Clients Say"**
...
**Visuals:**
- Layout: Centered quote with generous margins (20% on each side)
- Large decorative quotation marks in accent color (subtle, background)
- Quote text in serif or elegant font, 36pt, italic optional
- Attribution below: photo circle (80px), name, title
- Background: Solid light color or subtle texture
```

### Call-to-Action Slide

```
**Slide 15 — "Start Your Journey Today"**
...
**Visuals:**
- Layout: Centered, clear hierarchy
- Headline: Bold, action-oriented (48pt)
- Primary CTA: Button-style treatment with accent color
- Supporting info: Website, phone, email in clean stack
- QR code: Optional, bottom-right for easy scanning
- Background: Brand color or impactful imagery with overlay
- Logo: Centered at bottom
```

---

## Visual Consistency Checklist

Include in your query to ensure consistency:

```
VISUAL CONSISTENCY REQUIREMENTS:
□ Same logo placement on all slides (top-right, 80px width)
□ Consistent header position (top 15% of slide)
□ Uniform bullet styling (squares, not circles; brand color)
□ Same margin/padding on all content slides (80px from edges)
□ Consistent font sizes across similar elements
□ Same photo treatment throughout (rounded corners, shadows, etc.)
□ Repeating accent element (line, shape, pattern) for cohesion
□ Consistent transition/animation style (subtle fade preferred)
□ Page numbers in same position (bottom-right, 14pt)
□ Color palette limited to 3-4 colors maximum
```

---

## Complete Visual Style Example

Here's a complete Style Guide section for a query:

```
**Style Guide:**
OVERALL: Corporate minimalist with bold accents. Premium, trustworthy feel.

COLORS:
- Primary: Deep Navy (#1A2B4A)
- Accent: Gold (#C9A227)
- Background: Off-white (#F8F8F6) for light slides, Navy for dark slides
- Text: Charcoal (#333333) on light, White on dark

TYPOGRAPHY:
- Headlines: Montserrat Bold, 44-60pt
- Body: Open Sans Regular, 20-24pt
- Accents: Montserrat SemiBold for emphasis

IMAGERY:
- Professional photography with warm lighting
- Images desaturated slightly for cohesive look
- All images with subtle shadow (8px blur, 15% opacity)

LAYOUT RULES:
- Generous whitespace (minimum 80px margins)
- Content in upper 2/3, bottom third for breathing room
- Max 6 lines of body text per slide
- One key visual per content slide

BRAND ELEMENTS:
- Logo: Top-right corner, all slides, 100px width
- Accent line: Thin gold (2px) below headlines
- Section dividers: Full navy background with centered white text

TRANSITIONS:
- Subtle fade between slides
- No flashy animations
```

---

## Quick Reference: Visual Description Templates

**Minimalist Tech:**
"Minimalist dark mode. Charcoal backgrounds, white text, electric blue (#00A3FF) accents. Maximum whitespace. Single sans-serif font family. One element per slide. No decorative elements."

**Bold Sales:**
"High-impact bold design. Split layouts with striking imagery. Deep red (#CC0000) and gold (#FFD700). Large headlines (72pt+), minimal body text. Dynamic diagonal elements."

**Elegant Corporate:**
"Refined corporate style. Navy and cream palette. Serif headlines, clean sans-serif body. Subtle gold accents. Professional photography. Grid-based layouts with ample margins."

**Creative Modern:**
"Contemporary creative style. Asymmetric layouts. Gradient backgrounds (purple to coral). Mixed media - photos with geometric overlays. Bold typography with creative spacing."

**Educational/Training:**
"Clear instructional design. Light backgrounds, high contrast text. Numbered steps, clear icons. Visual hierarchy emphasizing learning sequence. Friendly, approachable feel."
