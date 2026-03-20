# Facebook Pixel Setup

## Implementation Overview

Facebook Pixel is a tracking code that collects data about visitor actions on your website.

### Benefits

✅ Track conversions from ads
✅ Build audiences for retargeting
✅ Measure ROI of campaigns
✅ Optimize for conversions
✅ Create lookalike audiences

### Installation Steps

1. **Get Pixel ID**
   - Go to Ads Manager
   - Settings → Pixels
   - Create new pixel or copy existing ID

2. **Add Base Code to Website**
   - Add to `<head>` section (before closing tag)
   - Should be on every page

3. **Verify Installation**
   - Use Facebook Pixel Helper (Chrome extension)
   - Visit website and check for events

4. **Set Up Events**
   - Track specific actions (purchase, signup, etc.)
   - Place event code on relevant pages

---

## Base Pixel Code

Place this in the `<head>` of every page:

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

<!-- Noscript Version (Backup) -->
<noscript>
  <img height="1" width="1" style="display:none"
    src="https://www.facebook.com/tr?id=YOUR_PIXEL_ID&ev=PageView&noscript=1"
  />
</noscript>
```

**Important:** Replace `YOUR_PIXEL_ID` with your actual pixel ID

---

## Event Tracking

### Purchase Event (Most Important)

**When:** On order confirmation page (after payment processed)

**Code:**
```html
<script>
fbq('track', 'Purchase', {
  value: 99.99,
  currency: 'USD',
  content_ids: ['SKU123', 'SKU456'],
  content_type: 'product',
  content_name: 'Nike Running Shoes'
});
</script>
```

**Parameters:**
- `value` - Order total in decimal (e.g., 99.99)
- `currency` - 3-letter currency code (USD, GBP, EUR, etc.)
- `content_ids` - Array of product IDs purchased
- `content_type` - 'product' or 'product_group'
- `content_name` - Friendly name of item purchased

**Example Setup:**
```html
<!-- Order confirmation page -->
<script>
fbq('track', 'Purchase', {
  value: parseFloat(document.getElementById('orderTotal').textContent),
  currency: 'USD',
  content_ids: [document.getElementById('productId').textContent],
  content_type: 'product'
});
</script>
```

### View Content (Product Page)

**When:** User lands on product page

**Code:**
```html
<script>
fbq('track', 'ViewContent', {
  content_ids: ['SKU123'],
  content_type: 'product',
  content_name: 'Nike Running Shoes',
  value: 99.99,
  currency: 'USD',
  content_category: 'Footwear'
});
</script>
```

**Parameters:**
- `content_ids` - Product ID
- `content_type` - 'product' or 'product_group'
- `content_name` - Product name
- `value` - Product price
- `currency` - Currency code
- `content_category` - Product category

**Example Setup:**
```html
<!-- Product page -->
<script>
fbq('track', 'ViewContent', {
  content_ids: [document.getElementById('sku').textContent],
  content_type: 'product',
  content_name: document.getElementById('productName').textContent,
  value: parseFloat(document.getElementById('price').textContent),
  currency: 'USD',
  content_category: document.getElementById('category').textContent
});
</script>
```

### Add to Cart

**When:** User clicks "Add to Cart"

**Code:**
```html
<script>
fbq('track', 'AddToCart', {
  content_ids: ['SKU123'],
  content_type: 'product',
  value: 99.99,
  currency: 'USD'
});
</script>
```

### Initiate Checkout

**When:** User clicks "Checkout" or enters checkout flow

**Code:**
```html
<script>
fbq('track', 'InitiateCheckout', {
  content_ids: ['SKU123', 'SKU456'],
  content_type: 'product',
  value: 199.98,
  currency: 'USD'
});
</script>
```

### Lead

**When:** User submits lead form (email signup, contact form, etc.)

**Code:**
```html
<script>
fbq('track', 'Lead', {
  content_name: 'Email Signup',
  content_category: 'Newsletter',
  currency: 'USD',
  value: 0
});
</script>
```

**Example Setup:**
```html
<!-- After form submission -->
<script>
fbq('track', 'Lead', {
  content_name: document.getElementById('formName').value,
  currency: 'USD'
});
</script>
```

### Complete Registration

**When:** User completes signup/registration

**Code:**
```html
<script>
fbq('track', 'CompleteRegistration', {
  content_name: 'Account Signup',
  status: 'completed'
});
</script>
```

### Search

**When:** User performs a search on site

**Code:**
```html
<script>
fbq('track', 'Search', {
  search_string: 'running shoes',
  content_category: 'Footwear'
});
</script>
```

---

## Custom Events

Track specific actions unique to your business.

**Format:**
```javascript
fbq('trackCustom', 'CustomEventName', {
  param1: 'value1',
  param2: 'value2'
});
```

**Examples:**

```javascript
// Video play
fbq('trackCustom', 'VideoPlay', {
  video_name: 'Product Demo',
  video_duration: 120
});

// Download
fbq('trackCustom', 'Download', {
  file_name: 'Pricing Guide',
  file_type: 'PDF'
});

// Newsletter subscription
fbq('trackCustom', 'NewsletterSignup', {
  frequency: 'weekly'
});
```

---

## Dynamic Pixel Events

Track events dynamically based on page data.

### Example: Dynamic Purchase Tracking

```javascript
// On order confirmation page
(function() {
  // Get order data from page
  const orderData = {
    total: document.querySelector('[data-order-total]').textContent,
    items: document.querySelectorAll('[data-product-id]'),
    ids: []
  };
  
  // Collect product IDs
  orderData.items.forEach(item => {
    orderData.ids.push(item.getAttribute('data-product-id'));
  });
  
  // Track purchase
  fbq('track', 'Purchase', {
    value: parseFloat(orderData.total),
    currency: 'USD',
    content_ids: orderData.ids,
    content_type: 'product'
  });
})();
```

### Example: Dynamic Page View Category

```javascript
// Track content category
const category = document.body.getAttribute('data-category');
fbq('track', 'ViewContent', {
  content_category: category
});
```

---

## Verification & Testing

### Facebook Pixel Helper (Chrome)

1. Install extension from Chrome Web Store
2. Click extension icon on website
3. Watch for events firing
4. Check for errors (red = problems)

**Good signs:**
✅ PageView fires on load
✅ Purchase fires on order confirmation
✅ Events appear within 1-2 seconds

**Bad signs:**
🚩 No events firing
🚩 Pixel ID mismatch error
🚩 Duplicate base code
🚩 JavaScript errors

### Test Event in Ads Manager

1. Go to Ads Manager → Settings → Pixels
2. Select your pixel
3. Click "Test Events"
4. Get test code to add to page
5. Make test purchase/action
6. Events appear in real-time

### Verification Checklist

- [ ] Base pixel code on every page
- [ ] No duplicate pixel codes
- [ ] Events firing on correct pages
- [ ] Correct parameters passed
- [ ] Test events working
- [ ] 24 hours for data to populate
- [ ] Verify in Ads Manager data

---

## Common Issues & Fixes

### Pixel Not Firing

**Problem:** No events detected

**Solutions:**
1. Check Pixel Helper - does it show base pixel?
2. Verify Pixel ID is correct
3. Check for JavaScript errors (Console)
4. Ensure noscript tag included
5. Clear browser cache and reload

### Duplicate Events

**Problem:** Events firing twice

**Solutions:**
1. Check for duplicate base code
2. Check for multiple pixel tags
3. Check for tracking tag manager conflicts
4. Remove duplicate tags

### Wrong Currency

**Problem:** Events recording wrong currency

**Solution:**
Ensure all events use correct 3-letter code:
- USD (US Dollar)
- EUR (Euro)
- GBP (British Pound)
- CAD (Canadian Dollar)
- AUD (Australian Dollar)

### No Conversions Data

**Problem:** Conversions show 0

**Solutions:**
1. Verify Purchase event fires on order confirmation
2. Check parameters are correct
3. Wait 24 hours for data to sync
4. Verify UTM parameters correct in ads
5. Check if users have JavaScript enabled

---

## Best Practices

✅ Always use `fbq('track', 'PageView')` on every page
✅ Include all relevant parameters in events
✅ Place base code in `<head>` section
✅ Test thoroughly before scaling
✅ Monitor pixel health weekly
✅ Use Test Events feature during setup
✅ Document pixel implementation
✅ Update to latest pixel code periodically

❌ Don't use placeholder values
❌ Don't hardcode pixel ID (use variable)
❌ Don't forget currency parameter
❌ Don't place events in wrong location
❌ Don't ignore Pixel Helper warnings
