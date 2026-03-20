#!/usr/bin/env python3
"""
Bundle Analyzer for Next.js/React Applications
Analyzes webpack bundles and provides optimization recommendations
"""

import os
import sys
import json
import argparse
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Tuple

class BundleAnalyzer:
    """Analyze webpack bundles for optimization opportunities"""
    
    def __init__(self, target_path: str, verbose: bool = False):
        self.target_path = Path(target_path)
        self.verbose = verbose
        self.results = {}
        self.package_json_path = None
        
    def run(self) -> Dict:
        """Execute bundle analysis"""
        print("🔍 Analyzing bundle...")
        print(f"📁 Target: {self.target_path}")
        
        try:
            self._validate_project()
            self._analyze_package_json()
            self._analyze_build_output()
            self._analyze_dependencies()
            self._generate_recommendations()
            self._generate_report()
            
            print("✅ Analysis completed successfully!")
            return self.results
            
        except Exception as e:
            print(f"❌ Error: {e}")
            sys.exit(1)
    
    def _validate_project(self):
        """Validate that this is a valid Next.js/React project"""
        if not self.target_path.exists():
            raise ValueError(f"Target path does not exist: {self.target_path}")
        
        # Look for package.json
        self.package_json_path = self.target_path / "package.json"
        if not self.package_json_path.exists():
            raise ValueError("package.json not found - not a valid Node.js project")
        
        if self.verbose:
            print(f"✓ Project validated: {self.target_path}")
    
    def _analyze_package_json(self):
        """Analyze package.json for dependencies and scripts"""
        with open(self.package_json_path, 'r') as f:
            package_data = json.load(f)
        
        dependencies = package_data.get('dependencies', {})
        dev_dependencies = package_data.get('devDependencies', {})
        scripts = package_data.get('scripts', {})
        
        # Analyze dependency sizes and versions
        dependency_issues = self._check_dependency_issues(dependencies, dev_dependencies)
        
        self.results['package_analysis'] = {
            'total_dependencies': len(dependencies),
            'total_dev_dependencies': len(dev_dependencies),
            'dependency_issues': dependency_issues,
            'has_next': 'next' in dependencies,
            'has_react': 'react' in dependencies,
            'has_typescript': 'typescript' in dev_dependencies
        }
        
        if self.verbose:
            print(f"✓ Dependencies analyzed: {len(dependencies)} prod, {len(dev_dependencies)} dev")
    
    def _analyze_build_output(self):
        """Analyze build output directory"""
        build_dirs = ['.next', 'out', 'build', 'dist']
        build_path = None
        
        for build_dir in build_dirs:
            potential_path = self.target_path / build_dir
            if potential_path.exists():
                build_path = potential_path
                break
        
        if not build_path:
            self.results['build_analysis'] = {
                'has_build': False,
                'recommendation': 'Run `npm run build` to generate build output for analysis'
            }
            return
        
        # Analyze build size
        total_size = self._calculate_directory_size(build_path)
        
        self.results['build_analysis'] = {
            'has_build': True,
            'build_path': str(build_path),
            'total_size_mb': round(total_size / (1024 * 1024), 2),
        }
        
        if self.verbose:
            print(f"✓ Build analyzed: {self.results['build_analysis']['total_size_mb']} MB total")
    
    def _analyze_dependencies(self):
        """Analyze dependencies for optimization opportunities"""
        try:
            with open(self.package_json_path, 'r') as f:
                package_data = json.load(f)
            
            dependencies = package_data.get('dependencies', {})
            
            # Analyze for heavy dependencies
            heavy_deps = self._identify_heavy_dependencies(dependencies)
            
            self.results['dependency_analysis'] = {
                'heavy_dependencies': heavy_deps,
                'total_installed': len(dependencies)
            }
                
        except Exception as e:
            self.results['dependency_analysis'] = {
                'error': f'Dependency analysis failed: {str(e)}'
            }
        
        if self.verbose:
            print("✓ Dependencies analyzed")
    
    def _check_dependency_issues(self, deps: Dict, dev_deps: Dict) -> List[str]:
        """Check for common dependency issues"""
        issues = []
        
        # Known heavy dependencies
        heavy_deps = [
            'moment', 'lodash', 'antd', 'material-ui', '@mui/material',
        ]
        
        for dep in heavy_deps:
            if dep in deps:
                if dep == 'moment':
                    issues.append(f"Consider replacing {dep} with date-fns or dayjs for smaller bundle")
                elif dep == 'lodash':
                    issues.append(f"Consider using lodash-es or individual lodash functions")
                else:
                    issues.append(f"Large dependency detected: {dep}")
        
        return issues
    
    def _identify_heavy_dependencies(self, dependencies: Dict) -> List[Dict]:
        """Identify dependencies that might be heavy"""
        known_heavy = {
            'moment': 'Large date library',
            'lodash': 'Large utility library', 
            'antd': 'Large UI component library',
            '@mui/material': 'Large Material-UI library',
            'three': 'Large 3D graphics library'
        }
        
        heavy_deps = []
        for dep, description in known_heavy.items():
            if dep in dependencies:
                heavy_deps.append({
                    'name': dep,
                    'description': description
                })
        
        return heavy_deps
    
    def _generate_recommendations(self):
        """Generate optimization recommendations"""
        recommendations = []
        
        # Bundle size recommendations
        if 'build_analysis' in self.results and self.results['build_analysis'].get('has_build'):
            size_mb = self.results['build_analysis']['total_size_mb']
            
            if size_mb > 10:
                recommendations.append({
                    'type': 'bundle_size',
                    'priority': 'high',
                    'message': f'Large bundle size ({size_mb}MB). Consider code splitting and lazy loading.'
                })
            elif size_mb > 5:
                recommendations.append({
                    'type': 'bundle_size', 
                    'priority': 'medium',
                    'message': f'Bundle size could be optimized ({size_mb}MB).'
                })
        
        # Dependency recommendations
        if 'dependency_analysis' in self.results:
            heavy_deps = self.results['dependency_analysis'].get('heavy_dependencies', [])
            if heavy_deps:
                recommendations.append({
                    'type': 'dependencies',
                    'priority': 'medium',
                    'message': f'Heavy dependencies detected: {", ".join([d["name"] for d in heavy_deps])}'
                })
        
        self.results['recommendations'] = recommendations
    
    def _generate_report(self):
        """Generate and display the analysis report"""
        print("\n" + "="*60)
        print("📊 BUNDLE ANALYSIS REPORT")
        print("="*60)
        
        # Build Analysis
        if 'build_analysis' in self.results:
            build = self.results['build_analysis']
            if build.get('has_build'):
                print(f"📦 Build Size: {build['total_size_mb']} MB")
            else:
                print("📦 No build output found - run `npm run build` first")
        
        # Dependencies
        if 'package_analysis' in self.results:
            pkg = self.results['package_analysis']
            print(f"📚 Dependencies: {pkg['total_dependencies']} production, {pkg['total_dev_dependencies']} development")
            
            if pkg['dependency_issues']:
                print("⚠️  Dependency Issues:")
                for issue in pkg['dependency_issues']:
                    print(f"   • {issue}")
        
        # Recommendations
        if 'recommendations' in self.results and self.results['recommendations']:
            print("\n🎯 RECOMMENDATIONS:")
            for rec in self.results['recommendations']:
                priority_icon = "🔴" if rec['priority'] == 'high' else "🟡" if rec['priority'] == 'medium' else "🟢"
                print(f"   {priority_icon} {rec['message']}")
        
        print("="*60 + "\n")
    
    def _calculate_directory_size(self, directory: Path) -> int:
        """Calculate total size of directory in bytes"""
        total_size = 0
        try:
            for file_path in directory.rglob('*'):
                if file_path.is_file():
                    total_size += file_path.stat().st_size
        except Exception:
            pass
        return total_size

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Analyze Next.js/React bundles for optimization opportunities"
    )
    parser.add_argument(
        'target',
        nargs='?',
        default='.',
        help='Target project directory (default: current directory)'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )
    
    args = parser.parse_args()
    
    analyzer = BundleAnalyzer(args.target, verbose=args.verbose)
    results = analyzer.run()

if __name__ == '__main__':
    main()
