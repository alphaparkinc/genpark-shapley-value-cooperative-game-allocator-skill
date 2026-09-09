"""
MCP Server for Shapley Value Cooperative Game Allocator Skill
"""

import json
import sys
from client import ShapleyValueAllocator

def handle_call(name: str, args: dict) -> dict:
    if name == "calculate_shapley_allocation":
        players = args.get("players", ["A", "B", "C"])
        standalone = args.get("standalone_values", {"A": 10.0, "B": 20.0, "C": 30.0})
        bonus = args.get("grand_coalition_bonus", 15.0)
        def v(c):
            val = sum(standalone.get(p, 0.0) for p in c)
            if len(c) == len(players):
                val += bonus
            return val
        allocator = ShapleyValueAllocator(players, v)
        shares = allocator.compute_shapley_values()
        return {"shapley_values": shares}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_call(req.get("method"), req.get("params", {}))
        sys.stdout.write(json.dumps(res) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
