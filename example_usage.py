"""
Demonstration of Shapley Value Cooperative Game Allocator Skill
"""

from client import ShapleyValueAllocator
from typing import FrozenSet

def main():
    print("=== Cooperative Game Theory Shapley Value Fair Allocation ===")
    players = ["Agent_A", "Agent_B", "Agent_C"]

    # Coalition game:
    # Standalone values: A=20, B=30, C=50
    # Grand coalition {A, B, C} creates synergistic bonus of 30 (total = 130)
    base_values = {"Agent_A": 20.0, "Agent_B": 30.0, "Agent_C": 50.0}

    def characteristic_fn(coalition: FrozenSet[str]) -> float:
        val = sum(base_values[p] for p in coalition)
        if len(coalition) == 3:
            val += 30.0  # Cooperative synergy surplus
        return val

    allocator = ShapleyValueAllocator(players, characteristic_fn)
    shapley_shares = allocator.compute_shapley_values()

    print("Computed Fair Shapley Value Allocations:")
    for p, share in shapley_shares.items():
        print(f"  {p}: ${share:.2f}")

    total_allocated = sum(shapley_shares.values())
    grand_coalition_val = characteristic_fn(frozenset(players))
    print(f"\nEfficiency Check: Sum of Shares = ${total_allocated:.2f} == Grand Coalition = ${grand_coalition_val:.2f}")

    assert abs(total_allocated - 130.0) < 1e-6
    # Symmetric 30-unit bonus split equally: +10 each
    assert abs(shapley_shares["Agent_A"] - 30.0) < 1e-6
    assert abs(shapley_shares["Agent_B"] - 40.0) < 1e-6
    assert abs(shapley_shares["Agent_C"] - 60.0) < 1e-6

    print("\nShapley Value Fair Allocation Verification PASS!")

if __name__ == "__main__":
    main()
