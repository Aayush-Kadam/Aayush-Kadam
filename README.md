# Aayush Kadam

### Making complex decisions testable, explainable, and verifiable.

Computer Science Sophomore at **MIT ADT University**. I build research software and developer tools around a practical question: **what evidence would make a difficult result worth trusting?**

Start with **[GhostFrame](https://github.com/Aayush-Kadam/ghostframe)**: a local recorder and branching debugger for supported deterministic agent workflows.

## Selected engineering

### [GhostFrame](https://github.com/Aayush-Kadam/ghostframe) · Observe and reproduce

Python SDK, SQLite evidence store, and React/TypeScript debugger. Record a synthetic document-agent incident, replay its supported policy, replace one observation, and execute a new continuation.

- **Engineering focus:** privacy-aware capture, evidence consistency, bounded execution, and loopback API controls.
- **Inspect:** [architecture](https://github.com/Aayush-Kadam/ghostframe/blob/main/docs/architecture.md) · [CI](https://github.com/Aayush-Kadam/ghostframe/actions) · [run the demo](https://github.com/Aayush-Kadam/ghostframe#start-the-synthetic-demonstration).
- **Boundary:** arbitrary SDK functions support playback only; live-model replay and general agent resumption are not implemented. The published pre-release predates the cross-platform CI repair; use current main for that fix.

### [Economic Protocol Verifier](https://github.com/Aayush-Kadam/economic-protocol-verifier) · Specify and verify

Python framework for finite economic mechanisms: exhaustive checking, SMT cross-checks with cvc5/Z3, replayable counterexamples, and hash-bound Alethe proof bundles checked with Carcara.

- **Engineering focus:** explicit trust boundaries, counterexample replay, and assurance levels that distinguish enumeration, solvers, and proof checking.
- **Inspect:** [trust and assurance](https://github.com/Aayush-Kadam/economic-protocol-verifier/blob/main/TRUST_AND_ASSURANCE.md) · [first result](https://github.com/Aayush-Kadam/economic-protocol-verifier#first-result) · [limitations](https://github.com/Aayush-Kadam/economic-protocol-verifier/blob/main/LIMITATIONS.md).
- **Boundary:** finite declared domains; the economic-to-logic translation remains trusted. V3 requires the pinned external checker. Public source is a research preview with restrictive license terms.

### [Incentive Fuzzer](https://github.com/Aayush-Kadam/incentive-fuzzer) · Search and stress-test

Python research prototype for bounded economic rules. A typed specification feeds exact evaluation, adversarial search, witness replay, restricted Z3 checks, finite games, and repair regression.

- **Engineering focus:** falsifiable findings and explicit failure statuses, including a preserved benchmark miss.
- **Inspect:** [quickstart](https://github.com/Aayush-Kadam/incentive-fuzzer#quickstart) · [reproduction](https://github.com/Aayush-Kadam/incentive-fuzzer#reproducibility) · [research report](https://github.com/Aayush-Kadam/incentive-fuzzer/blob/master/paper/INCENTIVE_FUZZER_RESEARCH_PREVIEW.md).
- **Boundary:** curated component-level benchmarks are not real-world audit accuracy or behavioral forecasts. Independent domain review is pending; see the repository's license decision before reuse.

## Computational research

- **[WAITLAB](https://github.com/Aayush-Kadam/WaitLab)** — strategic delay, dynamic matching, response operators, and synthetic identification. [Paper-to-code map](https://github.com/Aayush-Kadam/WaitLab/blob/main/docs/PAPER_TO_CODE.md).
- **[Delegation-Proof Market Design](https://github.com/Aayush-Kadam/delegation-proof-market-design)** — finite-horizon adaptive bidding experiments, revenue–allocation tradeoffs, and failed mechanism repairs preserved as results.
- **[VERITAS](https://github.com/Aayush-Kadam/veritas-computational-lab)** — verification congestion, deceptive entry, and Bayesian demand discipline. Model-generated results, not field evidence.

These repositories contain working papers, technical reports, and experimental artifacts. Repository publication or an archive DOI does not establish peer review or independent replication.

## How the work connects

```text
Specify → Simulate → Stress-test → Verify → Observe → Reproduce
```

This is a shared research workflow, not an integrated software platform. EPV and Incentive Fuzzer investigate bounded institutional rules; GhostFrame studies execution evidence. WAITLAB and the computational papers make model assumptions and numerical results inspectable.

## Technical practice

**Reliability:** Python, regression and property-based testing, CLI/API design, SQLite evidence, cross-platform CI.  
**Verification:** finite semantics, exact arithmetic, SMT-backed checks, counterexamples, certificate trust boundaries.  
**Research computing:** controlled simulations, explicit seeds and domains, baseline comparisons, reproducible artifacts.  
**Interfaces:** React/TypeScript debugging tools and computational exhibits.

I prefer a small reproducible counterexample to a broad unsupported claim. Tests establish behavior within their coverage; synthetic experiments establish results within their models. Limitations and negative results belong beside the result.

For technical discussion, use the relevant repository's issue tracker. Browse [all public repositories](https://github.com/Aayush-Kadam?tab=repositories).
