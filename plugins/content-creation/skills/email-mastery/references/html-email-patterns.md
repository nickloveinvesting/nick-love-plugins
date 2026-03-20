# HTML Email Design Patterns Reference

All examples use table-based layouts. No divs, no flexbox, no grid. Email clients don't support modern CSS.

---

## Master Container Template

Every email starts with this:

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Email Title</title>
</head>
<body style="margin: 0; padding: 0; background-color: #f8fafc;">

<!-- Master container -->
<table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="min-width: 100%;">
  <tr>
    <td align="center" style="padding: 0;">

      <!-- Content wrapper (600px max width) -->
      <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="600" style="max-width: 600px; width: 100%;">
        
        <!-- CONTENT GOES HERE -->
        
      </table>

    </td>
  </tr>
</table>

</body>
</html>
```

---

## Hero Section Pattern

```html
<table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
  <tr>
    <td style="background-color: #0f172a; padding: 60px 40px; text-align: center;">
      <h1 style="margin: 0 0 16px 0; color: #ffffff; font-family: Georgia, serif; font-size: 36px; font-weight: 700; line-height: 1.3;">
        Your Headline Here
      </h1>
      <p style="margin: 0 0 32px 0; color: #94a3b8; font-family: Arial, sans-serif; font-size: 16px; line-height: 1.5;">
        Supporting subheadline that expands on the main benefit
      </p>
      <table role="presentation" cellspacing="0" cellpadding="0" border="0">
        <tr>
          <td style="background-color: #3b82f6; padding: 14px 32px; text-align: center;">
            <a href="https://yoururl.com/action" style="color: #ffffff; font-family: Arial, sans-serif; font-size: 16px; font-weight: bold; text-decoration: none; display: inline-block;">
              Click to Action
            </a>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

---

## Two-Column Section (Features)

```html
<table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
  <tr>
    <td align="center" style="padding: 40px 20px;">

      <!--[if mso]>
      <table role="presentation" width="560" cellspacing="0" cellpadding="0" border="0" align="center">
      <tr>
      <td width="270">
      <![endif]-->

      <div style="display: inline-block; max-width: 270px; width: 100%; vertical-align: top;">
        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
          <tr>
            <td style="padding: 0 15px 30px 0; text-align: left;">
              <h3 style="margin: 0 0 8px 0; font-family: Arial, sans-serif; font-size: 18px; font-weight: 600; color: #0f172a;">
                Feature 1
              </h3>
              <p style="margin: 0; font-family: Arial, sans-serif; font-size: 15px; color: #64748b; line-height: 1.5;">
                Description of your feature and the benefit
              </p>
            </td>
          </tr>
        </table>
      </div>

      <!--[if mso]>
      </td>
      <td width="270">
      <![endif]-->

      <div style="display: inline-block; max-width: 270px; width: 100%; vertical-align: top;">
        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
          <tr>
            <td style="padding: 0 0 30px 15px; text-align: left;">
              <h3 style="margin: 0 0 8px 0; font-family: Arial, sans-serif; font-size: 18px; font-weight: 600; color: #0f172a;">
                Feature 2
              </h3>
              <p style="margin: 0; font-family: Arial, sans-serif; font-size: 15px; color: #64748b; line-height: 1.5;">
                Description of your feature and the benefit
              </p>
            </td>
          </tr>
        </table>
      </div>

      <!--[if mso]>
      </td>
      </tr>
      </table>
      <![endif]-->

    </td>
  </tr>
</table>
```

---

## Centered Icon + Text (Feature Card)

```html
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="text-align: center; margin-bottom: 32px;">
  <tr>
    <td align="center" style="padding-bottom: 16px;">
      <table role="presentation" cellspacing="0" cellpadding="0" border="0">
        <tr>
          <td width="56" height="56" style="background-color: #6366f1; text-align: center; vertical-align: middle;">
            <img src="https://cdn-icons-png.flaticon.com/128/2989/2989988.png" width="28" height="28" alt="" style="display: block; margin: 0 auto;">
          </td>
        </tr>
      </table>
    </td>
  </tr>
  <tr>
    <td align="center">
      <h3 style="margin: 0 0 8px 0; font-family: Arial, sans-serif; font-size: 20px; font-weight: 600; color: #0f172a;">
        Feature Title
      </h3>
      <p style="margin: 0; font-family: Arial, sans-serif; font-size: 15px; color: #64748b; line-height: 1.6;">
        Description of what this feature does and why it matters
      </p>
    </td>
  </tr>
</table>
```

---

## Full-Width Image + Text

```html
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="margin-bottom: 32px;">
  <tr>
    <td style="padding: 0;">
      <img src="[IMAGE_URL]" width="600" height="300" alt="Feature" style="display: block; width: 100%; height: auto;">
    </td>
  </tr>
  <tr>
    <td style="padding: 24px 20px 0 20px;">
      <h3 style="margin: 0 0 12px 0; font-family: Arial, sans-serif; font-size: 24px; font-weight: 700; color: #0f172a;">
        Feature Title
      </h3>
      <p style="margin: 0; font-family: Arial, sans-serif; font-size: 16px; color: #4a4a4a; line-height: 1.6;">
        Description here...
      </p>
    </td>
  </tr>
</table>
```

---

## Testimonial Section

```html
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
  <tr>
    <td style="background-color: #f8fafc; padding: 32px 24px; border-left: 4px solid #3b82f6;">
      <p style="margin: 0 0 16px 0; font-family: Georgia, serif; font-size: 16px; color: #1c1917; line-height: 1.6; font-style: italic;">
        "This was the exact system I needed. Results within 30 days. Couldn't recommend higher."
      </p>
      <p style="margin: 0; font-family: Arial, sans-serif; font-size: 14px; font-weight: 600; color: #0f172a;">
        — John Smith, Real Estate Investor
      </p>
    </td>
  </tr>
</table>
```

---

## CTA Section (Multiple Options)

### Button-Only CTA
```html
<table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
  <tr>
    <td align="center" style="padding: 40px 0;">
      <table role="presentation" cellspacing="0" cellpadding="0" border="0">
        <tr>
          <td style="background-color: #ea580c; padding: 16px 40px; text-align: center;">
            <a href="https://yoururl.com/action" style="color: #ffffff; font-family: Arial, sans-serif; font-size: 16px; font-weight: bold; text-decoration: none; display: inline-block;">
              Claim Your Spot
            </a>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

### Text + Link CTA
```html
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
  <tr>
    <td style="padding: 20px 0; text-align: center;">
      <p style="margin: 0; font-family: Arial, sans-serif; font-size: 15px; color: #0f172a;">
        Ready to get started?
        <a href="https://yoururl.com/action" style="color: #3b82f6; text-decoration: underline;">
          Click here to claim your spot
        </a>
      </p>
    </td>
  </tr>
</table>
```

---

## Footer Section

```html
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
  <tr>
    <td style="border-top: 1px solid #e5e7eb; padding: 32px 20px; text-align: center;">
      <p style="margin: 0 0 12px 0; font-family: Arial, sans-serif; font-size: 13px; color: #78716c;">
        [Company Name]<br>
        [Address]<br>
        [City, State ZIP]
      </p>
      <p style="margin: 0; font-family: Arial, sans-serif; font-size: 12px; color: #a8a29e;">
        <a href="https://yoururl.com/unsubscribe" style="color: #a8a29e; text-decoration: underline;">
          Unsubscribe
        </a> | 
        <a href="https://yoururl.com/preferences" style="color: #a8a29e; text-decoration: underline;">
          Preferences
        </a>
      </p>
    </td>
  </tr>
</table>
```

---

## Verified Flaticon CDN Icon URLs

### Business/Professional Icons
- Checkmark: https://cdn-icons-png.flaticon.com/128/2989/2989988.png
- Star: https://cdn-icons-png.flaticon.com/128/1828/1828884.png
- Lightning: https://cdn-icons-png.flaticon.com/128/3313/3313031.png
- Shield: https://cdn-icons-png.flaticon.com/128/2889/2889676.png
- Chart/Growth: https://cdn-icons-png.flaticon.com/128/3135/3135706.png
- Rocket: https://cdn-icons-png.flaticon.com/128/3135/3135715.png
- Target: https://cdn-icons-png.flaticon.com/128/3207/3207586.png
- Clock/Time: https://cdn-icons-png.flaticon.com/128/2784/2784459.png
- Gift: https://cdn-icons-png.flaticon.com/128/3131/3131978.png
- Heart: https://cdn-icons-png.flaticon.com/128/833/833472.png
- Settings: https://cdn-icons-png.flaticon.com/128/3524/3524659.png
- User/Profile: https://cdn-icons-png.flaticon.com/128/1077/1077114.png
- Mail/Message: https://cdn-icons-png.flaticon.com/128/561/561127.png

### Social Media Icons
- LinkedIn: https://cdn-icons-png.flaticon.com/128/3536/3536505.png
- Twitter/X: https://cdn-icons-png.flaticon.com/128/5968/5968830.png
- Facebook: https://cdn-icons-png.flaticon.com/128/733/733547.png
- Instagram: https://cdn-icons-png.flaticon.com/128/2111/2111463.png

---

## Design System Color Variables

### Dark Elegant (Tech/SaaS)
```css
background-color: #0f172a;  /* Dark navy */
surface: #1e293b;           /* Slightly lighter navy */
primary-text: #f8fafc;      /* Almost white */
muted-text: #94a3b8;        /* Gray */
accent: #3b82f6;            /* Blue */
```

### Warm Professional (Real Estate)
```css
background-color: #fef7ed;  /* Warm cream */
surface: #ffffff;           /* White */
primary-text: #1c1917;      /* Dark brown */
muted-text: #78716c;        /* Warm gray */
accent: #ea580c;            /* Orange */
```

### Professional Clean (Finance)
```css
background-color: #f8fafc;  /* Light blue-gray */
surface: #ffffff;           /* White */
primary-text: #0f172a;      /* Dark navy */
muted-text: #64748b;        /* Gray */
accent: #0d9488;            /* Teal */
```

---

## Section Separation Best Practices

Every section must have VISUAL separation:

```html
<!-- Section 1 (White background) -->
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
  <tr>
    <td style="background-color: #ffffff; padding: 40px 20px;">
      [Content]
    </td>
  </tr>
</table>

<!-- Spacer -->
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
  <tr>
    <td height="20" style="font-size: 1px; line-height: 1px;">&nbsp;</td>
  </tr>
</table>

<!-- Section 2 (Light gray background - DIFFERENT COLOR) -->
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
  <tr>
    <td style="background-color: #f8fafc; padding: 40px 20px;">
      [Content]
    </td>
  </tr>
</table>
```

---

## Email Preview in Code

Test in browser with this HTML wrapper:

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Email Preview</title>
</head>
<body style="margin: 0; padding: 20px; background-color: #f0f0f0;">

<!-- Email container (center in viewport) -->
<div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border: 1px solid #ddd;">

[PASTE YOUR ENTIRE EMAIL HERE]

</div>

</body>
</html>
```

---

## Outlook-Specific MSO Conditionals

Outlook 2007-2016 requires explicit widths. Template:

```html
<!--[if mso]>
<table role="presentation" width="600" align="center" cellspacing="0" cellpadding="0" border="0">
<tr>
<td width="300">
<![endif]-->

<div style="display: inline-block; max-width: 300px; width: 100%; vertical-align: top;">
  <!-- Content -->
</div>

<!--[if mso]>
</td>
<td width="300">
<![endif]-->

<div style="display: inline-block; max-width: 300px; width: 100%; vertical-align: top;">
  <!-- Content -->
</div>

<!--[if mso]>
</td>
</tr>
</table>
<![endif]-->
```

---

## Pre-Flight Checklist

- [ ] All tables have role="presentation" cellspacing="0" cellpadding="0" border="0"
- [ ] All images have alt text, width, height, style="display:block;"
- [ ] All styles are inline (no `<style>` block)
- [ ] No margin, float, position, flexbox, or grid
- [ ] MSO conditionals wrap multi-column layouts
- [ ] Font stacks include web-safe fallbacks
- [ ] Total HTML < 102KB
- [ ] All links have full URLs (not relative)
- [ ] Buttons use table-based bulletproof pattern
- [ ] NO emojis
- [ ] Tested in Gmail, Outlook, Apple Mail, mobile
- [ ] Images optimized (< 100KB total)
- [ ] No third-party fonts (web-safe only)
