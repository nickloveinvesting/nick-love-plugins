# Anti-Patterns: How to Avoid AI-Looking Landing Pages

## The Dead Giveaways of AI Design

### 1. The Gradient Epidemic

**What AI Does:**
- Gradient backgrounds everywhere
- Multiple competing gradients on one page
- Bright, saturated gradient meshes
- Purple-to-blue gradients (the AI favorite)

**What Premium Designs Do:**
- Solid colors or subtle single gradient as accent only
- Monochromatic backgrounds (off-white, light gray)
- One subtle gradient in hero, if at all
- Prefer transparent overlays with backdrop-blur

**Fix:**
```
❌ bg-gradient-to-br from-purple-500 via-pink-500 to-orange-500
✅ bg-slate-50 or bg-white
✅ bg-gradient-to-br from-blue-50 to-indigo-50 (very subtle)
```

### 2. The Everything-Centered Syndrome

**What AI Does:**
- Every section centered
- All text centered
- CTAs floating in the middle
- Symmetric layouts throughout

**What Premium Designs Do:**
- Asymmetric hero (60/40 split)
- Left-aligned text blocks
- Right-aligned images offset
- Strategic use of centering (sparingly)

**Fix:**
```
❌ Everything: text-center mx-auto
✅ Hero: text-left with grid grid-cols-1 lg:grid-cols-2 gap-12
✅ Feature sections: Alternate left/right layouts
```

### 3. The Rainbow Catastrophe

**What AI Does:**
- Different bright color for each section
- Blue, purple, green, orange, pink all on one page
- Each card a different color
- "Colorful" = "professional" (wrong)

**What Premium Designs Do:**
- 1 brand color + 1 accent color maximum
- 80% neutral colors (grays, off-white)
- Strategic pops of color for CTAs only
- Monochromatic sophistication

**Fix:**
```
❌ Sections: bg-blue-500, bg-purple-500, bg-green-500, bg-pink-500
✅ Sections: bg-white, bg-slate-50, bg-slate-900 (for contrast)
✅ CTAs: Only element with saturated color
```

### 4. The Stock Photo Disaster

**What AI Does:**
- Generic diverse team high-fiving in office
- Smiling person pointing at laptop
- Corporate handshake photos
- Obviously posed "candid" shots

**What Premium Designs Do:**
- Real product screenshots
- Actual customer photos (if applicable)
- Custom illustrations or abstract shapes
- High-quality, authentic photography
- Or no photos at all (just great typography)

**Fix:**
- Use product demos instead of people
- Use abstract geometric shapes for visual interest
- Use subtle background patterns
- Commission real photography if needed

### 5. The Feature-Dumping Problem

**What AI Does:**
- Lists 20+ features in grid
- Each feature = icon + title + paragraph
- Everything gets equal emphasis
- No clear hierarchy or flow

**What Premium Designs Do:**
- 3-6 key features maximum
- Primary features get more space
- Benefits, not feature lists
- Visual hierarchy clear

**Fix:**
```
❌ 4x5 grid of 20 tiny feature cards
✅ 3 large feature blocks with real benefits
✅ Or: 1 main feature + 4 supporting features (asymmetric grid)
```

### 6. The Pill Button Plague

**What AI Does:**
- Every button: `rounded-full` (pill-shaped)
- Multiple pill buttons competing
- Gradient pill buttons
- Floating pill buttons everywhere

**What Premium Designs Do:**
- `rounded-lg` (8-12px) maximum
- Rectangular with subtle rounding
- Consistent button style throughout
- Strategic button placement

**Fix:**
```
❌ rounded-full px-8 py-3 bg-gradient-to-r from-purple-500 to-pink-500
✅ rounded-lg px-6 py-3 bg-blue-600 hover:bg-blue-700
```

### 7. The Busy Background Nightmare

**What AI Does:**
- Geometric patterns everywhere
- Animated shapes flying around
- Grid patterns competing with content
- Gradient meshes as backgrounds

**What Premium Designs Do:**
- Clean, minimal backgrounds
- Subtle grid or dot pattern (if any)
- Single accent shape (positioned strategically)
- White space as design element

**Fix:**
```
❌ Background: Rotating shapes, mesh gradient, grid pattern all at once
✅ Background: Solid color with optional subtle grid in one section
✅ Or: Single large shape in corner as accent (opacity: 0.1)
```

### 8. The Typography Chaos

**What AI Does:**
- 3+ different fonts
- Inconsistent sizing
- All caps everywhere
- Centered paragraphs (hard to read)
- Tiny body text (14px or less)

**What Premium Designs Do:**
- 1-2 fonts maximum
- Clear size hierarchy
- Sentence case (not ALL CAPS)
- Left-aligned body text
- 18-20px body text (readable)

**Fix:**
```
❌ <h1 className="text-5xl font-display uppercase text-center">
    <span className="text-blue-500">AMAZING</span>
    <span className="text-purple-500"> PRODUCT</span>
</h1>

✅ <h1 className="text-6xl font-bold text-slate-900 leading-tight">
    Transform Your Business With AI-Powered Analytics
</h1>
```

### 9. The CTA Apocalypse

**What AI Does:**
- 5+ CTAs above the fold
- Different colors for each CTA
- "Learn More" as primary CTA
- CTAs with vague copy

**What Premium Designs Do:**
- 1 primary + 1 secondary CTA max
- Same primary CTA throughout page
- Specific action in CTA copy
- Clear visual hierarchy

**Fix:**
```
❌ [Get Started] [Learn More] [Try Free] [Watch Demo] [Contact Us]
    (all different colors, centered)

✅ [Start Building My Landing Page] (primary, blue-600)
    [See How It Works →] (secondary, ghost button)
```

### 10. The Shadow Overload

**What AI Does:**
- Heavy drop shadows on everything
- Multiple shadow directions
- Glowing neon shadows
- Cards floating with excessive shadows

**What Premium Designs Do:**
- Subtle shadows (shadow-sm, shadow-md)
- Consistent shadow direction
- Minimal shadows, strategic use
- Often no shadows (borders instead)

**Fix:**
```
❌ shadow-2xl shadow-purple-500/50
✅ shadow-sm hover:shadow-md transition-shadow
✅ Or: border border-slate-200 (no shadow at all)
```

## Section-Specific Anti-Patterns

### Hero Section Red Flags

**AI Mistakes:**
```tsx
❌ Centered layout
❌ Gradient background
❌ Generic headline: "Welcome to Our Platform"
❌ Stock photo hero image
❌ Multiple competing CTAs
❌ Busy animated background
```

**Premium Approach:**
```tsx
✅ Asymmetric 60/40 grid
✅ Solid background (off-white or subtle)
✅ Specific headline: Result-focused
✅ Product screenshot or clean illustration
✅ 1 strong CTA + 1 ghost CTA
✅ Clean background, maybe subtle grid
```

### Feature Section Red Flags

**AI Mistakes:**
```tsx
❌ 12+ features in 3x4 grid
❌ Each feature: icon, title, 3 sentences (all identical treatment)
❌ Different colors for each icon
❌ Feature names instead of benefits
```

**Premium Approach:**
```tsx
✅ 3-6 features maximum
✅ Varied layouts (some larger, some smaller)
✅ Icons same color (brand or slate-700)
✅ Benefits-focused copy
```

### Testimonial Section Red Flags

**AI Mistakes:**
```tsx
❌ Carousel (kills conversion)
❌ Fake-looking testimonials
❌ Generic: "Great product! 5 stars!"
❌ Stock photo avatars
❌ No names or companies
```

**Premium Approach:**
```tsx
✅ Static grid (all visible)
✅ Specific results: "Increased revenue 43%"
✅ Real photos or initials
✅ Full name + company/role
✅ 2-4 sentences with details
```

### Pricing Section Red Flags

**AI Mistakes:**
```tsx
❌ 4+ pricing tiers
❌ Every plan different color background
❌ Checkmarks in rainbow colors
❌ "Most Popular" badge on every plan
❌ Inconsistent feature lists
```

**Premium Approach:**
```tsx
✅ 2-3 tiers maximum
✅ Consistent design, one highlighted
✅ Single accent color for highlights
✅ One "Recommended" badge
✅ Clear feature differentiation
```

### Footer Red Flags

**AI Mistakes:**
```tsx
❌ Huge footer with 10+ columns
❌ Every social icon a different color
❌ Newsletter signup in bright color
❌ Competing CTAs in footer
```

**Premium Approach:**
```tsx
✅ Clean, minimal footer (3-4 columns max)
✅ Monochrome social icons
✅ Subtle newsletter signup (if needed)
✅ Footer is for navigation, not conversion
```

## Code-Level Giveaways

### Tailwind Anti-Patterns

**AI Code Smells:**
```tsx
❌ Inconsistent spacing (p-3, p-5, p-7, p-9 randomly)
❌ Rainbow colors (blue-500, purple-600, green-400, pink-500)
❌ Arbitrary values everywhere: [123px] [47%]
❌ Inline styles mixed with Tailwind
❌ No consistent design system

// Example of AI code:
<div className="p-7 bg-gradient-to-r from-purple-400 via-pink-500 to-red-500 rounded-full shadow-2xl">
```

**Premium Code:**
```tsx
✅ Consistent 8pt spacing (p-4, p-6, p-8, p-12)
✅ Monochromatic or 1-2 colors max
✅ Standard Tailwind values
✅ Consistent design tokens
✅ Clear component patterns

// Example of premium code:
<div className="p-8 bg-slate-50 rounded-lg shadow-sm border border-slate-200">
```

### Component Structure Anti-Patterns

**AI Mistakes:**
```tsx
❌ Everything inline (no components)
❌ Repeated code everywhere
❌ Inconsistent spacing
❌ No shared styles or patterns
❌ Copy-paste approach
```

**Premium Approach:**
```tsx
✅ Reusable components
✅ Consistent button components
✅ Shared card patterns
✅ Design system tokens
✅ DRY principles
```

## The Premium Design Checklist

Before considering a landing page complete, verify:

### Visual Design
- [ ] Uses 1-2 fonts maximum
- [ ] Consistent spacing scale (8pt grid)
- [ ] Generous white space (80-128px section padding)
- [ ] Monochromatic or minimal color palette
- [ ] No gradients (or one subtle accent)
- [ ] No stock photos (or high-quality custom only)
- [ ] Subtle shadows only (shadow-sm/md)
- [ ] Professional typography (18-20px body, 64-80px hero)

### Layout
- [ ] Asymmetric hero (not centered)
- [ ] Max-width containers (1280px)
- [ ] Varied layouts between sections
- [ ] Clear visual hierarchy
- [ ] Content breathes (not cramped)

### Copywriting
- [ ] Specific, transformation-focused headlines
- [ ] No AI clichés ("unlock", "next level")
- [ ] Benefit-driven feature copy
- [ ] Specific social proof with numbers
- [ ] Clear, action-focused CTAs

### Conversion Elements
- [ ] 1 primary + 1 secondary CTA max above fold
- [ ] Same primary CTA throughout page
- [ ] Specific CTA copy (not "Learn More")
- [ ] Social proof with real specifics
- [ ] 3-6 key features (not 20)
- [ ] FAQ section with objection handling

### Technical
- [ ] Fast loading (<3s)
- [ ] Mobile-optimized (tested on real device)
- [ ] Semantic HTML
- [ ] Consistent component patterns
- [ ] No console errors
- [ ] Smooth hover states (150-200ms transitions)

## How Humans Spot AI Design (And How to Pass)

### Human Designer Tells
Real designers:
- Make intentional asymmetric choices
- Use restraint (less is more)
- Have consistent spacing systems
- Think in visual hierarchy
- Sweat the micro-interactions
- Use real copy, not lorem ipsum
- Test on real devices
- Care about typography details

### AI Designer Tells
AI generates:
- Perfectly centered everything
- Every section has equal weight
- Rainbow colors "for variety"
- Generic, safe choices everywhere
- Lorem ipsum in final output
- Stock photo clichés
- No attention to details
- Gradient backgrounds by default

### The "Human Touch" Additions

Add these to make it feel human-designed:
1. **Intentional imperfection**: Slightly offset elements, asymmetric spacing (within system)
2. **Personality**: Unexpected micro-interactions, playful hover states
3. **Restraint**: Not using all the colors/fonts/effects available
4. **Details**: Custom icons, tailored illustrations, specific social proof
5. **Story**: Copy that flows naturally, conversational tone
6. **Polish**: Smooth transitions, loading states, error states
7. **Context**: Design choices that fit the brand, not generic templates

## Red Flag Combinations

If you see multiple of these together, it's definitely AI:

**The AI Starter Pack:**
- [ ] Centered hero layout
- [ ] Purple-to-blue gradient background
- [ ] "Unlock Your Potential" headline
- [ ] Generic stock team photo
- [ ] Pill-shaped buttons
- [ ] 8+ feature cards in rainbow colors
- [ ] "Learn More" as primary CTA
- [ ] Testimonial carousel
- [ ] Heavy drop shadows everywhere
- [ ] All caps section titles

**The Premium Designer Pack:**
- [ ] Asymmetric hero with 60/40 split
- [ ] Solid off-white background (slate-50)
- [ ] Specific transformation headline
- [ ] Product screenshot or minimal visual
- [ ] Rounded-lg buttons (8-12px)
- [ ] 3-4 features with varied layouts
- [ ] Action-specific CTA copy
- [ ] Static testimonial grid
- [ ] Subtle shadows or borders
- [ ] Sentence case throughout

## Quick Reference: AI vs Premium

| Element | AI Default | Premium Approach |
|---------|-----------|------------------|
| Background | Gradient mesh | Solid off-white |
| Hero Layout | Centered | Asymmetric 60/40 |
| Typography | 3+ fonts | 1-2 fonts max |
| Colors | Rainbow | Monochrome + 1 accent |
| Buttons | Pill-shaped | Subtle radius (8-12px) |
| Features | 12+ in grid | 3-6 strategically placed |
| Photos | Stock generic | Real product or none |
| Shadows | Heavy everywhere | Subtle, strategic |
| Spacing | Random | Consistent 8pt scale |
| CTA Copy | "Learn More" | Specific action |
| Testimonials | Carousel | Static grid |
| White Space | Minimal | Generous |

Remember: **Premium design is about restraint, intention, and sophistication. AI design is about maximalism, safety, and templates.**
