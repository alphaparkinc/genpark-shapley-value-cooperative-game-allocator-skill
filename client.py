"""
Shapley Value Cooperative Game Allocator Skill Client
Pure Python Standard Library implementation of Shapley value calculation in cooperative games.
Computes the uniquely fair surplus/cost allocation satisfying Efficiency, Symmetry,
Dummy Player, and Additivity axioms across all player coalitions.
"""

import itertools
import math
from typing import List, Dict, Callable, Any, FrozenSet


class ShapleyValueAllocator:
    def __init__(self, players: List[str], characteristic_fn: Callable[[FrozenSet[str]], float]):
        self.players = list(players)
        self.v = characteristic_fn
        self.n = len(players)

    def compute_shapley_values(self) -> Dict[str, float]:
        """Compute exact Shapley value for every player across all 2^n coalitions."""
        shapley: Dict[str, float] = {p: 0.0 for p in self.players}
        n = self.n

        for p in self.players:
            other_players = [o for o in self.players if o != p]
            phi_p = 0.0
            for k in range(len(other_players) + 1):
                # Weight: |S|! * (|N| - |S| - 1)! / |N|!
                weight = (math.factorial(k) * math.factorial(n - k - 1)) / math.factorial(n)
                for subset in itertools.combinations(other_players, k):
                    s = frozenset(subset)
                    s_with_p = s | frozenset([p])
                    marginal_contrib = self.v(s_with_p) - self.v(s)
                    phi_p += weight * marginal_contrib
            shapley[p] = phi_p
        return shapley
