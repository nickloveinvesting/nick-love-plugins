#!/usr/bin/env python3
"""
Recursive Problem Solver - Complexity Analyzer

Analyzes problem statements to recommend appropriate depth levels,
confidence thresholds, and workflow templates.

Usage:
    python analyze_complexity.py "Your problem statement here"
"""

import sys
import re
from typing import Dict, Tuple


def analyze_complexity(problem: str) -> Dict:
    """
    Analyze problem complexity based on various indicators.
    
    Returns dict with:
    - complexity_score (0-100)
    - recommended_depth (1-5)
    - confidence_threshold (0.75-0.95)
    - workflow_template (str)
    - estimated_tokens (int)
    - reasoning (list of str)
    """
    score = 0
    reasoning = []
    
    # Normalize text
    problem_lower = problem.lower()
    word_count = len(problem.split())
    
    # Indicator 1: Problem statement length (more detail = more complex)
    if word_count > 100:
        score += 15
        reasoning.append("Long problem description (>100 words) suggests complexity")
    elif word_count > 50:
        score += 10
        reasoning.append("Moderate problem description length")
    else:
        score += 5
        reasoning.append("Brief problem description")
    
    # Indicator 2: Critical/high-stakes keywords
    critical_keywords = [
        'production', 'critical', 'security', 'financial', 'safety',
        'compliance', 'regulation', 'audit', 'legal', 'mission-critical'
    ]
    critical_count = sum(1 for kw in critical_keywords if kw in problem_lower)
    if critical_count > 0:
        score += min(critical_count * 10, 20)
        reasoning.append(f"Contains {critical_count} critical/high-stakes indicator(s)")
    
    # Indicator 3: Complexity keywords
    complexity_keywords = [
        'complex', 'multiple', 'distributed', 'scale', 'architecture',
        'trade-off', 'optimize', 'balance', 'consider', 'evaluate'
    ]
    complexity_count = sum(1 for kw in complexity_keywords if kw in problem_lower)
    if complexity_count >= 3:
        score += 15
        reasoning.append(f"High complexity indicators ({complexity_count} keywords)")
    elif complexity_count >= 1:
        score += 10
        reasoning.append(f"Moderate complexity indicators ({complexity_count} keywords)")
    
    # Indicator 4: Multiple options/alternatives mentioned
    options_patterns = [
        r'option [abc123]', r'vs\.', r'versus', r'or', r'alternative',
        r'choose between', r'which', r'should [iw]e'
    ]
    options_found = sum(1 for pattern in options_patterns 
                       if re.search(pattern, problem_lower))
    if options_found >= 2:
        score += 15
        reasoning.append("Multiple options/alternatives to evaluate")
    
    # Indicator 5: Unknown/learning indicators
    learning_keywords = [
        'understand', 'learn', 'explain', 'what is', 'how does',
        'why', 'concept', 'theory', 'principle'
    ]
    learning_count = sum(1 for kw in learning_keywords if kw in problem_lower)
    if learning_count >= 2:
        score += 10
        reasoning.append("Learning/understanding focus detected")
    
    # Indicator 6: Validation/review keywords
    validation_keywords = [
        'review', 'validate', 'verify', 'check', 'correct',
        'bug', 'error', 'issue', 'problem with'
    ]
    validation_count = sum(1 for kw in validation_keywords if kw in problem_lower)
    if validation_count >= 2:
        score += 15
        reasoning.append("Validation/review focus detected")
    
    # Indicator 7: Implementation/design keywords
    design_keywords = [
        'design', 'build', 'create', 'implement', 'develop',
        'architecture', 'api', 'system', 'database', 'specification'
    ]
    design_count = sum(1 for kw in design_keywords if kw in problem_lower)
    if design_count >= 2:
        score += 15
        reasoning.append("Design/implementation focus detected")
    
    # Indicator 8: Constraint indicators (more constraints = more complex)
    constraint_keywords = [
        'must', 'cannot', 'requirement', 'constraint', 'within',
        'budget', 'timeline', 'limitation', 'requirement'
    ]
    constraint_count = sum(1 for kw in constraint_keywords if kw in problem_lower)
    if constraint_count >= 3:
        score += 15
        reasoning.append(f"Multiple constraints specified ({constraint_count})")
    elif constraint_count >= 1:
        score += 5
        reasoning.append(f"Some constraints specified ({constraint_count})")
    
    # Indicator 9: Uncertainty indicators
    uncertainty_keywords = [
        'not sure', 'uncertain', 'unclear', 'confused', 'help me decide',
        'what should', 'which is better', 'unsure'
    ]
    uncertainty_count = sum(1 for kw in uncertainty_keywords if kw in problem_lower)
    if uncertainty_count >= 1:
        score += 10
        reasoning.append("Uncertainty/indecision detected")
    
    # Indicator 10: Question marks (more questions = need more depth)
    question_count = problem.count('?')
    if question_count >= 3:
        score += 10
        reasoning.append(f"Multiple questions asked ({question_count})")
    
    # Cap score at 100
    score = min(score, 100)
    
    # Determine recommendations based on score
    recommendations = determine_recommendations(score, problem_lower)
    
    return {
        'complexity_score': score,
        'recommended_depth': recommendations['depth'],
        'confidence_threshold': recommendations['confidence'],
        'workflow_template': recommendations['workflow'],
        'estimated_tokens': recommendations['tokens'],
        'reasoning': reasoning,
        'complexity_level': recommendations['level']
    }


def determine_recommendations(score: int, problem_lower: str) -> Dict:
    """Determine recommended approach based on complexity score."""
    
    # Detect workflow type based on keywords
    workflow = "Deep Dive"  # Default
    
    if any(kw in problem_lower for kw in ['review', 'validate', 'check', 'verify', 'bug']):
        workflow = "Validation Loop"
    elif any(kw in problem_lower for kw in ['learn', 'understand', 'explain', 'what is']):
        workflow = "Learning Deep Dive"
    elif any(kw in problem_lower for kw in ['choose', 'decide', 'option', 'alternative', 'vs']):
        workflow = "Decision Framework"
    elif any(kw in problem_lower for kw in ['design', 'api', 'specification', 'architecture']):
        workflow = "Progressive Deepening"
    
    # Score-based recommendations
    if score >= 75:
        return {
            'level': 'Very High',
            'depth': 4,
            'confidence': 0.90,
            'workflow': workflow,
            'tokens': 30000
        }
    elif score >= 60:
        return {
            'level': 'High',
            'depth': 3,
            'confidence': 0.85,
            'workflow': workflow,
            'tokens': 25000
        }
    elif score >= 40:
        return {
            'level': 'Medium',
            'depth': 3,
            'confidence': 0.85,
            'workflow': workflow,
            'tokens': 20000
        }
    elif score >= 25:
        return {
            'level': 'Medium-Low',
            'depth': 2,
            'confidence': 0.80,
            'workflow': workflow,
            'tokens': 15000
        }
    else:
        return {
            'level': 'Low',
            'depth': 2,
            'confidence': 0.75,
            'workflow': workflow,
            'tokens': 10000
        }


def format_output(analysis: Dict) -> str:
    """Format analysis results for display."""
    output = []
    output.append("=" * 60)
    output.append("RECURSIVE PROBLEM SOLVER - COMPLEXITY ANALYSIS")
    output.append("=" * 60)
    output.append("")
    
    # Complexity assessment
    output.append(f"📊 Complexity Score: {analysis['complexity_score']}/100")
    output.append(f"📈 Complexity Level: {analysis['complexity_level']}")
    output.append("")
    
    # Recommendations
    output.append("🎯 RECOMMENDATIONS")
    output.append("-" * 60)
    output.append(f"Workflow Template:    {analysis['workflow_template']}")
    output.append(f"Recommended Depth:    {analysis['recommended_depth']} levels")
    output.append(f"Confidence Target:    {analysis['confidence_threshold']:.0%}")
    output.append(f"Estimated Tokens:     ~{analysis['estimated_tokens']:,}")
    output.append("")
    
    # Reasoning
    output.append("💡 REASONING")
    output.append("-" * 60)
    for i, reason in enumerate(analysis['reasoning'], 1):
        output.append(f"{i}. {reason}")
    output.append("")
    
    # Workflow guidance
    output.append("📋 WORKFLOW GUIDANCE")
    output.append("-" * 60)
    output.append(f"Template: {analysis['workflow_template']}")
    output.append("")
    
    if analysis['workflow_template'] == "Deep Dive":
        output.append("Process:")
        output.append("1. Depth 0: Initial exploration (sequential-thinking)")
        output.append("2. Depth 1: First critique (reflection)")
        output.append("3. Depth 2: Deep analysis (reflection)")
        output.append("4. Depth 3+: Validation (reflection)")
        output.append("5. Synthesize final recommendation")
    elif analysis['workflow_template'] == "Validation Loop":
        output.append("Process:")
        output.append("1. Depth 0: Propose solution (sequential-thinking)")
        output.append("2. Depth 1: First validation (reflection)")
        output.append("3. Depth 2: Refinement (sequential-thinking)")
        output.append("4. Depth 3: Second validation (reflection)")
        output.append("5. Approve or iterate")
    elif analysis['workflow_template'] == "Learning Deep Dive":
        output.append("Process:")
        output.append("1. Depth 0: Initial understanding")
        output.append("2. Depth 1: Gap identification (reflection)")
        output.append("3. Depth 2: Deep dive on gaps")
        output.append("4. Depth 3: Integration & validation")
    elif analysis['workflow_template'] == "Decision Framework":
        output.append("Process:")
        output.append("1. Depth 0: Options generation (sequential-thinking)")
        output.append("2. Depth 1-2: Deep evaluation (reflection per option)")
        output.append("3. Depth 3: Comparative analysis (reflection)")
        output.append("4. Depth 4: Risk assessment (reflection)")
        output.append("5. Final recommendation")
    elif analysis['workflow_template'] == "Progressive Deepening":
        output.append("Process:")
        output.append("1. Depth 0: Initial design (sequential-thinking)")
        output.append("2. Depth 1: Design critique (reflection)")
        output.append("3. Depth 2: Refined design with edge cases")
        output.append("4. Depth 3: Final validation (reflection)")
    
    output.append("")
    
    # Token budget warning
    output.append("⚠️  TOKEN BUDGET")
    output.append("-" * 60)
    output.append(f"Estimated usage: {analysis['estimated_tokens']:,} tokens")
    output.append(f"Total budget:    190,000 tokens")
    output.append(f"Remaining:       ~{190000 - analysis['estimated_tokens']:,} tokens")
    
    if analysis['estimated_tokens'] > 150000:
        output.append("")
        output.append("⚠️  WARNING: Estimated token usage exceeds 80% of budget!")
        output.append("   Consider breaking into multiple conversations.")
    
    output.append("")
    output.append("=" * 60)
    
    return "\n".join(output)


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python analyze_complexity.py \"Your problem statement here\"")
        print("\nExample:")
        print("  python analyze_complexity.py \"Should we migrate to microservices?\"")
        sys.exit(1)
    
    problem = " ".join(sys.argv[1:])
    
    print("\nAnalyzing problem complexity...\n")
    analysis = analyze_complexity(problem)
    print(format_output(analysis))


if __name__ == "__main__":
    main()
