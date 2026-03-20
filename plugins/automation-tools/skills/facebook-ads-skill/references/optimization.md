# Optimization & Scaling

## A/B Testing Framework

### Variables to Test

Test one variable at a time to isolate impact.

#### Headlines

```
A: "Buy Running Shoes Online"
B: "Find Your Perfect Running Shoes"
C: "Shop 1000+ Running Shoes"

Winner: B (+15% CTR)
```

**What works:**
- ✅ Benefit-driven ("Find Your Perfect")
- ✅ Number-based ("1000+", "50%")
- ✅ Question format ("Want comfort?")
- ✅ Urgency ("Limited time offer")

❌ Generic ("Shop Now")
❌ Brand-only ("Nike Store")

#### Images

```
A: Product on white background
B: Person using product
C: Lifestyle image

Winner: B (+30% CTR)
```

**What works:**
- ✅ Human faces increase engagement +30%
- ✅ Show product in action
- ✅ Bright, high-contrast colors
- ✅ Simple, clean composition

#### Video

```
A: 15-second product demo
B: 30-second customer testimonial
C: 60-second lifestyle story

Winner: B (+25% CVR)
```

**What works:**
- ✅ Hook in first 3 seconds
- ✅ Customer testimonials
- ✅ Problem-solution structure
- ✅ Clear CTA at end

#### Call-to-Action (CTA)

```
A: "Learn More"
B: "Shop Now"
C: "Get Started"

Winner: B (+20% CVR)
```

**What works:**
- ✅ Action-oriented ("Shop", "Buy", "Get")
- ✅ Specific to offer
- ✅ Verb + benefit

❌ Vague ("Click Here")
❌ Weak verbs ("Explore")

#### Copy Length

```
A: Short (15 words)
   "Beautiful shoes. Free shipping. Order today."

B: Medium (30 words)
   "Discover comfort with our premium running shoes. Free shipping on all orders. Limited time offer!"

C: Long (50 words)
   Full story about shoes, brand, value proposition, social proof, and offer

Winner: B (usually)
```

**General rule:** Mobile = shorter, Desktop = slightly longer

#### Audience

```
A: All ages 25-45
B: Age 25-35 (younger)
C: Age 35-45 (older)

Result: Age 25-35 wins with 3x ROAS
Action: Focus budget on winning age group
```

### Testing Rules

1. **Test one variable at a time**
   - Prevents confounding variables
   - Clear cause-effect relationship

2. **Statistical significance required**
   - Need 100+ conversions per variant minimum
   - 2 weeks minimum test duration
   - Avoid false positives from randomness

3. **Proper test setup**
   - Equal budget allocation
   - Similar traffic distribution
   - Same time period
   - Exclude personal interactions

4. **Documentation**
   - Record test date, variables, results
   - Keep organized for future reference
   - Share learnings with team

### Winning Formulas

**Awareness Campaign (Build reach):**
- Benefit-driven headlines
- Lifestyle/aspirational images
- Customer testimonials
- Target: 20%+ brand recall

**Consideration Campaign (Engagement):**
- Question-based headlines
- Product-in-use images
- Educational video content
- Target: High engagement rate

**Conversion Campaign (Sales):**
- Action-oriented CTAs
- Social proof/urgency
- Clear value proposition
- Specific to offer/discount
- Target: High CVR and ROAS

---

## Troubleshooting Low Performance

### Low CTR (< 1%)

**Problem:** Ad creative is boring or not resonating

**Diagnosis:**
- Check Relevance Score (lower than 6 = problem)
- Review ad creative quality
- Compare to historical CTR

**Solutions:**

1. **Refresh Creative**
   - Design new images
   - Shoot new video
   - Write new copy
   - Test new format (video → carousel)

2. **Improve Headline**
   - Add benefit ("Find Your Perfect...")
   - Use power words ("Discover", "Unlock")
   - Add number ("50% off", "1000+")

3. **Add Urgency**
   - "Limited time only"
   - "Sale ends Friday"
   - "Only 5 spots left"

4. **Tighten Targeting**
   - More relevant audience = higher CTR
   - Remove broad interests
   - Focus on warm audiences

**Expected timeline:** Results within 2-3 days

---

### High CPC (> Benchmark)

**Problem:** Low ad relevance or weak landing page

**Diagnosis:**
- CPC = Budget / Clicks
- Compare to industry benchmark
- Check Quality Score

**Solutions:**

1. **Improve Ad-Landing Page Match**
   - Ad headline should match page headline
   - Ad image relevant to page content
   - Direct users to specific product (not homepage)

2. **Improve Landing Page Speed**
   - Target: < 2 seconds load time
   - Compress images
   - Enable caching
   - Minimize JavaScript

3. **Increase Relevance Score**
   - Tighter targeting (fewer, better people)
   - Better ad copy
   - More engaging creative

4. **Temporarily Increase Bid**
   - May get better placement
   - Improved position = more clicks
   - Monitor CPA to ensure profitability

**Expected timeline:** Results within 2-5 days

---

### Low CVR (< 2%)

**Problem:** Landing page or offer issue, not the ad

**Diagnosis:**
- High CTR + Low CVR = landing page problem
- Low CTR + Low CVR = ad problem
- Users clicking but not converting

**Solutions:**

1. **Optimize Landing Page**
   - Clear headline (match ad copy)
   - Product images from multiple angles
   - Compelling description (benefits, not features)
   - Reduce form fields
   - Smooth checkout

2. **Improve Offer**
   - Add guarantee ("30-day money-back")
   - Add scarcity ("50 spots left")
   - Add social proof ("5,000+ happy customers")
   - Reduce friction (fewer steps to purchase)

3. **Add Trust Signals**
   - Customer reviews/testimonials
   - Trust badges (SSL, payment security)
   - Money-back guarantee
   - Visible support (chat, phone, email)

4. **Simplify Checkout**
   - Guest checkout option
   - Multiple payment methods
   - Progress indicator
   - Error messages (clear fixes)

**Expected timeline:** Results within 3-7 days (test thoroughly before launch)

---

### No Sales (ROAS = 0)

**Problem:** Serious campaign issue or wrong audience

**Checklist:**

- [ ] Pixel firing? (Check with Pixel Helper)
- [ ] Correct audience selected?
- [ ] Budget sufficient? (Min $5-10/day for learning)
- [ ] Landing page working? (Test purchase flow)
- [ ] Product in stock?
- [ ] Checkout not broken?
- [ ] Sufficient daily traffic? (Need volume for conversions)

**Nuclear Option:**
- Pause campaign
- Fix landing page issues
- Adjust audience/budget
- Relaunch with one variable changed

---

## Scaling Strategies

### Vertical Scaling (Increase Budget on Winners)

Scale budget on profitable campaigns gradually.

**Formula:**
```
Day 1:  $100/day
Day 3:  $150/day (+50%)
Day 7:  $200/day (+33%)
Day 14: $300/day (+50%)
Day 21: $400/day (+33%)
```

**Guard Rails:**
- Only scale if ROAS > 3x
- Reduce if ROAS drops below 2x
- Increase max 50% per adjustment
- Wait 2-3 days between increases

**Expected Outcome:**
- Higher daily conversions
- Potential slight decrease in ROAS (normal)
- Monitor CPA - should stay stable

**When to Stop:**
- ROAS consistently drops below 2x
- CPA increases beyond profitability threshold
- Ad frequency too high (fatigue)

### Horizontal Scaling (New Audiences)

Duplicate winning campaigns with new audience segments.

**Process:**
1. Identify winning campaign (ROAS > 3x)
2. Clone campaign structure
3. Change audience (keep everything else)
4. Set initial budget same as original
5. Monitor performance

**New Audience Ideas:**
```
Original:
- Location: US
- Age: 25-35
- Interest: Fitness
- Budget: $300/day

Clone 1:
- Location: Canada  ← New location
- Age: 25-35
- Interest: Fitness
- Budget: $300/day

Clone 2:
- Location: US
- Age: 35-45  ← New age
- Interest: Fitness
- Budget: $300/day

Clone 3:
- Location: US
- Age: 25-35
- Interest: Health  ← New interest
- Budget: $300/day

Clone 4:
- Location: US
- Age: 25-35
- Lookalike: 1% of purchasers  ← Lookalike
- Budget: $300/day
```

**Expected Outcome:**
- New customers from untapped audiences
- Some clones outperform original
- Average ROAS slightly lower (normal)

### Channel Stacking

Scale across platforms beyond Facebook.

**Platforms to test:**
- Instagram (same audience)
- Google Ads (search + display)
- TikTok (younger demographic)
- Pinterest (visual products)
- YouTube (video content)

**Approach:**
- Start with proven creative
- Adapt to platform native format
- Test with 10% of budget
- Scale winners to 50-100% budget match

---

## Optimization Checklist

### Daily (First 48 hours)

- [ ] Campaign live and receiving budget
- [ ] Ads appearing in feed
- [ ] Pixel firing correctly
- [ ] Conversions reporting in 24 hours
- [ ] No obvious errors in messaging

### Weekly

- [ ] Review metrics (ROAS, CPA, CTR, CVR)
- [ ] Compare to benchmarks
- [ ] Pause ads with ROAS < 2x
- [ ] Increase budget on winners (+20%)
- [ ] Test new ad variations
- [ ] Check for ad fatigue (high frequency)

### Monthly

- [ ] Full campaign analysis
- [ ] Audience performance breakdown
- [ ] Creative refresh (fatigue test)
- [ ] Expand to new audiences
- [ ] Review and improve landing page
- [ ] Calculate lifetime value vs CPA
- [ ] Document learnings and wins

---

## Performance Dashboard

Track these metrics in a spreadsheet:

```
| Campaign | ROAS | CPA | CTR | CVR | Budget | Conversions | Status |
|----------|------|-----|-----|-----|--------|-------------|--------|
| Spring Sale | 5x | $25 | 2.5% | 3% | $1,000 | 40 | ✅ Scale |
| Brand Awareness | - | - | 1.2% | - | $500 | 0 | ❌ Pause |
| Retargeting | 8x | $15 | 4% | 4% | $800 | 53 | ✅ Scale |
```

### Formulas

```
ROAS = Revenue / Spend
CPA = Spend / Conversions
CTR = Clicks / Impressions
CVR = Conversions / Clicks
Frequency = Impressions / Unique Reach
```

### Red Flags

🚩 CPA increasing week-over-week
🚩 ROAS dropping below profitability
🚩 High frequency (>8) = ad fatigue
🚩 CTR dropping consistently
🚩 CVR not matching historical baseline

---

## Common Mistakes to Avoid

❌ **Not testing enough**
- Test at least 2-3 creative variations
- Set minimum spend before judging

❌ **Targeting too broad**
- Use layered interests, not single broad ones
- Narrow audiences usually outperform

❌ **Scaling too fast**
- Risk oversaturation and ad fatigue
- Max 50% budget increase at a time

❌ **Ignoring landing page quality**
- Ad can't fix a bad landing page
- Optimize landing page before scaling

❌ **Not tracking conversions**
- Pixel is essential for optimization
- Can't optimize what you don't measure

❌ **Using generic CTAs**
- "Learn More" underperforms specifics
- Use action-oriented CTAs ("Buy Now", "Sign Up")

❌ **Changing too many variables**
- Can't determine what moved the needle
- Test one element at a time
