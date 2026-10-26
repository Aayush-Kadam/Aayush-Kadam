<picture>
  <source media="(max-width: 600px)" srcset="assets/hero/observatory-mobile.svg">
  <img src="assets/hero/observatory.svg" width="1200" alt="Aayush Kadam — Code. Incentives. Evidence. Engineering, economics, entrepreneurship. A luminous computational instrument suspended in an orbital observatory.">
</picture>

# Aayush Kadam

**I build tools that make difficult claims easier to interrogate.**

Computer Science sophomore at **MIT ADT University, Pune**. Founder building developer tools and experimental software, with a research interest in incentives, AI systems, and how decisions survive contact with evidence. Long term, I'm interested in the meeting point of entrepreneurship and finance.

[Explore the engineering ↓](#selected-engineering) · [Enter the research atlas ↓](#research-atlas) · [Talk shop ↗](#connect)

## On the workbench

**Agent infrastructure** — recording what happened, reproducing supported executions, and making a changed observation inspectable.<br>
**Computational economics** — strategic delay, algorithmic bidders, and incentives created by persistent records.<br>
**Experimental products** — developer tools and research interfaces with visible assumptions and reproducible examples.

## Selected engineering

<a href="https://github.com/Aayush-Kadam/ghostframe"><img src="assets/projects/ghostframe.svg" width="1200" alt="01 — GhostFrame. Change one observation. Inspect what follows. A branching execution diagram."></a>

A local-first recorder and counterfactual debugger for **supported deterministic AI-agent workflows**. Python captures execution into SQLite; a React/TypeScript interface makes the evidence explorable.

**The interesting part:** replay a supported policy, replace one observation, and compare the new continuation with the preserved original.

`Python` `SQLite` `FastAPI` `React / TypeScript`<br>
**Pre-release.** Arbitrary SDK functions support playback only; general agent resumption and live-model replay are not implemented.

[Inspect the source ↗](https://github.com/Aayush-Kadam/ghostframe) · [Architecture](https://github.com/Aayush-Kadam/ghostframe/blob/main/docs/architecture.md) · [Synthetic demo](https://github.com/Aayush-Kadam/ghostframe#start-the-synthetic-demonstration)

<a href="https://github.com/Aayush-Kadam/economic-protocol-verifier"><img src="assets/projects/epv.svg" width="1200" alt="02 — Economic Protocol Verifier. Small domains. Explicit assurance. A finite grid with a certificate check."></a>

Bounded verification for selected economic protocols: finite semantics, exhaustive and SMT checks, replayable counterexamples, and checked proof certificates for specific compiled obligations.

**The interesting part:** assurance levels distinguish enumeration, solver results, and independent certificate checking instead of calling all three “proof.”

`Python` `Z3 / cvc5` `Alethe / Carcara`<br>
**Research preview.** Finite declared domains; economic-to-logic translation remains trusted. V3 requires the pinned external checker. Restrictive reuse terms apply.

[Inspect the source ↗](https://github.com/Aayush-Kadam/economic-protocol-verifier) · [Reviewer walkthrough](https://github.com/Aayush-Kadam/economic-protocol-verifier/blob/main/docs/REVIEWER_WALKTHROUGH.md) · [Trust boundaries](https://github.com/Aayush-Kadam/economic-protocol-verifier/blob/main/TRUST_AND_ASSURANCE.md)

<a href="https://github.com/Aayush-Kadam/incentive-fuzzer"><img src="assets/projects/incentive-fuzzer.svg" width="1200" alt="03 — Incentive Fuzzer. Give the rule an adversary. A search lens isolates a witness in a finite grid."></a>

Adversarial testing for bounded economic rules. Specify the rule, search feasible behavior, replay a witness exactly, and regression-test a proposed repair.

**The interesting part:** counterexamples and benchmark misses remain inspectable alongside successful checks.

`Python` `Exact evaluation` `Z3`<br>
**Research preview.** Component benchmarks are not real-world audit accuracy or behavioral forecasts. No software license has been selected; check reuse terms.

[Inspect the source ↗](https://github.com/Aayush-Kadam/incentive-fuzzer) · [Reviewer walkthrough](https://github.com/Aayush-Kadam/incentive-fuzzer/blob/master/docs/REVIEWER_WALKTHROUGH.md) · [Reuse terms](https://github.com/Aayush-Kadam/incentive-fuzzer/blob/master/LICENSE_DECISION.md)

## Research atlas

<img src="assets/graphics/research-atlas.svg" width="1200" alt="Research atlas connecting matching, memory, information, and mechanisms. Model, computation, reproduction, review.">

**01 / Matching — [WAITLAB](https://github.com/Aayush-Kadam/WaitLab)**<br>
When does waiting change the pool worth waiting for? Strategic delay, dynamic matching, and synthetic response recovery. [Paper-to-code map](https://github.com/Aayush-Kadam/WaitLab/blob/main/docs/PAPER_TO_CODE.md). **Released computational research software; synthetic evidence.**

**02 / Memory — [The Economics of Forgetting](https://github.com/Aayush-Kadam/economics-of-forgetting)**<br>
How do persistent records change the return to rehabilitation? A finite-horizon model with regional results. **Working paper; not peer reviewed.**

**03 / Information — [VERITAS](https://github.com/Aayush-Kadam/veritas-computational-lab)**<br>
What happens when persuasive evidence is cheap and verification is scarce? A computational lab for deception, congestion, and Bayesian demand. **Model-generated evidence; mixed recovery results.**

**04 / Mechanisms — [Delegation-Proof Market Design](https://github.com/Aayush-Kadam/delegation-proof-market-design)**<br>
How do auction rankings change when algorithms bid? Finite-horizon revenue–allocation tradeoffs, scoped certificates, and failed repairs. **Research artifacts; no successful delegation-proof mechanism claimed.**

These are computational studies and working materials. A public repository or archive DOI does not establish peer review or external replication. [More experiments ↗](https://github.com/Aayush-Kadam?tab=repositories)

## Tools behind the work

| Practice | Tools I use |
| :--- | :--- |
| Languages & interfaces | Python · TypeScript · JavaScript · React |
| Systems | FastAPI · SQLite · Git |
| Verification & reliability | Z3 · cvc5 · Pytest · Hypothesis · Ruff · mypy · GitHub Actions |
| Computational research | NumPy · Pandas · finite models · seeded simulation |

## Live signals

[![Profile view counter: provider-counted image requests](https://komarev.com/ghpvc/?username=Aayush-Kadam&label=Profile+image+requests&color=157784&style=flat-square)](https://github.com/antonkomarev/github-profile-views-counter)
[![GhostFrame repository stars](https://img.shields.io/github/stars/Aayush-Kadam/ghostframe?label=GhostFrame%20stars&style=flat-square&color=b18b48)](https://github.com/Aayush-Kadam/ghostframe/stargazers)
[![GhostFrame main verification status](https://github.com/Aayush-Kadam/ghostframe/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Aayush-Kadam/ghostframe/actions/workflows/ci.yml?query=branch%3Amain)

The view counter records provider-served image requests, including previews and repeat loads. GitHub caching affects updates; this is **not unique visitors or lifetime profile traffic**. Stars and CI are cached live service images. If a badge is unavailable, its source link remains usable. [How these signals work](docs/MAINTENANCE.md#live-signals).

## A working principle

I'd rather find the counterexample myself.

The fun starts when a clean idea meets a stubborn result: an agent that cannot replay, an auction rule that invites a better strategy, or a model that loses to its baseline. I want the failure small enough to reproduce, and the next version better for having found it.

## Connect

Building agent infrastructure, checking a mechanism, or arguing with a model? Let's compare notes.

**[GitHub ↗](https://github.com/Aayush-Kadam) · [LinkedIn ↗](https://www.linkedin.com/in/aayush-kadam-18545a217)**

<sub>Original Observatory artwork · [Sources & maintenance](docs/MAINTENANCE.md) · Built to be inspected.</sub>
