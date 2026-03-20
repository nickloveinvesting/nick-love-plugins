---
name: facebook-ads-skill
description: Master Facebook Ads for maximum ROI with precise targeting and data-driven optimization. Use for campaign structure and objectives, audience targeting (core/custom/lookalike), persona development, ad creative and copywriting, ad formats (image/video/carousel), placement optimization, pixel implementation, conversion tracking, budget allocation, A/B testing, ROAS/CPA/CTR/CPM analysis, retargeting funnels, scaling strategies, competitor research, creative variant testing, and troubleshooting underperforming campaigns.
---

# Facebook Ads Mastery Skill

Master data-driven Facebook advertising for maximum ROI and precision targeting.

---

## Core Principles

### Campaign Structure Hierarchy

```
Business Manager
  └─ Ad Account
       └─ Campaign (Objective)
            └─ Ad Set (Audience + Placement + Budget)
                 └─ Ad (Creative + Copy)
```

**Best Practice:**
- 1 Campaign = 1 Objective
- 3-5 Ad Sets per Campaign (different audiences)
- 2-3 Ads per Ad Set (different creatives)

---

## Campaign Architecture & Naming

### Naming Convention System

Consistent naming prevents chaos at scale. Use this structure:

```
[Channel]_[Objective]_[Audience]_[Creative]_[Date/TestID]

Examples:
FB_CONV_LAL1-Purchasers_VideoTestimonial_2025Q1
FB_TRAFFIC_INT-RealEstate_CarouselA_T01
FB_LEAD_RET-WebVisitors7d_StaticProof_T03
IG_CONV_BROAD-25-55_UGCHook_2025-01
```

**Component Keys:**
| Code | Meaning |
|------|---------|
| FB/IG | Facebook / Instagram |
| CONV/TRAFFIC/LEAD/AWARE | Objective |
| LAL/INT/RET/BROAD | Lookalike / Interest / Retargeting / Broad |
| T01/T02 | Test variant ID |

### Campaign Structure Patterns

**Prospecting Structure:**
```
Campaign: FB_CONV_Prospecting_Q1
├─ Ad Set: LAL1-Purchasers (1% Lookalike)
├─ Ad Set: LAL2-Leads (2% Lookalike)
├─ Ad Set: INT-Competitors (Interest targeting)
└─ Ad Set: BROAD-25-55 (Broad with age only)
```

**Retargeting Structure:**
```
Campaign: FB_CONV_Retargeting_Q1
├─ Ad Set: RET-WebVisitors-30d (exclude purchasers)
├─ Ad Set: RET-VideoViewers-75pct
├─ Ad Set: RET-CartAbandoners-14d
└─ Ad Set: RET-PageEngagers-60d
```

### Learning Phase Management

Facebook's algorithm needs ~50 conversions per ad set per week to exit learning phase.

**Rules:**
- Don't edit ad sets during learning (resets progress)
- Consolidate small audiences to hit threshold
- Use CBO (Campaign Budget Optimization) for automatic distribution
- Minimum budget: $50/day per ad set for conversion campaigns

**Learning Phase Signals:**
| Status | Meaning | Action |
|--------|---------|--------|
| Learning | <50 conversions, algorithm exploring | Wait, don't touch |
| Learning Limited | Won't hit 50/week | Broaden audience or increase budget |
| Active | Exited learning, optimized | Safe to scale |

### Test Cell Isolation

Structure tests to isolate variables:

```
Test: Hook Type Performance
─────────────────────────────
Campaign: FB_CONV_HookTest_T01
├─ Ad Set: Audience-A (identical across all)
│   ├─ Ad: Hook-Benefit
│   ├─ Ad: Hook-Problem
│   └─ Ad: Hook-Proof
└─ Control: Keep audience, placement, budget identical
```

**Test Design Brief Template:**
```
Variable: [What you're testing]
Hypothesis: [Expected outcome and why]
Metric: [Primary KPI]
Sample Size: [Min conversions needed]
Duration: [Min 7 days, ideally 14]
Success Criteria: [X% lift at 95% confidence]
```

---

## Campaign Objectives Framework

### Awareness Stage
- **Brand Awareness** - Maximize reach
- **Reach** - Show to most people

### Consideration Stage
- **Traffic** - Drive clicks to website
- **Engagement** - Boost posts, page likes
- **App Installs** - Drive downloads
- **Video Views** - Watch video content
- **Lead Generation** - Collect leads via forms
- **Messages** - Start conversations

### Conversion Stage
- **Conversions** - Drive purchases/actions
- **Catalog Sales** - Dynamic product ads
- **Store Traffic** - Drive offline visits

### Choosing the Right Objective

| Goal | Objective |
|------|-----------:|
| Build awareness | Brand Awareness / Reach |
| Drive website traffic | Traffic |
| Collect emails | Lead Generation |
| Sell products online | Conversions / Catalog Sales |
| Get app downloads | App Installs |
| Get messages/inquiries | Messages |
| Boost engagement | Engagement |

---

## Audience Targeting Mastery

### 1. Core Audiences (Manual Targeting)

#### Demographics
- Age range (minimum 18+)
- Gender (All, Male, Female)
- Location (Country, Region, City, ZIP)
- Language
- Education level
- Job title
- Relationship status
- Life events (Engaged, Newlywed, New parent)

#### Interests (The Gold Mine)

**How to find winning interests:**

1. **Layered Targeting** (Narrow Audience)
   ```
   Interest 1: "Small Business Owners"
   AND
   Interest 2: "Accounting Software"
   = Hyper-targeted audience
   ```

2. **Broad + Narrow Stacking**
   ```
   Age: 25-65
   Interest: "Entrepreneurship"
   AND (Narrow): "Marketing"
   AND (Narrow): "Facebook Marketing"
   ```

3. **Competitor Targeting**
   ```
   Interests:
   - [Competitor Brand 1]
   - [Competitor Brand 2]
   - [Industry Magazine]
   - [Industry Influencer]
   ```

#### Behaviors
- Purchase behavior (Engaged shoppers, High-value purchasers)
- Device usage (iPhone users, Android users)
- Travel (Frequent travelers, Commuters)
- Business (Small business owners, IT decision makers)

#### Connections
- People who like your Page
- Friends of people who like your Page
- Exclude people who like your Page (prospecting)

---

### 2. Custom Audiences (Your Data)

#### Website Traffic (via Pixel)

**Pixel Events:**
- View Content (visited product page)
- Add to Cart (added but didn't buy)
- Initiate Checkout (started checkout)
- Purchase (completed transaction)
- Lead (submitted form)

**Retargeting Funnel:**
```
30 days: All website visitors
14 days: Product page viewers (exclude buyers)
7 days: Cart abandoners (exclude buyers)
1 day: Checkout abandoners (HOT LEADS!)
```

**Pixel Implementation:** See `references/pixel-setup.md` for detailed code and event tracking.

#### Customer List Upload
- Email list (existing customers)
- Phone numbers
- App user IDs

#### Engagement Audiences
- Video viewers (25%, 50%, 75%, 95%)
- Instagram profile engagers
- Facebook Page engagers
- Lead form openers

---

### 3. Lookalike Audiences (Scaling Gold)

Facebook finds people similar to your best customers.

**Best Lookalike Sources:**
1. Purchasers (Top 1% - best ROI)
2. High LTV Customers (Top 5% spenders)
3. Email Subscribers (engaged list)
4. Website Visitors (180 days, min 1000 people)
5. Engaged Video Viewers (watched 75%+)

**Lookalike Size Strategy:**

| Audience % | Use Case | Quality |
|:----------:|:--------:|:-------:|
| 1% | Testing, highest quality | Excellent |
| 2-3% | Scaling winners | Very Good |
| 5-6% | Broad reach | Good |
| 10% | Max scale (lower quality) | Fair |

**Advanced Stacking:**
```
1% Lookalike (Purchasers)
AND
Interest: [Related topic]
AND
Age: 25-54
= Hyper-targeted lookalike
```

---

## Persona Development

### Framework: 5W Persona Builder

#### 1. WHO are they?
- Age range, gender, location
- Job title/role, income level
- Education level, relationship status

#### 2. WHAT do they want?
- Primary goal, pain points
- Desires, frustrations
- Current solutions (competitors)

#### 3. WHERE do they hang out?
- Facebook Groups
- Pages they follow
- Brands they like
- Influencers they follow
- Publications they read

#### 4. WHEN do they buy?
- Time of day, day of week
- Season/month
- Trigger events (life events, holidays)

#### 5. WHY will they buy from YOU?
- Unique value proposition
- Trust factors needed
- Social proof
- Objections to overcome

---

## Hook Library & Creative Variants

### The 6 Hook Types

Every ad needs a hook in the first 3 seconds. Master these six types:

#### 1. Benefit Hook
Lead with the outcome they want.
```
"Finally, passive income without being a landlord..."
"Make $10K/month while keeping your day job..."
"Build wealth in 2 hours a week..."
```

#### 2. Problem Hook
Call out the pain they're experiencing.
```
"Tired of trading time for money?"
"Sick of gurus selling you courses that don't work?"
"Still stuck at the same income level you were 5 years ago?"
```

#### 3. Proof Hook
Lead with credibility and results.
```
"I went from $0 to $1.2M in 18 months..."
"Here's how 847 students built 6-figure portfolios..."
"This strategy generated $47K last month alone..."
```

#### 4. Story Hook
Open a narrative loop.
```
"I was sitting in my cubicle when I got the call..."
"Three years ago, I was $300K in debt..."
"Let me tell you about my worst investment ever..."
```

#### 5. Contrarian Hook
Challenge conventional wisdom.
```
"Everything you've been told about real estate is wrong..."
"Stop saving for retirement. Here's why..."
"The #1 reason most investors fail (it's not what you think)..."
```

#### 6. Curiosity Hook
Create an information gap.
```
"The strategy Wall Street doesn't want you to know..."
"I found a loophole in the tax code..."
"This one change doubled my deal flow..."
```

### Voice & Tone by Persona

Adapt messaging to audience sophistication:

| Persona | Tone | Vocabulary | Pain Points |
|---------|------|------------|-------------|
| **Executive (C-Suite)** | Direct, ROI-focused | Strategic, time-value | Time scarcity, risk mitigation |
| **Practitioner (Manager)** | Tactical, how-to | Step-by-step, tools | Implementation, proof it works |
| **Beginner (Aspiring)** | Encouraging, simple | Jargon-free, relatable | Overwhelm, fear of failure |
| **Skeptic (Burned before)** | Transparent, evidence-based | Show the math, real numbers | Trust, realistic expectations |

### Creative Variant Tracker Template

Track all ad variants systematically:

```
| ID | Hook Type | Visual | Copy Angle | CTA | Status | CTR | CVR | ROAS |
|----|-----------|--------|------------|-----|--------|-----|-----|------|
| V01 | Problem | UGC Video | Pain point | Book Call | Active | 2.1% | 3.2% | 4.2x |
| V02 | Proof | Testimonial | Results | Learn More | Active | 1.8% | 2.8% | 3.8x |
| V03 | Benefit | Lifestyle | Outcome | Get Started | Testing | - | - | - |
| V04 | Story | Interview | Journey | Watch Now | Paused | 0.9% | 1.1% | 1.2x |
```

---

## Ad Creative & Copy

### Ad Formats

#### Image Ad
- Single image + text + CTA
- Best for: Simple message, product showcase
- Specs: 1080 x 1080 px (square)

#### Video Ad
- Video + text + CTA
- Best for: Storytelling, demos, testimonials
- Specs: 9:16 (Stories), 1:1 (Feed), 16:9 (Landscape)
- Length: 15-60 seconds ideal

#### Carousel Ad
- 2-10 swipeable cards
- Best for: Multiple products, features, step-by-step
- Specs: 1080 x 1080 px per card

#### Collection Ad
- Cover image/video + product grid
- Best for: E-commerce, browsing experience
- Mobile-only

### Creative Best Practices

**Image:**
- Bright, high-contrast colors
- Faces (increase engagement 30%)
- Text overlay (max 20% of image)
- Show product in use

**Video:**
- Hook in first 3 seconds
- Captions (85% watch without sound)
- Mobile-first (vertical 9:16)
- CTA in video + description

**Copy:**
- Start with benefit
- Use emoji sparingly
- Add urgency (Limited time, Sale ends)
- Clear CTA

### Copywriting Formulas

**PAS (Problem-Agitate-Solution):**
```
Problem:   "Tired of slow website load times?"
Agitate:   "Every second costs you customers"
Solution:  "Our CDN speeds up your site 10x"
CTA:       "Start free trial →"
```

**AIDA:**
```
Attention:  Bold claim or question
Interest:   Benefit or feature
Desire:     Social proof, urgency
Action:     Clear CTA
```

**Story Formula (for video):**
```
Hook (0-3s):     Pattern interrupt, bold claim
Value Proof (3-30s): Show transformation, social proof
CTA (30-45s):    Clear next step, urgency
```

---

## Competitor Research

### Why Research Competitors

- Discover what messaging resonates in your market
- Identify creative patterns that work
- Find gaps in competitor positioning
- Inspire (not copy) your own campaigns
- Understand audience pain points they're targeting

### Facebook Ad Library Research

**Access:** https://www.facebook.com/ads/library

**Search Process:**
1. Search competitor brand name
2. Filter by country, platform, date range
3. Review all active ads
4. Screenshot and categorize findings

**What to Analyze:**

| Element | Questions to Answer |
|---------|---------------------|
| **Hook** | What grabs attention in first 3 seconds? |
| **Pain Points** | What problems are they highlighting? |
| **Value Props** | What benefits do they emphasize? |
| **Social Proof** | How do they build credibility? |
| **CTA** | What action do they want? |
| **Format** | Video, image, carousel? Which dominates? |
| **Frequency** | How many ads are they running? |
| **Longevity** | How long have ads been running? (longer = working) |

### Competitor Analysis Template

```
Competitor: [Name]
Date Analyzed: [Date]
Total Active Ads: [Number]

TOP THEMES:
1. [Theme 1] - [X] ads
2. [Theme 2] - [X] ads
3. [Theme 3] - [X] ads

PAIN POINTS HIGHLIGHTED:
- [Pain point 1]
- [Pain point 2]
- [Pain point 3]

SUCCESSFUL PATTERNS:
- [Pattern 1] - Why it likely works: [reason]
- [Pattern 2] - Why it likely works: [reason]

GAPS/OPPORTUNITIES:
- [What they're NOT addressing that you could]

CREATIVE INSPIRATION:
- [Screenshot/link to ad 1] - Adapt this because: [reason]
- [Screenshot/link to ad 2] - Adapt this because: [reason]
```

**Detailed competitor research methodology:** See `references/competitor-research.md`

---

## Placement Optimization

### Facebook Placements
- **Feed** - Main news feed
- **Stories** - Full-screen vertical ads
- **Reels** - Short-form video
- **In-Stream Video** - Mid-roll video ads
- **Messenger** - Message inbox
- **Right Column** - Desktop sidebar

### Instagram Placements
- **Feed** - Main feed
- **Stories** - Full-screen vertical
- **Reels** - Short-form video
- **Explorer** - Discovery tab
- **Messenger** - Message inbox

### Audience Network
- Third-party mobile apps & websites
- Expanded reach beyond Facebook/Instagram
- Lower cost, but less control

**Placement Strategy:**
- Test all placements first
- Disable underperforming ones
- Optimize budgets on winners

---

## Budget & Bid Management

### Budget Types

**Daily Budget:** Spend limit per day (recommended)
```
$50/day = $1,500/month (~30 days)
```

**Lifetime Budget:** Total spend over campaign duration
```
$500 lifetime over 10 days = $50/day average
```

**Cost Controls:**
- **Manual CPC** - You set max cost per click
- **Target CPA** - Optimize for conversions at target cost (needs 50+ conversions)
- **Target ROAS** - Maximize revenue at target return (e-commerce)
- **Maximize Conversions** - Most conversions within budget

### CBO vs ABO Strategy

**CBO (Campaign Budget Optimization):**
- Budget set at campaign level
- Facebook auto-distributes to best ad sets
- Best for: Scaling, letting algorithm optimize
- Requires: All ad sets have similar audience size

**ABO (Ad Set Budget Optimization):**
- Budget set at ad set level
- You control distribution manually
- Best for: Testing, learning phase, specific allocation
- Requires: Active monitoring and adjustment

**When to Use Each:**
| Situation | Use |
|-----------|-----|
| Testing new audiences | ABO |
| Scaling proven winners | CBO |
| Need control over spend per audience | ABO |
| Want algorithm to find best performers | CBO |
| Different audience sizes | ABO |
| Similar audience sizes | CBO |

---

## Key Metrics

**Impressions:** How many times ad shown
**Clicks:** How many clicked
**CTR (Click-Through Rate):** Clicks / Impressions x 100%
**CPC (Cost Per Click):** Total Spend / Clicks
**CPM (Cost Per Mille):** Cost per 1,000 impressions
**Conversions:** Desired actions (purchase, signup, lead)
**CVR (Conversion Rate):** Conversions / Clicks x 100%
**CPA (Cost Per Acquisition):** Total Spend / Conversions
**ROAS (Return on Ad Spend):** Revenue / Ad Spend
**Frequency:** Impressions / Unique Reach (watch for fatigue >3-4)

### ROAS Benchmarks

```
ROAS < 1x  = Losing money
ROAS = 2x  = Breaking even (after COGS)
ROAS = 3x  = Profitable
ROAS > 5x  = Excellent
```

---

## Conversion Tracking

For detailed UTM parameters, server-side tracking, and Conversion API setup, see `references/conversion-tracking.md`.

**Quick Setup:**
1. Install Facebook Pixel on website
2. Add UTM parameters to URLs
3. Track key events (View, Add to Cart, Purchase)
4. Verify pixel firing
5. Wait for conversion data before optimizing

---

## A/B Testing & Optimization

See `references/optimization.md` for detailed A/B testing frameworks, troubleshooting low CTR/CVR, and scaling strategies.

### ICE Scoring for Test Prioritization

Rate each test 1-10 on three factors:

**ICE Score = (Impact + Confidence + Ease) / 3**

| Factor | Question |
|--------|----------|
| **Impact** | How much will this move the needle on revenue? |
| **Confidence** | How sure are you this will work? |
| **Ease** | How easy is it to implement and measure? |

**Example Prioritization:**

| Test | Impact | Confidence | Ease | ICE | Priority |
|------|--------|------------|------|-----|----------|
| New hook type | 8 | 6 | 9 | 7.7 | High |
| Landing page headline | 9 | 7 | 7 | 7.7 | High |
| CTA button color | 3 | 8 | 10 | 7.0 | Low |
| New audience segment | 8 | 5 | 8 | 7.0 | Medium |
| Video vs image | 7 | 7 | 6 | 6.7 | Medium |

### Testing Rules

- Test one variable at a time
- Run until statistical significance
- Need 100+ conversions per variant
- 2 weeks minimum
- Document everything (winners AND losers)

---

## Scaling Strategies

### Vertical Scaling

Increase budget on winning campaigns

```
Day 1:  $100/day -> ROAS 5x
Day 3:  $150/day (+50%)
Day 7:  $200/day (+33%)
Day 14: $300/day (+50%)

Monitor: If ROAS drops below 3x, reduce budget
```

### Horizontal Scaling

Duplicate winning campaigns with new audiences

```
Original:   US, Age 25-35, Interests: Fitness
Duplicate 1: Canada, Age 25-35, Interests: Fitness
Duplicate 2: US, Age 35-45, Interests: Fitness
Duplicate 3: US, Age 25-35, Lookalike 1%
```

---

## Campaign Launch Checklist

**Setup:**
- [ ] Objective selected
- [ ] Budget set (daily or lifetime)
- [ ] Naming convention applied
- [ ] Targeting configured
- [ ] Exclusions set (existing customers, employees)
- [ ] Conversion tracking installed
- [ ] UTM parameters added

**Creative:**
- [ ] 3+ ad variations created (different hooks)
- [ ] Images/videos meet specs
- [ ] Copy includes CTA
- [ ] Captions added to video
- [ ] Landing page ready and tested

**Testing:**
- [ ] Preview ads on mobile & desktop
- [ ] Verify pixel firing
- [ ] Test checkout/conversion flow
- [ ] Check spelling/links
- [ ] Confirm tracking in analytics

**Launch:**
- [ ] Campaign activated
- [ ] Monitor first 24-48 hours
- [ ] Don't touch during learning phase
- [ ] Document in tracker spreadsheet

---

## Funnel Coverage Matrix

Ensure you have ads at every stage:

| Stage | Objective | Audience | Message Focus |
|-------|-----------|----------|---------------|
| **TOFU** (Awareness) | Reach, Video Views | Cold, Broad, Interests | Problem awareness, education |
| **MOFU** (Consideration) | Traffic, Lead Gen | Warm, Engagers, Video Viewers | Solution, differentiation |
| **BOFU** (Conversion) | Conversions | Hot, Retargeting, Cart Abandoners | Urgency, proof, CTA |
| **Post-Purchase** | Engagement | Customers | Upsell, referral, retention |

---

## Additional Resources

- `references/conversion-tracking.md` - UTM parameters, Conversion API, server-side tracking
- `references/optimization.md` - A/B testing frameworks, troubleshooting, scaling
- `references/pixel-setup.md` - Facebook Pixel implementation and event tracking
- `references/competitor-research.md` - Detailed competitor analysis methodology
