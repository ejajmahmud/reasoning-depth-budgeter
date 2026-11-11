"""Unit tests for reasoning-depth-budgeter."""
import unittest
from reasoning_depth_budgeter.budgeter import ReasoningDepthBudgeter, BudgetTier

class TestReasoningDepthBudgeter(unittest.TestCase):
    def setUp(self):
        self.budgeter = ReasoningDepthBudgeter()

    def test_simple_prompt_xs(self):
        a = self.budgeter.assess_complexity("Hello world")
        self.assertEqual(a.tier, BudgetTier.XS)
        self.assertEqual(a.allocated_tokens, 256)

    def test_hard_math_tier(self):
        prompt = "Compute the integral of x * exp(x) subject to boundary conditions and solve for eigenvalues of the matrix."
        a = self.budgeter.assess_complexity(prompt)
        self.assertIn(a.tier, (BudgetTier.LG, BudgetTier.XL, BudgetTier.MD))
        self.assertGreaterEqual(a.allocated_tokens, 3072)
