# Canva MCP Quick Reference

## One-Liners for Common Tasks

### Find Designs
```python
# Search by keyword
search-designs(query="webinar", sort_by="relevance")

# Recent modifications
search-designs(sort_by="modified_descending")

# My designs only
search-designs(ownership="owned")

# Shared with me
search-designs(ownership="shared")
```

### Get Design Info
```python
# Full metadata
get-design(design_id="DAG9TPtALt0")

# Extract text
get-design-content(design_id="...", content_types=["richtexts"])

# Get specific pages text
get-design-content(design_id="...", content_types=["richtexts"], pages=[1,2,3])

# Page thumbnails
get-design-pages(design_id="...", limit=10)

# Speaker notes
get-presenter-notes(design_id="...", pages=[1,2,3])
```

### Generate Designs
```python
# Simple generation
generate-design(query="Professional Instagram post about...", design_type="instagram_post")

# With brand kit
generate-design(query="...", design_type="presentation", brand_kit_id="kAFrPxMDrlE")

# With images
generate-design(query="...", asset_ids=["MAG9TxdnD2o", "MAG7-a-HDko"])

# Convert candidate to real design
create-design-from-candidate(job_id="99510ce8-...", candidate_id="dg-b46bd9b8-...")
```

### Export
```python
# Check available formats
get-export-formats(design_id="...")

# PDF export
export-design(design_id="...", format={"type":"pdf", "export_quality":"pro"})

# PNG with transparency
export-design(design_id="...", format={"type":"png", "transparent_background":true})

# Specific pages
export-design(design_id="...", format={"type":"pdf", "pages":[1,2,3]})

# Video
export-design(design_id="...", format={"type":"mp4", "quality":"horizontal_1080p"})
```

### Resize/Convert
```python
# To presentation
resize-design(design_id="...", design_type={"type":"preset", "name":"presentation"})

# Custom size
resize-design(design_id="...", design_type={"type":"custom", "width":1920, "height":1080})
```

### Organization
```python
# List brand kits
list-brand-kits()

# Browse folders
list-folder-items(folder_id="root")
list-folder-items(folder_id="FAF9kJO-MS8", item_types=["design"])

# Create folder
create-folder(name="Campaign Q1", parent_folder_id="root")

# Move item
move-item-to-folder(item_id="DAG9kP-fKpA", to_folder_id="FAF9kJO-MS8")
```

### Collaboration
```python
# Add comment
comment-on-design(design_id="...", message_plaintext="Great work on slide 3!")

# View comments
list-comments(design_id="...", comment_resolution="unresolved")

# Reply
reply-to-comment(design_id="...", comment_id="KAG9kPQZRBY", message_plaintext="Thanks!")

# View replies
list-replies(design_id="...", comment_id="KAG9kPQZRBY")
```

## Format Options Reference

### PDF Export
```json
{
  "type": "pdf",
  "export_quality": "pro",    // "regular" or "pro"
  "size": "a4",               // "a4", "a3", "letter", "legal"
  "pages": [1, 2, 3]          // specific pages (1-indexed)
}
```

### PNG Export
```json
{
  "type": "png",
  "export_quality": "pro",
  "width": 1920,              // 40-25000 pixels
  "height": 1080,
  "transparent_background": true,
  "lossless": true,
  "as_single_image": true,    // merge multi-page into one
  "pages": [1]
}
```

### JPG Export
```json
{
  "type": "jpg",
  "export_quality": "pro",
  "width": 1920,
  "height": 1080,
  "quality": 90,              // 1-100
  "pages": [1, 2]
}
```

### PPTX Export
```json
{
  "type": "pptx",
  "export_quality": "pro",
  "pages": [1, 2, 3, 4, 5]
}
```

### GIF Export
```json
{
  "type": "gif",
  "export_quality": "pro",
  "width": 800,
  "height": 600,
  "pages": [1, 2, 3]
}
```

### MP4 Export
```json
{
  "type": "mp4",
  "export_quality": "pro",
  "quality": "horizontal_1080p",
  "pages": [1, 2, 3]
}
```

## Design Types Quick List

**Social Media:** `instagram_post`, `facebook_post`, `twitter_post`, `your_story`, `pinterest_pin`, `facebook_cover`, `youtube_thumbnail`, `youtube_banner`

**Print:** `flyer`, `poster`, `business_card`, `postcard`, `invitation`, `card`

**Documents:** `document`, `report`, `proposal`, `resume`, `presentation`

**Graphics:** `logo`, `infographic`, `photo_collage`

**Wallpapers:** `desktop_wallpaper`, `phone_wallpaper`

## Error Handling Patterns

### Missing Scopes
If tool returns "Missing scopes: [asset:write]" or similar:
→ Ask user to disconnect and reconnect their Canva connector in Claude settings

### Invalid Design ID
Design IDs must be exactly 11 characters starting with "D":
- ✅ `DAG9TPtALt0`
- ❌ `AG9TPtALt0` (missing D)
- ❌ `DAG9TPtALt0xyz` (too long)

### Pagination Token Errors
Never fabricate tokens. Only use exact tokens from previous response.
If no continuation token returned → omit parameter entirely

### Common Query Errors
"Common queries will not be generated" → Add more detail to query
→ Include specific audience, colors, style, text content
