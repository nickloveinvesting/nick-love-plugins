#!/usr/bin/env python3
"""
Enhanced Component Generator for React/Next.js Applications
Generates production-ready components with TypeScript, tests, and stories
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List, Dict, Optional
import re

class ComponentGenerator:
    """Generate React/Next.js components with best practices"""
    
    def __init__(self, component_name: str, target_path: str, options: Dict):
        self.component_name = component_name
        self.target_path = Path(target_path)
        self.options = options
        self.component_dir = self.target_path / 'components' / self.component_name.lower()
        
    def run(self):
        """Generate component files"""
        print(f"🚀 Generating {self.component_name} component...")
        
        self._create_directories()
        self._generate_component()
        self._generate_types()
        self._generate_test()
        self._generate_story()
        self._generate_index()
        
        print(f"✅ Component {self.component_name} generated successfully!")
        print(f"📁 Location: {self.component_dir}")
        
    def _create_directories(self):
        """Create component directory structure"""
        self.component_dir.mkdir(parents=True, exist_ok=True)
        
    def _generate_component(self):
        """Generate main component file"""
        component_template = self._get_component_template()
        
        file_path = self.component_dir / f"{self.component_name}.tsx"
        with open(file_path, 'w') as f:
            f.write(component_template)
            
    def _generate_types(self):
        """Generate TypeScript types file"""
        types_template = f'''export interface {self.component_name}Props {{
{self._generate_props_interface()}
  className?: string;
  children?: React.ReactNode;
}}

export type {self.component_name}Variant = {self._generate_variants()};
'''
        
        file_path = self.component_dir / "types.ts"
        with open(file_path, 'w') as f:
            f.write(types_template)
            
    def _generate_test(self):
        """Generate test file"""
        test_template = f'''import {{ render, screen }} from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import {{ {self.component_name} }} from './{self.component_name}';

describe('{self.component_name}', () => {{
  it('renders correctly', () => {{
    render(<{self.component_name}>Test content</{self.component_name}>);
    expect(screen.getByText('Test content')).toBeInTheDocument();
  }});

  it('applies custom className', () => {{
    render(<{self.component_name} className="custom-class">Content</{self.component_name}>);
    const element = screen.getByText('Content').closest('div');
    expect(element).toHaveClass('custom-class');
  }});

{self._generate_variant_tests()}
}});
'''
        
        file_path = self.component_dir / f"{self.component_name}.test.tsx"
        with open(file_path, 'w') as f:
            f.write(test_template)
            
    def _generate_story(self):
        """Generate Storybook story"""
        story_template = f'''import type {{ Meta, StoryObj }} from '@storybook/react';
import {{ {self.component_name} }} from './{self.component_name}';

const meta: Meta<typeof {self.component_name}> = {{
  title: 'Components/{self.component_name}',
  component: {self.component_name},
  parameters: {{
    layout: 'centered',
  }},
  tags: ['autodocs'],
  argTypes: {{
    variant: {{
      control: {{ type: 'select' }},
      options: ['primary', 'secondary', 'accent'],
    }},
    size: {{
      control: {{ type: 'select' }},
      options: ['sm', 'md', 'lg'],
    }},
  }},
}};

export default meta;
type Story = StoryObj<typeof meta>;

export const Default: Story = {{
  args: {{
    children: '{self.component_name} content',
  }},
}};

export const Primary: Story = {{
  args: {{
    variant: 'primary',
    children: 'Primary {self.component_name}',
  }},
}};
'''
        
        file_path = self.component_dir / f"{self.component_name}.stories.tsx"
        with open(file_path, 'w') as f:
            f.write(story_template)
            
    def _generate_index(self):
        """Generate index file for clean imports"""
        index_template = f'''export {{ {self.component_name} }} from './{self.component_name}';
export type {{ {self.component_name}Props }} from './types';
'''
        
        file_path = self.component_dir / "index.ts"
        with open(file_path, 'w') as f:
            f.write(index_template)
            
    def _get_component_template(self):
        """Get appropriate component template based on type"""
        component_type = self.options.get('type', 'ui')
        
        if component_type == 'form':
            return self._get_form_component_template()
        elif component_type == 'layout':
            return self._get_layout_component_template()
        else:
            return self._get_ui_component_template()
            
    def _get_ui_component_template(self):
        """Generate UI component template"""
        return f'''import React from 'react';
import {{ cn }} from '@/lib/utils';
import {{ {self.component_name}Props }} from './types';

const variants = {{
  primary: 'bg-primary text-primary-foreground hover:bg-primary/90',
  secondary: 'bg-secondary text-secondary-foreground hover:bg-secondary/80',
  accent: 'bg-accent text-accent-foreground hover:bg-accent/90',
}};

const sizes = {{
  sm: 'h-8 px-3 text-sm',
  md: 'h-10 px-4',
  lg: 'h-12 px-6 text-lg',
}};

export const {self.component_name}: React.FC<{self.component_name}Props> = ({{
  variant = 'primary',
  size = 'md',
  className,
  children,
  ...props
}}) => {{
  return (
    <div
      className={{cn(
        'inline-flex items-center justify-center rounded-md font-medium',
        'transition-colors focus-visible:outline-none focus-visible:ring-2',
        'focus-visible:ring-ring focus-visible:ring-offset-2',
        'disabled:pointer-events-none disabled:opacity-50',
        variants[variant],
        sizes[size],
        className
      )}}
      {{...props}}
    >
      {{children}}
    </div>
  );
}};
'''
        
    def _generate_props_interface(self):
        """Generate props interface based on component type"""
        component_type = self.options.get('type', 'ui')
        props = self.options.get('props', [])
        
        interface_props = []
        
        if component_type == 'ui':
            interface_props.extend([
                '  variant?: "primary" | "secondary" | "accent";',
                '  size?: "sm" | "md" | "lg";'
            ])
            
        # Add custom props
        for prop in props:
            prop_type = 'string'  # Default type
            if ':' in prop:
                prop, prop_type = prop.split(':', 1)
            interface_props.append(f'  {prop}?: {prop_type};')
            
        return '\n'.join(interface_props)
        
    def _generate_variants(self):
        """Generate variant type union"""
        return '"primary" | "secondary" | "accent"'
            
    def _generate_variant_tests(self):
        """Generate variant-specific tests"""
        return f'''
  it('renders primary variant correctly', () => {{
    render(<{self.component_name} variant="primary">Primary</{self.component_name}>);
    const element = screen.getByText('Primary');
    expect(element).toHaveClass('bg-primary');
  }});'''

def main():
    parser = argparse.ArgumentParser(description='Generate React/Next.js components')
    parser.add_argument('name', help='Component name (PascalCase)')
    parser.add_argument('--type', choices=['ui', 'form', 'layout'], default='ui',
                       help='Component type (default: ui)')
    parser.add_argument('--props', nargs='*', default=[],
                       help='Additional props (format: propName or propName:type)')
    parser.add_argument('--path', default='./src',
                       help='Target path (default: ./src)')
    
    args = parser.parse_args()
    
    # Validate component name
    if not re.match(r'^[A-Z][a-zA-Z0-9]*$', args.name):
        print("❌ Component name must be in PascalCase (e.g., ButtonCard)")
        sys.exit(1)
        
    options = {
        'type': args.type,
        'props': args.props,
    }
    
    generator = ComponentGenerator(args.name, args.path, options)
    generator.run()

if __name__ == '__main__':
    main()
