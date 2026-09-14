# Runtime integration

The canonical protocol is runtime-neutral. Installation and activation are not.

## Generic integration

A runtime can use `kang-agent-collab` when it can:

1. read [SKILL.md](../SKILL.md) and referenced contract files;
2. access the project authority or receive its location;
3. access the canonical repository for engineering work;
4. inspect live Git state when Git evidence is required;
5. receive explicit task permission;
6. produce the required result state and, when triggered, a Handoff.

If one of these capabilities is absent, the agent should degrade transparently or stop. It must not infer missing access from the model name.

## Installation patterns

Use the pattern supported by your runtime:

- **Repository reference:** clone the repository and explicitly ask the agent to read its root `SKILL.md`.
- **Skill directory:** copy or link the complete repository into the runtime's documented Skill directory.
- **Instruction attachment:** attach `SKILL.md` plus the referenced contract needed for the task.

These are patterns, not universal commands. Directory names, discovery rules, recursion, and tool permissions vary by runtime.

## Runtime-specific notes

The dated observations in [capability-profiles.md](../references/capability-profiles.md) are the canonical source. They cover identified local runtime configurations, not every installation of those products.

- **Codex:** local Skill and Git capabilities were observed, while filesystem and optional tools remain session-specific.
- **Claude Code:** local Skill loading and repository access were observed for the recorded version; external paths and optional integrations remain conditional.
- **Hermes:** indexed on-demand Skill loading was observed; active tools and external directories depend on configuration.
- **OpenClaw:** documented workspace, managed, and shared Skill roots were observed; enabled tools remain agent-specific.
- **ChatGPT Work:** exchanging the text contract is possible, but local Skill loading and tools depend on the session.
- **DeepSeek Harness:** no general operational profile is claimed. Verify the concrete harness before use.

## Integration checklist

- [ ] The runtime can find the single canonical `SKILL.md`.
- [ ] Referenced files remain available at their relative paths.
- [ ] Project authority access is explicit.
- [ ] Repository and Git access are verified when required.
- [ ] Write, commit, push, deployment, cost, and external-service permissions are explicit.
- [ ] A takeover test includes a fresh receiving session and independently rechecked Git state.
- [ ] Results record conditions and missing evidence.

## Troubleshooting

| Symptom | Likely cause | Safe response |
|---|---|---|
| The agent cannot locate the contract | The runtime does not discover this Skill layout | Point it directly to the root `SKILL.md` or use the runtime's documented Skill directory |
| The project identity is ambiguous | Authority and repository identity are missing or conflict | Stop and request the authoritative entry or maintainer decision |
| The Handoff says clean but Git is dirty | State changed after the Handoff | Reclassify drift and identify ownership; do not stash or reset unknown work |
| Git is available but push is not authorized | Capability was mistaken for permission | Keep changes local and request explicit publication permission |
| Shared memory is inaccessible | External path or integration is not available | Request the smallest required authority excerpt or path grant; do not guess |
