# GenPark Shapley Value Cooperative Game Allocator Skill

Cooperative game theory Shapley value engine computing fair payoff allocations.

Read more at [GenPark](https://genpark.ai) and the [GenPark MCP Catalog](https://genpark.ai/mcp).

```mermaid
graph TD
    A[Agent Subsets S] --> M[Marginal Contribution v S+i - v S]
    M --> W[Combinatorial Weighting |S|! |N|-|S|-1! / |N|!]
    W --> S[Shapley Fair Payoff phi_i]
    S --> E[Satisfies Efficiency, Symmetry, Dummy Player & Additivity]
    style A fill:#e1f5fe
    style M fill:#fff9c4
    style W fill:#ffcdd2
    style S fill:#c8e6c9
    style E fill:#d1c4e9
```

## Features
- Exact Shapley value calculation across all coalition permutations.
- Guaranteed satisfaction of axiomatic fairness criteria.
- Pure Python standard library.
