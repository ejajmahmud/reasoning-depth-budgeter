"""CLI for reasoning-depth-budgeter."""
import sys
import argparse
from .budgeter import ReasoningDepthBudgeter

def main():
    parser = argparse.ArgumentParser(description="Reasoning Depth Budgeter CLI")
    parser.add_argument("--demo", action="store_true", help="Evaluate budget allocation on diverse prompts")
    args = parser.parse_args()

    if args.demo:
        budgeter = ReasoningDepthBudgeter()
        p1 = "What is the capital of France?"
        p2 = "Prove that every planar graph has a vertex of degree at most 5 using Euler's formula."
        
        a1 = budgeter.assess_complexity(p1)
        a2 = budgeter.assess_complexity(p2)
        print(f"Prompt 1: '{p1}' -> {a1}")
        print(f"Prompt 2: '{p2[:40]}...' -> {a2}")
    else:
        parser.print_help()
    sys.exit(0)

if __name__ == "__main__":
    main()
