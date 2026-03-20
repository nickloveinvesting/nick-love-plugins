---
name: canva-mcp
description: >
  Complete Canva design automation via MCP tools. Use when user wants to create,
  edit, export, organize, or collaborate on Canva designs including presentations,
  social media posts, documents, and logos. Handles AI design generation, brand kit
  integration, multi-format export, and team collaboration.
---

# Canva MCP Skill

## Overview

This skill enables comprehensive Canva automation through 19+ MCP tools organized into 5 categories: Search/Browse, Read, Generate, Modify, and Collaborate.

## Quick Reference: When to Use Which Tool

| User Intent | Tool(s) | Key Parameters |
|-------------|---------|----------------|
| "Find my presentation about X" | `search-designs` | query, sort_by |
| "Create a presentation about X" | `generate-design` + `create-design-from-candidate` | design_type="presentation", query, brand_kit_id |
| "Make an Instagram post" | `generate-design` | design_type="instagram_post", query |
| "Export as PDF" | `get-export-formats` → `export-design` | format.type="pdf" |
| "What brand kits do I have?" | `list-brand-kits` | - |
| "Show what's in my folder" | `list-folder-items` | folder_id |
| "Read the text from this design" | `get-design-content` | content_types=["richtexts"] |
| "Add a comment" | `comment-on-design` | message_plaintext |
| "Convert to presentation format" | `resize-design` | design_type.type="preset", name="presentation" |

## Critical Rules

### Rule 1: Brand Kit Workflow
**ALWAYS** ask user about brand kit before calling `generate-design`:
```
"Would you like to create an on-brand design? I can use your brand kit for consistent colors, fonts, and logos."
```
If yes → call `list-brand-kits` → let user select → include `brand_kit_id` in `generate-design`.

### Rule 2: Design Generation is Two-Step
1. `generate-design` returns candidates (4 options with thumbnails)
2. Present options to user, get selection
3. `create-design-from-candidate(job_id, candidate_id)` creates actual editable design
4. Use returned `design_id` for all subsequent operations

### Rule 3: ID Patterns
- **Design ID**: `D[a-zA-Z0-9_-]{10}` (11 chars, starts with D) — e.g., `DAG9TPtALt0`
- **Folder ID**: `FA[...]` pattern — e.g., `FAF9kJO-MS8`
- **Brand Kit ID**: `k[A-Za-z0-9]+` — e.g., `kAFrPxMDrlE`
- **Image/Asset ID**: `M[A-Za-z0-9]+` — e.g., `MAG9TxdnD2o`
- ⚠️ IDs in Canva URLs are NOT the design_id parameter (URL IDs are different encoding)

### Rule 4: Pagination
- Never fabricate continuation tokens
- Only use tokens returned from previous responses
- Omit parameter entirely if no token was returned

---

## Core Workflows

### Workflow 1: Create New Design

```
1. ASK: "Would you like on-brand design?"
   YES → list-brand-kits → user selects → save brand_kit_id
   NO → proceed without brand_kit_id

2. GENERATE: generate-design
   - query: Detailed description (see Prompting Best Practices)
   - design_type: See Design Types Reference
   - brand_kit_id: (if selected)
   - asset_ids: (optional) Array of image IDs in order

3. PRESENT: Show 4 candidates with thumbnails
   "Here are 4 design options. Which do you prefer? (1-4)"

4. CREATE: create-design-from-candidate
   - job_id: From step 2 response
   - candidate_id: From user selection

5. DELIVER: Return edit_url for user to refine in Canva
```

### Workflow 2: Search & Retrieve Designs

```
1. SEARCH: search-designs
   - query: Keywords from user request
   - ownership: "any" (default), "owned", or "shared"
   - sort_by: "relevance" (if query used), "modified_descending", etc.

2. DISPLAY: Show results with titles and thumbnails

3. DETAILS: If user selects one → get-design for full metadata

4. CONTENT: If user wants text → get-design-content
   - content_types: ["richtexts"]
   - pages: [1, 2, 3] (optional, specific pages)
```

### Workflow 3: Export Design

```
1. CHECK: get-export-formats
   Returns: {formats: {pdf:{}, jpg:{}, png:{}, pptx:{}, gif:{}, mp4:{}}}

2. EXPORT: export-design
   - design_id: Target design
   - format: {type: "pdf", export_quality: "pro", pages: [1,2,3]}

3. DELIVER: Return download URL(s) to user
   ⚠️ URLs are temporary (expire within hours)
```

### Workflow 4: Resize/Convert Design

```
resize-design creates a NEW design (does not modify original)

PRESET options:
- {type: "preset", name: "presentation"}
- {type: "preset", name: "doc"}
- {type: "preset", name: "whiteboard"}

CUSTOM options:
- {type: "custom", width: 1920, height: 1080}
```

---

## Design Types Reference

| Type | Use Case |
|------|----------|
| `presentation` | Slide decks, pitch decks, webinars |
| `instagram_post` | Square social media content |
| `facebook_post` | Facebook feed content |
| `twitter_post` | Twitter/X posts |
| `youtube_thumbnail` | Video thumbnails |
| `youtube_banner` | Channel headers |
| `your_story` | Instagram/Facebook stories (vertical) |
| `flyer` | Single-page promotional |
| `poster` | Large format print |
| `infographic` | Data visualization |
| `logo` | Brand identity |
| `business_card` | Contact cards |
| `document` | Professional documents |
| `report` | Data reports |
| `proposal` | Business proposals |
| `resume` | CVs and resumes |
| `invitation` | Event invitations |
| `card` | Greeting cards |
| `postcard` | Mailable postcards |
| `photo_collage` | Multi-photo layouts |
| `facebook_cover` | Profile/page banners |
| `pinterest_pin` | Pinterest content |
| `desktop_wallpaper` | Computer backgrounds |
| `phone_wallpaper` | Mobile backgrounds |

---

## Reference Files

This skill includes deep-dive references for complex topics:

| Reference | When to Use |
|-----------|-------------|
| `references/presentations.md` | Creating presentation slide plans, narrative arcs |
| `references/visual-design.md` | General styling: colors, typography, logos, layouts |
| `references/unshakable-style-guide.md` | **Unshakable Investor / Toby Potter brand presentations** |
| `references/social-media.md` | Platform-specific social content |
| `references/quick-reference.md` | One-liner commands, format options |

**For visual styling questions**, always read `references/visual-design.md` first - it contains:
- Visual style vocabulary (minimalist, bold, corporate, etc.)
- Color scheme language and specifications
- Typography guidance
- Layout pattern options
- Logo/asset integration instructions
- Slide-by-slide visual specifications
- Complete visual style examples

**For Unshakable Investor / Toby Potter presentations**, read `references/unshakable-style-guide.md`:
- Exact brand colors (deep black, amber gold #D4A853)
- Curved gold accent lines pattern
- Fire/smoke texture overlays
- 7 specific slide layout types
- Problem cards with red X icons
- Statement slide patterns

---

## Prompting Best Practices

### For Presentations (Most Complex)

Structure the query with these sections:

**1. Presentation Brief**
```
Title: [Working title]
Topic/Scope: [1-2 lines, define uncommon terms]
Key Messages: [3-5 crisp takeaways]
Constraints: [Brand, data limits, language]
Style Guide: [Tone, colors, imagery style]
```

**2. Narrative Arc**
```
One paragraph: Hook → Problem → Insight → Solution → Proof → Plan → CTA
```

**3. Slide Plan**
For each slide include:
```
Slide N — "Exact Title"
Goal: One sentence purpose
Bullets (3-6): Short, parallel phrasing with specifics
Visuals: Explicit recommendation (e.g., "Clustered bar chart of X by Y")
Data/Inputs: Concrete values or "example values" if unknown
Speaker Notes: 2-4 sentences narrative
Transition: Lead to next slide
```

### Visual Styling (Critical for Quality)

Every presentation query needs a **Style Guide** section. See `references/visual-design.md` for complete vocabulary.

**Minimum Style Guide:**
```
**Style Guide:**
- Overall: [Minimalist/Bold/Corporate/Creative/Editorial]
- Colors: [Primary, Accent, Background - with hex codes or descriptions]
- Typography: [Font style, size hierarchy]
- Imagery: [Photo style, treatment]
- Layout: [Grid/Split/Centered preferences]
- Logo: [Placement, size on slides]
```

**Example for professional deck:**
```
**Style Guide:**
Corporate minimalist. Navy (#1A2B4A) primary, gold (#C9A227) accents, 
off-white backgrounds. Montserrat Bold headlines (48pt), Open Sans body (22pt).
Professional photography with subtle desaturation. Clean grid layouts with 
80px margins. Logo top-right on all slides, 100px width.
```

### For Social Media

Include in query:
- Target audience
- Primary message/CTA
- Tone (professional, casual, urgent)
- Color preferences (or reference brand kit)
- Text to include (headline, subtext, CTA button)

### For Documents/Reports

Include in query:
- Document purpose
- Target reader
- Key sections needed
- Data visualization requirements
- Branding requirements

---

## Tool Reference

### Search & Browse

**search-designs**
- query: Search term (if used, sort_by must be "relevance")
- ownership: "any" | "owned" | "shared"
- sort_by: "relevance" | "modified_descending" | "modified_ascending" | "title_ascending" | "title_descending"
- continuation: Pagination token from previous response

**search-folders**
- query: Folder name/tag search
- ownership: "any" | "owned" | "shared"
- limit: 1-100 (default 5)
- continuation: Pagination token

**list-brand-kits**
- continuation: Pagination token
- Returns: id, name, thumbnail for each brand kit

**list-folder-items**
- folder_id: Target folder ID or "root"
- item_types: ["design", "folder", "image"] filter
- sort_by: Sort order
- continuation: Pagination token

### Read

**get-design**
- design_id: Required (11 chars, starts with D)
- Returns: id, title, owner, thumbnail, urls (edit_url, view_url), timestamps, page_count

**get-design-pages**
- design_id: Required
- offset, limit: Pagination (0-indexed)
- Returns: Array of {index, thumbnail}

**get-design-content**
- design_id: Required
- content_types: ["richtexts"] (only option currently)
- pages: Optional array of page numbers (1-indexed)
- Returns: Extracted text content

**get-presenter-notes**
- design_id: Required
- pages: Optional array (1-indexed)
- Returns: Array of {page_number, notes}

**get-export-formats**
- design_id: Required
- Returns: Available formats object

### Generate

**generate-design**
- query: Required - detailed description
- design_type: Optional - from Design Types Reference
- brand_kit_id: Optional - from list-brand-kits
- asset_ids: Optional - array of image IDs in slide order
- Returns: job_id + array of candidates

**create-design-from-candidate**
- job_id: From generate-design response
- candidate_id: Selected candidate ID
- Returns: design_summary with design_id for further operations

### Modify

**export-design**
- design_id: Required
- format: Object with type and options
  - type: "pdf" | "png" | "jpg" | "pptx" | "gif" | "mp4"
  - export_quality: "regular" | "pro"
  - pages: Array of page numbers
  - (Type-specific options: size, quality, transparency, etc.)
- Returns: Download URL(s)

**resize-design**
- design_id: Required
- design_type: {type: "preset", name: "..."} or {type: "custom", width, height}
- Returns: NEW design with new design_id

**upload-asset-from-url**
- url: Source URL
- name: Asset name
- Returns: Asset ID for use in generate-design

**import-design-from-url**
- url: Source file URL
- name: Design name
- Returns: New design summary

**create-folder**
- name: Folder name
- parent_folder_id: Parent ID or "root"
- Returns: Folder ID and URL

**move-item-to-folder**
- item_id: Design, folder, or image ID
- to_folder_id: Destination folder ID or "root"

### Collaborate

**comment-on-design**
- design_id: Required
- message_plaintext: Comment text (max 1000 chars)
- Returns: Thread ID and metadata

**list-comments**
- design_id: Required
- comment_resolution: "resolved" | "unresolved" (default)
- limit: 1-100 (default 50)
- continuation: Pagination token

**reply-to-comment**
- design_id: Required
- comment_id: From list-comments
- message_plaintext: Reply text (max 2048 chars)

**list-replies**
- design_id: Required
- comment_id: Required
- limit: 1-100 (default 50)
- continuation: Pagination token

---

## Common Patterns

### Pattern: Find and Export Recent Work
```
1. search-designs(sort_by="modified_descending")
2. User selects design
3. get-export-formats(design_id)
4. export-design(design_id, format={type:"pdf"})
5. Return download URL
```

### Pattern: Create On-Brand Social Media Campaign
```
1. list-brand-kits()
2. User selects brand
3. For each platform:
   generate-design(design_type="instagram_post", brand_kit_id, query)
   create-design-from-candidate()
4. Organize: create-folder("Campaign Name")
5. move-item-to-folder() for each design
```

### Pattern: Review and Comment on Team Work
```
1. search-designs(ownership="shared")
2. get-design-content() to review text
3. get-design-pages() to see thumbnails
4. comment-on-design() with feedback
5. list-comments() to see discussion
```

---

## Anti-Patterns to Avoid

❌ **Don't** use design_type without generate-design (it's only for generation)
❌ **Don't** assume URL IDs are design_ids (they're different encodings)
❌ **Don't** fabricate continuation tokens (always from responses)
❌ **Don't** skip brand kit question for professional content
❌ **Don't** expect resize-design to modify in-place (creates new design)
❌ **Don't** call search-brand-templates via search-designs (they're separate)
❌ **Don't** assume export URLs are permanent (they expire)
❌ **Don't** use vague queries for generate-design (be specific)
