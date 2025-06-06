## Appendix A | Agent‑Based Resilience Model (v0.9)

**Model platform:** NetLogo 6.3.0   •   **Code repo:** https://github.com/rjbotelho/jus‑soli‑resilience

### Purpose
Simulate how removing a single constitutional safeguard (birth‑right citizenship) propagates through a multi‑layer democratic network (voting‑rights, equal‑protection, rule‑making) and measure survivability (percentage of agents retaining full civic status) over legislative cycles.

### Key Entities
| Entity | Attributes | Notes |
|--------|------------|-------|
| Citizen agents | status ∈ {full, partial, stateless}; trust ∈ [0‑1] | 20 000 agents seeded with baseline trust = 0.70 |
| Institution nodes | redundancy‑weight; jurisdiction | Nodes: Congress, Courts, States, Agencies, Presidency |
| Shock event | magnitude, frequency | External economic shock every 10 ticks |

### Scenario Parameters
| Parameter | Baseline | Project 2025 |
|-----------|----------|--------------|
| Citizenship redundancy (Rc) | 3 | 1 (executive only) |
| Loop latency (L) | 2 ticks | 5 ticks (agency purge) |
| Trust‑decay rate (δ) | 0.01 | 0.04 |

### Results
| Metric | Healthy Republic | Project 2025 |
|--------|------------------|--------------|
| Survivability after 3 cycles | 92 % | 57 % (-38 %) |
| Avg. trust score | 0.66 | 0.41 |
| Time to first cascade failure | >50 ticks | 17 ticks |

### Interpretation
Lower redundancy and longer feedback latency create a tipping‑point where an external shock pushes the system past a critical threshold, triggering cascade failure of rights (statelessness agents spike). This empirically supports the article’s claim that revoking *jus soli* moves the republic from antifragile to brittle.
