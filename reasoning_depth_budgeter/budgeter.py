"""Core Reasoning Depth Budgeter implementation."""
import re
from enum import Enum
from typing import Dict, List, Tuple

class BudgetTier(Enum):
    XS = (256, "Trivial / Lookup")
    SM = (1024, "Simple Transformation")
    MD = (3072, "Moderate Logic / Multi-step")
    LG = (8192, "Complex Architecture / Math")
    XL = (16384, "Exhaustive Theorem / Deep Debug")

    def __init__(self, tokens: int, description: str):
        self.tokens = tokens
        self.description = description

class ComplexityAssessment:
    def __init__(self, tier: BudgetTier, allocated_tokens: int, score: float, indicators: List[str]):
        self.tier = tier
        self.allocated_tokens = allocated_tokens
        self.score = score
        self.indicators = indicators

    def __repr__(self) -> str:
        return f"<ComplexityAssessment tier={self.tier.name} tokens={self.allocated_tokens} score={self.score:.2f}>"

class ReasoningDepthBudgeter:
    """Estimates cognitive difficulty of input tasks and dynamically provisions reasoning token caps."""
    
    COMPLEXITY_PATTERNS = {
        "mathematical_notation": (r"[∑∫∂√π≠≤≥^]|\b(integral|derivative|matrix|eigen)\b", 2.5),
        "formal_logic": (r"\b(contrapositive|isomorphism|np-complete|bijection|invariant)\b", 2.0),
        "code_architecture": (r"\b(refactor|deadlock|race condition|concurrency|distributed)\b", 1.8),
        "multi_constraint": (r"\b(given that|subject to|optimizing|satisfying|at the same time)\b", 1.2),
        "code_snippet": (r"```[a-z]*\n[\s\S]*?```", 1.5)
    }

    def assess_complexity(self, prompt: str) -> ComplexityAssessment:
        score = 0.5  # Base score
        indicators = []

        for name, (pat, weight) in self.COMPLEXITY_PATTERNS.items():
            matches = re.findall(pat, prompt, re.IGNORECASE)
            if matches:
                count = len(matches)
                score += weight * min(3, count)
                indicators.append(f"{name} ({count} match(es))")

        # Word count contribution
        word_count = len(prompt.split())
        score += min(3.0, word_count / 100.0)

        # Map score to Tier
        if score < 1.5:
            tier = BudgetTier.XS
        elif score < 3.5:
            tier = BudgetTier.SM
        elif score < 6.0:
            tier = BudgetTier.MD
        elif score < 9.5:
            tier = BudgetTier.LG
        else:
            tier = BudgetTier.XL

        return ComplexityAssessment(
            tier=tier,
            allocated_tokens=tier.tokens,
            score=round(score, 2),
            indicators=indicators
        )
