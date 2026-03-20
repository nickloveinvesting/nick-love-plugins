# Premium Component Library & Implementation Patterns

## Tech Stack Assumptions
- **Framework**: React / Next.js
- **Styling**: Tailwind CSS 3.x/4.x
- **Components**: ShadCN/UI (where applicable)
- **Icons**: Lucide React
- **Animations**: Framer Motion (optional) or CSS transitions

## Hero Section Patterns

### Pattern 1: Asymmetric Hero with Product Shot

```tsx
export default function Hero() {
  return (
    <section className="relative bg-slate-50 overflow-hidden">
      <div className="max-w-7xl mx-auto px-6 lg:px-12 py-24 lg:py-32">
        <div className="grid lg:grid-cols-2 gap-12 lg:gap-16 items-center">
          {/* Left: Content */}
          <div>
            <div className="inline-flex items-center gap-2 px-3 py-1 bg-blue-50 text-blue-700 text-sm font-medium rounded-full mb-6">
              <span className="w-2 h-2 bg-blue-500 rounded-full"></span>
              New: AI-Powered Analytics
            </div>
            
            <h1 className="text-5xl lg:text-6xl xl:text-7xl font-bold text-slate-900 leading-tight mb-6">
              Scale Your Agency to{' '}
              <span className="text-blue-600">$50K/month</span> Without Hiring
            </h1>
            
            <p className="text-lg lg:text-xl text-slate-600 mb-8 max-w-xl">
              Automate client reporting, lead generation, and follow-ups. 
              Join 2,847 agencies saving 20+ hours per week.
            </p>
            
            <div className="flex flex-col sm:flex-row gap-4">
              <button className="px-8 py-4 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 shadow-sm transition-all duration-150">
                Start Your Free Trial
              </button>
              <button className="px-8 py-4 border-2 border-slate-300 text-slate-700 font-semibold rounded-lg hover:border-slate-400 transition-all duration-150">
                Watch 2-Min Demo →
              </button>
            </div>
            
            <div className="mt-8 flex items-center gap-6">
              <div className="flex -space-x-2">
                {[1,2,3,4].map(i => (
                  <div key={i} className="w-10 h-10 rounded-full bg-slate-300 border-2 border-white" />
                ))}
              </div>
              <div className="text-sm">
                <div className="font-semibold text-slate-900">2,847+ agencies</div>
                <div className="text-slate-600">switched this month</div>
              </div>
            </div>
          </div>
          
          {/* Right: Visual */}
          <div className="relative lg:pl-8">
            <div className="relative rounded-xl overflow-hidden shadow-2xl border border-slate-200">
              {/* Product screenshot placeholder */}
              <div className="aspect-[4/3] bg-slate-100"></div>
            </div>
            {/* Floating metric card */}
            <div className="absolute -bottom-6 -left-6 bg-white p-4 rounded-lg shadow-lg border border-slate-200">
              <div className="text-sm text-slate-600 mb-1">Revenue Growth</div>
              <div className="text-2xl font-bold text-green-600">+127%</div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
```

### Pattern 2: Minimal Hero (Typography-Focused)

```tsx
export default function MinimalHero() {
  return (
    <section className="relative min-h-screen flex items-center justify-center bg-white px-6">
      <div className="max-w-4xl mx-auto text-center">
        <h1 className="text-6xl lg:text-8xl font-bold text-slate-900 leading-none mb-8 tracking-tight">
          Premium Landing Pages That Actually Convert
        </h1>
        
        <p className="text-xl lg:text-2xl text-slate-600 mb-12 max-w-2xl mx-auto">
          No templates. No generic designs. Just conversion-focused landing pages 
          built specifically for your business.
        </p>
        
        <button className="px-10 py-5 bg-slate-900 text-white text-lg font-semibold rounded-lg hover:bg-slate-800 transition-colors">
          Start Your Project →
        </button>
        
        <div className="mt-16 text-sm text-slate-500">
          Trusted by 500+ high-growth startups
        </div>
      </div>
      
      {/* Subtle scroll indicator */}
      <div className="absolute bottom-12 left-1/2 -translate-x-1/2">
        <div className="w-6 h-10 border-2 border-slate-300 rounded-full flex items-start justify-center p-2">
          <div className="w-1.5 h-1.5 bg-slate-400 rounded-full animate-bounce"></div>
        </div>
      </div>
    </section>
  );
}
```

## Feature Section Patterns

### Pattern 1: Three-Column Features (Premium)

```tsx
import { Zap, Shield, BarChart3 } from 'lucide-react';

const features = [
  {
    icon: Zap,
    title: "Automated Lead Qualification",
    description: "Stop wasting time on unqualified leads. Our AI scores every lead and prioritizes the ones ready to buy."
  },
  {
    icon: Shield,
    title: "Bank-Level Security",
    description: "Enterprise-grade encryption and compliance. Your data is protected by the same security used by Fortune 500 companies."
  },
  {
    icon: BarChart3,
    title: "Real-Time Analytics",
    description: "See exactly what's working. Track conversions, ROI, and pipeline in one beautiful dashboard."
  }
];

export default function Features() {
  return (
    <section className="py-24 lg:py-32 bg-white">
      <div className="max-w-7xl mx-auto px-6 lg:px-12">
        <div className="text-center mb-16">
          <h2 className="text-4xl lg:text-5xl font-bold text-slate-900 mb-4">
            Everything you need to scale
          </h2>
          <p className="text-xl text-slate-600 max-w-2xl mx-auto">
            Built for agencies who refuse to compromise on quality
          </p>
        </div>
        
        <div className="grid md:grid-cols-3 gap-12">
          {features.map((feature, i) => (
            <div key={i} className="group">
              <div className="w-12 h-12 rounded-lg bg-blue-50 flex items-center justify-center mb-6 group-hover:bg-blue-100 transition-colors">
                <feature.icon className="w-6 h-6 text-blue-600" />
              </div>
              
              <h3 className="text-2xl font-bold text-slate-900 mb-3">
                {feature.title}
              </h3>
              
              <p className="text-slate-600 leading-relaxed">
                {feature.description}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
```

### Pattern 2: Asymmetric Feature Showcase

```tsx
export default function FeatureShowcase() {
  return (
    <section className="py-24 bg-slate-50">
      <div className="max-w-7xl mx-auto px-6 lg:px-12">
        {/* Feature 1 - Large */}
        <div className="grid lg:grid-cols-2 gap-16 items-center mb-24">
          <div>
            <div className="text-sm font-semibold text-blue-600 mb-3">
              SMART AUTOMATION
            </div>
            <h3 className="text-4xl lg:text-5xl font-bold text-slate-900 mb-6">
              Your sales team, running on autopilot
            </h3>
            <p className="text-xl text-slate-600 mb-8">
              Our AI handles lead qualification, follow-ups, and scheduling. 
              Your team focuses on closing deals, not chasing leads.
            </p>
            <ul className="space-y-4">
              {[
                "Qualify 10x more leads in the same time",
                "Never miss a follow-up or hot lead",
                "Automatic meeting scheduling and reminders"
              ].map((item, i) => (
                <li key={i} className="flex items-start gap-3">
                  <div className="w-6 h-6 rounded-full bg-green-100 flex items-center justify-center flex-shrink-0 mt-0.5">
                    <svg className="w-4 h-4 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                  </div>
                  <span className="text-slate-700">{item}</span>
                </li>
              ))}
            </ul>
          </div>
          
          <div className="relative">
            <div className="aspect-[4/3] bg-slate-200 rounded-xl"></div>
          </div>
        </div>
        
        {/* Feature 2 - Reversed */}
        <div className="grid lg:grid-cols-2 gap-16 items-center">
          <div className="lg:order-2">
            <div className="text-sm font-semibold text-blue-600 mb-3">
              ANALYTICS THAT MATTER
            </div>
            <h3 className="text-4xl lg:text-5xl font-bold text-slate-900 mb-6">
              Know your numbers at a glance
            </h3>
            <p className="text-xl text-slate-600 mb-8">
              Real-time dashboards show you exactly what's working. 
              No more guessing, no more spreadsheet hell.
            </p>
          </div>
          
          <div className="lg:order-1 relative">
            <div className="aspect-[4/3] bg-slate-200 rounded-xl"></div>
          </div>
        </div>
      </div>
    </section>
  );
}
```

## Social Proof Patterns

### Pattern 1: Testimonial Grid (No Carousel!)

```tsx
const testimonials = [
  {
    quote: "We closed $240K in new business in our first 60 days. The automated lead qualification alone saved us 25 hours per week.",
    author: "Sarah Chen",
    role: "Founder, GrowthLab Agency",
    avatar: "/avatars/sarah.jpg",
    rating: 5
  },
  // ... more testimonials
];

export default function Testimonials() {
  return (
    <section className="py-24 bg-slate-900">
      <div className="max-w-7xl mx-auto px-6 lg:px-12">
        <div className="text-center mb-16">
          <h2 className="text-4xl lg:text-5xl font-bold text-white mb-4">
            Loved by 2,847+ agencies
          </h2>
          <p className="text-xl text-slate-400">
            Real results from real businesses
          </p>
        </div>
        
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {testimonials.map((testimonial, i) => (
            <div key={i} className="bg-slate-800 rounded-xl p-8 border border-slate-700">
              {/* Star rating */}
              <div className="flex gap-1 mb-4">
                {[...Array(testimonial.rating)].map((_, i) => (
                  <svg key={i} className="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                ))}
              </div>
              
              <p className="text-slate-300 mb-6 leading-relaxed">
                "{testimonial.quote}"
              </p>
              
              <div className="flex items-center gap-3">
                <div className="w-12 h-12 rounded-full bg-slate-700" />
                <div>
                  <div className="font-semibold text-white">{testimonial.author}</div>
                  <div className="text-sm text-slate-400">{testimonial.role}</div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
```

### Pattern 2: Logo Strip + Featured Testimonial

```tsx
export default function LogoProof() {
  return (
    <section className="py-16 bg-white border-y border-slate-200">
      <div className="max-w-7xl mx-auto px-6 lg:px-12">
        <p className="text-center text-sm font-semibold text-slate-600 mb-8">
          TRUSTED BY LEADING COMPANIES
        </p>
        
        <div className="grid grid-cols-2 md:grid-cols-4 gap-8 items-center justify-items-center opacity-50 grayscale">
          {/* Logo placeholders */}
          {[1,2,3,4].map(i => (
            <div key={i} className="h-8 w-32 bg-slate-300 rounded" />
          ))}
        </div>
      </div>
    </section>
  );
}
```

## CTA Patterns

### Pattern 1: Final CTA with Risk Reversal

```tsx
export default function FinalCTA() {
  return (
    <section className="py-24 lg:py-32 bg-gradient-to-br from-blue-600 to-blue-700">
      <div className="max-w-4xl mx-auto px-6 text-center">
        <h2 className="text-4xl lg:text-5xl font-bold text-white mb-6">
          Ready to scale your agency?
        </h2>
        
        <p className="text-xl text-blue-100 mb-10">
          Join 2,847 agencies using our platform to close more deals, 
          faster, with less manual work.
        </p>
        
        <button className="px-10 py-5 bg-white text-blue-600 text-lg font-semibold rounded-lg hover:bg-blue-50 transition-colors shadow-xl mb-6">
          Start Your 14-Day Free Trial
        </button>
        
        <div className="flex flex-col sm:flex-row items-center justify-center gap-6 text-sm text-blue-100">
          <div className="flex items-center gap-2">
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
            </svg>
            No credit card required
          </div>
          <div className="flex items-center gap-2">
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
            </svg>
            14-day money-back guarantee
          </div>
          <div className="flex items-center gap-2">
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
            </svg>
            Setup in under 10 minutes
          </div>
        </div>
      </div>
    </section>
  );
}
```

## Pricing Section Pattern

```tsx
const plans = [
  {
    name: "Starter",
    price: 49,
    description: "Perfect for solo consultants",
    features: [
      "Up to 100 leads/month",
      "Basic automation",
      "Email support",
      "Core integrations"
    ]
  },
  {
    name: "Professional",
    price: 149,
    description: "Most popular for growing agencies",
    features: [
      "Unlimited leads",
      "Advanced automation",
      "Priority support",
      "All integrations",
      "Custom workflows",
      "Team collaboration"
    ],
    popular: true
  },
  {
    name: "Enterprise",
    price: 499,
    description: "For agencies at scale",
    features: [
      "Everything in Professional",
      "Dedicated account manager",
      "Custom integrations",
      "SLA guarantee",
      "Onboarding & training"
    ]
  }
];

export default function Pricing() {
  return (
    <section className="py-24 bg-slate-50">
      <div className="max-w-7xl mx-auto px-6 lg:px-12">
        <div className="text-center mb-16">
          <h2 className="text-4xl lg:text-5xl font-bold text-slate-900 mb-4">
            Simple, transparent pricing
          </h2>
          <p className="text-xl text-slate-600">
            Start free, upgrade as you grow
          </p>
        </div>
        
        <div className="grid md:grid-cols-3 gap-8">
          {plans.map((plan, i) => (
            <div 
              key={i} 
              className={`relative rounded-2xl p-8 ${
                plan.popular 
                  ? 'bg-slate-900 text-white ring-4 ring-blue-600 scale-105' 
                  : 'bg-white border border-slate-200'
              }`}
            >
              {plan.popular && (
                <div className="absolute -top-4 left-1/2 -translate-x-1/2">
                  <div className="px-4 py-1 bg-blue-600 text-white text-sm font-semibold rounded-full">
                    Most Popular
                  </div>
                </div>
              )}
              
              <div className="mb-6">
                <h3 className="text-2xl font-bold mb-2">{plan.name}</h3>
                <p className={plan.popular ? 'text-slate-300' : 'text-slate-600'}>
                  {plan.description}
                </p>
              </div>
              
              <div className="mb-8">
                <span className="text-5xl font-bold">${plan.price}</span>
                <span className={plan.popular ? 'text-slate-300' : 'text-slate-600'}>
                  /month
                </span>
              </div>
              
              <button 
                className={`w-full py-3 rounded-lg font-semibold transition-colors mb-8 ${
                  plan.popular
                    ? 'bg-blue-600 text-white hover:bg-blue-700'
                    : 'bg-slate-900 text-white hover:bg-slate-800'
                }`}
              >
                Start Free Trial
              </button>
              
              <ul className="space-y-3">
                {plan.features.map((feature, j) => (
                  <li key={j} className="flex items-start gap-3">
                    <svg 
                      className={`w-5 h-5 flex-shrink-0 mt-0.5 ${
                        plan.popular ? 'text-blue-400' : 'text-green-600'
                      }`} 
                      fill="none" 
                      stroke="currentColor" 
                      viewBox="0 0 24 24"
                    >
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                    <span className={plan.popular ? 'text-slate-300' : 'text-slate-600'}>
                      {feature}
                    </span>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
```

## FAQ Pattern

```tsx
'use client';
import { useState } from 'react';
import { ChevronDown } from 'lucide-react';

const faqs = [
  {
    q: "How is this different from [competitor]?",
    a: "Unlike generic CRMs, we're built specifically for agencies. Our automation handles the entire lead qualification process, not just data storage."
  },
  // ... more FAQs
];

export default function FAQ() {
  const [open, setOpen] = useState<number | null>(0);
  
  return (
    <section className="py-24 bg-white">
      <div className="max-w-3xl mx-auto px-6">
        <h2 className="text-4xl font-bold text-slate-900 text-center mb-16">
          Frequently asked questions
        </h2>
        
        <div className="space-y-4">
          {faqs.map((faq, i) => (
            <div 
              key={i} 
              className="border border-slate-200 rounded-lg overflow-hidden"
            >
              <button
                onClick={() => setOpen(open === i ? null : i)}
                className="w-full px-6 py-5 text-left flex items-center justify-between hover:bg-slate-50 transition-colors"
              >
                <span className="font-semibold text-slate-900 pr-4">
                  {faq.q}
                </span>
                <ChevronDown 
                  className={`w-5 h-5 text-slate-600 transition-transform flex-shrink-0 ${
                    open === i ? 'rotate-180' : ''
                  }`}
                />
              </button>
              
              {open === i && (
                <div className="px-6 pb-5 text-slate-600 leading-relaxed">
                  {faq.a}
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
```

## Implementation Best Practices

### 1. Consistent Component Patterns
```tsx
// Create reusable components
const Button = ({ variant = 'primary', children, ...props }) => {
  const variants = {
    primary: 'px-8 py-4 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition-colors',
    secondary: 'px-8 py-4 border-2 border-slate-300 text-slate-700 font-semibold rounded-lg hover:border-slate-400 transition-colors'
  };
  
  return (
    <button className={variants[variant]} {...props}>
      {children}
    </button>
  );
};
```

### 2. Design Tokens
```tsx
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#f0f9ff',
          // ... your brand colors
          900: '#0c4a6e',
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        display: ['Cal Sans', 'Inter', 'sans-serif'],
      },
      boxShadow: {
        'premium': '0 4px 6px -1px rgb(0 0 0 / 0.05), 0 2px 4px -2px rgb(0 0 0 / 0.02)',
      }
    }
  }
}
```

### 3. Smooth Transitions
```tsx
// Add to global CSS or component
.smooth-transition {
  @apply transition-all duration-150 ease-in-out;
}

// Usage in components
className="transform hover:scale-102 hover:shadow-lg smooth-transition"
```

### 4. Responsive Patterns
```tsx
// Mobile-first approach
<div className="
  px-6 py-16          /* Mobile */
  md:px-8 md:py-20    /* Tablet */
  lg:px-12 lg:py-24   /* Desktop */
  xl:px-16 xl:py-32   /* Wide */
">
```

## Common Mistakes to Avoid

### ❌ Don't Do This:
```tsx
// Random spacing
<div className="p-7 mb-11 mt-5">

// Inline styles mixed with Tailwind
<div className="p-4" style={{ marginTop: '23px' }}>

// Multiple competing gradients
<div className="bg-gradient-to-r from-purple-500 via-pink-500 to-orange-500">
```

### ✅ Do This Instead:
```tsx
// Consistent 8pt spacing
<div className="p-8 mb-12 mt-6">

// Pure Tailwind
<div className="p-4 mt-6">

// Solid backgrounds
<div className="bg-slate-50">
```
