# Next.js Optimization Guide

## App Router Best Practices

### File-Based Routing Structure
```
app/
├── (dashboard)/           # Route groups (don't affect URL)
│   ├── analytics/
│   │   └── page.tsx
│   └── settings/
│       └── page.tsx
├── api/                   # API routes
│   ├── auth/
│   │   └── route.ts
│   └── users/
│       └── route.ts
├── globals.css
├── layout.tsx             # Root layout
└── page.tsx              # Home page
```

### Server and Client Components Strategy
```typescript
// app/dashboard/layout.tsx - Server Component (default)
import { Sidebar } from './sidebar';
import { Header } from './header';

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="dashboard-layout">
      <Sidebar />
      <div className="main-content">
        <Header />
        {children}
      </div>
    </div>
  );
}

// app/dashboard/analytics/page.tsx - Server Component for data fetching
import { AnalyticsClient } from './analytics-client';

async function getAnalyticsData() {
  const res = await fetch('https://api.example.com/analytics', {
    next: { revalidate: 3600 } // ISR - revalidate every hour
  });
  return res.json();
}

export default async function AnalyticsPage() {
  const data = await getAnalyticsData();
  
  return (
    <div>
      <h1>Analytics Dashboard</h1>
      <AnalyticsClient initialData={data} />
    </div>
  );
}
```

## Performance Optimization

### Image Optimization
```typescript
import Image from 'next/image';

// Optimized image component with proper sizing
export function OptimizedImage({ src, alt, ...props }) {
  return (
    <Image
      src={src}
      alt={alt}
      width={800}
      height={600}
      placeholder="blur"
      blurDataURL="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD..."
      sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
      priority={props.priority} // Only for above-the-fold images
      quality={85} // Optimal balance of quality/size
      {...props}
    />
  );
}
```

### Code Splitting and Lazy Loading
```typescript
// Dynamic imports for large components
import dynamic from 'next/dynamic';
import { Suspense } from 'react';

const HeavyChart = dynamic(() => import('./heavy-chart'), {
  loading: () => <ChartSkeleton />,
  ssr: false // Disable SSR for client-only components
});

const LazyModal = dynamic(() => import('./modal'), {
  ssr: false
});

export function Dashboard() {
  const [showModal, setShowModal] = useState(false);
  const { user } = useAuth();

  return (
    <div>
      <Suspense fallback={<ChartSkeleton />}>
        <HeavyChart />
      </Suspense>
      
      {showModal && <LazyModal onClose={() => setShowModal(false)} />}
    </div>
  );
}
```

## Core Web Vitals Optimization

### Largest Contentful Paint (LCP)
```typescript
// Optimize hero sections
export function HeroSection({ image, title, subtitle }: HeroProps) {
  return (
    <section className="hero">
      <Image
        src={image}
        alt="Hero image"
        width={1920}
        height={1080}
        priority // Critical for LCP
        placeholder="blur"
        blurDataURL="/hero-placeholder.jpg"
        sizes="100vw"
      />
      <div className="hero-content">
        <h1>{title}</h1>
        <p>{subtitle}</p>
      </div>
    </section>
  );
}

// Preload critical resources
// app/layout.tsx
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <link rel="preload" href="/fonts/inter.woff2" as="font" type="font/woff2" crossOrigin="" />
        <link rel="preload" href="/hero-image.jpg" as="image" />
      </head>
      <body>{children}</body>
    </html>
  );
}
```

### Cumulative Layout Shift (CLS)
```typescript
// Prevent layout shift with skeleton placeholders
export function ProductCard({ product }: { product: Product | null }) {
  if (!product) {
    return (
      <div className="product-card">
        <div className="w-full h-48 bg-gray-200 animate-pulse" />
        <div className="p-4 space-y-2">
          <div className="h-4 bg-gray-200 rounded animate-pulse" />
          <div className="h-4 bg-gray-200 rounded w-3/4 animate-pulse" />
        </div>
      </div>
    );
  }

  return (
    <div className="product-card">
      <Image
        src={product.image}
        alt={product.name}
        width={300}
        height={200}
        className="object-cover"
      />
      <div className="p-4">
        <h3 className="font-semibold">{product.name}</h3>
        <p className="text-gray-600">${product.price}</p>
      </div>
    </div>
  );
}
```

## Production Deployment

### Environment Configuration
```javascript
// next.config.js production optimizations
const nextConfig = {
  // Enable SWC minification
  swcMinify: true,
  
  // Optimize for production
  productionBrowserSourceMaps: false,
  
  // Security headers
  async headers() {
    return [
      {
        source: '/(.*)',
        headers: [
          {
            key: 'X-Frame-Options',
            value: 'DENY',
          },
          {
            key: 'X-Content-Type-Options',
            value: 'nosniff',
          },
          {
            key: 'Referrer-Policy',
            value: 'strict-origin-when-cross-origin',
          },
        ],
      },
    ];
  },
  
  // Image optimization
  images: {
    formats: ['image/avif', 'image/webp'],
    deviceSizes: [640, 750, 828, 1080, 1200, 1920, 2048, 3840],
    imageSizes: [16, 32, 48, 64, 96, 128, 256, 384],
  },
};

module.exports = nextConfig;
```

This optimization guide provides practical strategies for building high-performance Next.js applications that score well on Core Web Vitals and provide excellent user experiences.
