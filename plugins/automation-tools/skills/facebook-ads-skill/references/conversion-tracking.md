# Conversion Tracking

## UTM Parameters

Track campaign performance through Google Analytics with properly structured URLs.

### UTM Structure

```
https://example.com/product?
  utm_source=facebook       ← Platform
  &utm_medium=cpc          ← Traffic type
  &utm_campaign=spring-sale ← Campaign name
  &utm_content=carousel-1   ← Ad variation
  &utm_term=running-shoes   ← Keyword (optional)
```

### Parameter Definitions

**utm_source** (Required)
- facebook, instagram, tiktok, google, etc.
- Identifies where traffic came from

**utm_medium** (Required)
- cpc (cost per click ads)
- cpm (display/banner ads)
- organic, email, etc.
- Identifies traffic type

**utm_campaign** (Required)
- Marketing campaign name
- spring-sale, black-friday, new-product-launch
- Groups related ads/channels

**utm_content** (Optional)
- Ad variation identifier
- carousel-1, video-hero, image-product
- Differentiates A/B test variants

**utm_term** (Optional)
- Keyword or audience segment
- budget-running-shoes, womens-nike
- Additional targeting context

### URL Builder Example

```
Base URL: https://www.example.com/summer-sale

Full URL:
https://www.example.com/summer-sale?
utm_source=facebook&
utm_medium=cpc&
utm_campaign=summer-sale-2025&
utm_content=video-1&
utm_term=womens

Shortened (for Ads Manager):
facebook | cpc | summer-sale-2025 | video-1 | womens
```

### Best Practices

✅ Use lowercase and hyphens (not underscores)
✅ Be consistent with naming conventions
✅ Create UTM naming document for team
✅ Use URL shortener for cleaner tracking
✅ Test URLs before launching campaigns

❌ Don't use special characters or spaces
❌ Don't change UTM scheme mid-campaign
❌ Don't over-complicate parameters

---

## Google Analytics Tracking

### View Campaign Performance

**Path:** Acquisition → Campaigns → All Campaigns

**Filter by utm_campaign:**
```
utm_campaign=spring-sale
```

**Results:**
```
Sessions: 5,000
Users: 4,200
Conversions: 150
Conversion Rate: 3%
Revenue: $15,000
ROAS: 5x
```

### View Ad Variation Performance

**Path:** Acquisition → Campaigns → All Campaigns → Drill down by utm_content

```
utm_content | Sessions | Conversions | CVR | Revenue
-----------|----------|-------------|-----|--------
carousel-1 | 2,500    | 100        | 4%  | $10,000
video-1    | 2,000    | 50         | 2.5%| $5,000
image-1    | 500      | 0          | 0%  | $0
```

**Action:** Pause image-1, increase budget on carousel-1

---

## Facebook Pixel Implementation

### Base Pixel Code

Add to every page on your website:

```html
<!-- Facebook Pixel -->
<script>
  !function(f,b,e,v,n,t,s)
  {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};
  if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
  n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];
  s.parentNode.insertBefore(t,s)}(window, document,'script',
  'https://connect.facebook.net/en_US/fbevents.js');
  fbq('init', 'YOUR_PIXEL_ID');
  fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
  src="https://www.facebook.com/tr?id=YOUR_PIXEL_ID&ev=PageView&noscript=1"
/></noscript>
```

Replace `YOUR_PIXEL_ID` with your actual pixel ID.

### Standard Events

#### View Content (Product Page)

```javascript
fbq('track', 'ViewContent', {
  content_ids: ['SKU123'],
  content_type: 'product',
  value: 29.99,
  currency: 'USD'
});
```

**When to fire:** When user lands on product page

#### Add to Cart

```javascript
fbq('track', 'AddToCart', {
  content_ids: ['SKU123', 'SKU456'],
  value: 59.98,
  currency: 'USD'
});
```

**When to fire:** When user clicks "Add to Cart"

#### Initiate Checkout

```javascript
fbq('track', 'InitiateCheckout', {
  content_ids: ['SKU123'],
  value: 29.99,
  currency: 'USD'
});
```

**When to fire:** When user starts checkout process

#### Purchase (Most Important!)

```javascript
fbq('track', 'Purchase', {
  value: 29.99,
  currency: 'USD',
  content_ids: ['SKU123'],
  content_type: 'product'
});
```

**When to fire:** When user completes purchase (order confirmation page)

#### Lead

```javascript
fbq('track', 'Lead', {
  content_name: 'Email Signup',
  value: 0,
  currency: 'USD'
});
```

**When to fire:** When user submits lead form

### Pixel Verification

1. **Facebook Pixel Helper (Chrome Extension)**
   - Install extension
   - Visit website
   - Events should appear in real-time
   - Check for errors

2. **Test Conversions**
   - Go through purchase flow
   - Check pixel fires on order confirmation
   - Wait 5-10 minutes
   - Verify in Ads Manager → Pixels → Test Events

---

## Conversion API (Server-Side Tracking)

Server-side tracking bypasses browser limitations and provides more reliable conversion data.

### Why Use Conversion API?

✅ iOS 14+ privacy changes limit pixel reliability
✅ Ad blockers prevent client-side pixel firing
✅ Cookie restrictions affect data collection
✅ More accurate conversion attribution
✅ Better data for optimization

### Setup (Node.js Example)

```javascript
const bizSdk = require('facebook-nodejs-business-sdk');

const access_token = 'YOUR_ACCESS_TOKEN';
const pixel_id = 'YOUR_PIXEL_ID';

const api = bizSdk.FacebookAdsApi.init(access_token);
const ServerEvent = bizSdk.ServerEvent;
const EventRequest = bizSdk.EventRequest;

// Track purchase
const event = (new ServerEvent())
  .setEventName('Purchase')
  .setEventTime(Math.floor(Date.now() / 1000))
  .setUserData({
    email: 'user@example.com',
    phone: '5551234567',
    firstName: 'John',
    lastName: 'Doe',
    city: 'New York',
    state: 'NY',
    zipCode: '10001',
    country: 'US'
  })
  .setCustomData({
    value: 29.99,
    currency: 'USD',
    contentName: 'Running Shoes',
    contentId: 'SKU123'
  });

const request = (new EventRequest(pixel_id))
  .setEvents([event]);

request.execute();
```

### Setup (Python Example)

```python
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.serverside.event import Event
from facebook_business.adobjects.serverside.event_request import EventRequest
from facebook_business.adobjects.serverside.user_data import UserData
from facebook_business.adobjects.serverside.custom_data import CustomData

access_token = 'YOUR_ACCESS_TOKEN'
pixel_id = 'YOUR_PIXEL_ID'

api = FacebookAdsApi.init(access_token=access_token)

# Create user data
user_data = UserData(
    email='user@example.com',
    phone='5551234567',
    first_name='John',
    last_name='Doe',
    city='New York',
    state='NY',
    zip='10001',
    country='US'
)

# Create custom data
custom_data = CustomData(
    value=29.99,
    currency='USD',
    content_name='Running Shoes',
    content_id='SKU123'
)

# Create event
event = Event(
    event_name='Purchase',
    event_time=int(time.time()),
    user_data=user_data,
    custom_data=custom_data
)

# Send event
request = EventRequest(pixel_id=pixel_id, events=[event])
request.execute()
```

### User Data Fields

For better matching, include as much user data as possible:

```python
user_data = {
    'email': 'user@example.com',          # Hashed
    'phone': '5551234567',                 # Hashed
    'first_name': 'John',
    'last_name': 'Doe',
    'city': 'New York',
    'state': 'NY',
    'zip': '10001',
    'country': 'US',
    'external_id': 'customer_123',        # Your CRM ID
    'client_ip_address': '192.168.1.1',   # Server IP
    'client_user_agent': 'user-agent'     # Browser agent
}
```

### Custom Data Fields

```python
custom_data = {
    'value': 29.99,                       # Transaction value
    'currency': 'USD',                    # Currency code
    'content_name': 'Running Shoes',      # Product name
    'content_id': 'SKU123',               # Product ID
    'content_type': 'product',            # product or product_group
    'content_category': 'Footwear',       # Product category
    'num_items': 1                        # Quantity
}
```

### Implementation Checklist

- [ ] Get access token from Business Manager
- [ ] Create test event in Ads Manager
- [ ] Implement Conversion API in backend
- [ ] Test with sample purchase
- [ ] Verify events appear in Test Events tab
- [ ] Map custom fields to your data
- [ ] Deploy to production
- [ ] Monitor event delivery

---

## Attribution Models

Facebook uses different attribution models to assign credit to touchpoints.

### Last Click

Gives 100% credit to last touchpoint before conversion.
```
User journey: Ad View → Ad Click → Website → Purchase
Credit: Ad Click (100%)
```

### First Click

Gives 100% credit to first touchpoint.
```
User journey: Ad View → Ad Click → Website → Purchase
Credit: Ad View (100%)
```

### Linear

Distributes credit equally across all touchpoints.
```
User journey: Ad View → Ad Click → Website → Purchase
Credit: Ad View (33%) → Ad Click (33%) → Website (33%)
```

### Time Decay

Recent touchpoints get more credit.
```
User journey: Ad View → Ad Click → Website → Purchase
Credit: Ad View (20%) → Ad Click (30%) → Website (50%)
```

---

## Troubleshooting

**Pixel not firing:**
- Verify pixel ID is correct
- Check noscript tag placement
- Use Facebook Pixel Helper extension
- Check for JavaScript errors in console

**No conversions recorded:**
- Ensure Purchase event fires on order confirmation page
- Check value and currency parameters
- Wait 24 hours for data to sync
- Verify UTM parameters are correct

**Data discrepancies between Ads Manager and Google Analytics:**
- Attribution window differences (Facebook vs GA default)
- Time zone mismatches
- Pixel ID issues
- Cross-domain tracking setup
