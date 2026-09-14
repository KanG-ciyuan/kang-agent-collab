# Validation and evidence boundaries

This document separates what is visible in the repository from Pilot outcomes supplied by the maintainer.

## Evidence classes

| Class | Meaning |
|---|---|
| Repository-verified | Can be checked from the current tracked files or Git history |
| Maintainer-reported Pilot evidence | Observed in a real Pilot under stated conditions, but the underlying private artifacts are not published here |
| Unknown / to verify | Not supported strongly enough for a public capability claim |

## Repository-verified in v0.2.0

- A single canonical Skill entrypoint defines activation, exclusions, workflow, recovery, stop conditions, and required output.
- Shared contracts define Project Identity, Lite and Full Manifests, drift levels, result state, write-back, Handoff, and Takeover Check.
- Capability Profiles record dated, conditional runtime observations and explicitly separate capability from permission.
- Git history shows the protocol version progression from `0.1.0` to `0.2.0` without introducing a service or runtime.

## Maintainer-reported Pilot evidence

The maintainer reports real engineering Pilot evidence for:

- recovery from a fresh session without relying on full prior chat history;
- project identity recovery;
- authority → canonical repository → live Git recovery;
- takeover from a clean working tree;
- recovery behavior when authority was stale or the working tree was dirty;
- safe STOP behavior when identity, permission, evidence, or change ownership did not justify continuation;
- initial evidence across more than one runtime under specific configurations.

The Pilot's private project paths, conversation data, and internal materials are intentionally not included in this public repository. No benchmark score or universal success rate is inferred from these observations.

## Claim boundary

The evidence does **not** prove:

- compatibility with every agent, model, runtime, harness, or project type;
- autonomous access to a user's repository or shared memory;
- correct behavior when a runtime ignores the contract;
- permission to write, commit, push, deploy, spend money, or call external services;
- Level 4 proof;
- production readiness in every environment.

The strongest supported statement is: the protocol has real Pilot evidence and dated multi-runtime observations under tested conditions. New runtime claims should follow [CONTRIBUTING.md](../CONTRIBUTING.md) and include reproducible, privacy-safe evidence.

## Suggested future evidence

These are evidence improvements, not new product features:

- publish anonymized recovery fixtures;
- record exact runtime and tool conditions;
- test the same handoff against clean, explainable-drift, and D3 cases;
- add an isolated installation check for each claimed Skill loader;
- publish redacted expected-versus-observed takeover results.
