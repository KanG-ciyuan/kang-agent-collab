# Contributing to kang-agent-collab

Thank you for helping keep this protocol small, portable, and evidence-bound.

## Good contributions

- clarify a contract without changing its meaning;
- add a generic, secret-free example;
- improve a translation while preserving the canonical English facts;
- report a runtime observation with its exact conditions and date;
- add a privacy-safe takeover fixture;
- fix broken links, terminology drift, or ambiguous stop conditions.

Features that introduce orchestration, scheduling, databases, dashboards, registries, message buses, hosted memory, automatic write-back, or agent selection are outside this repository's purpose.

## Canonical sources

- `SKILL.md` is the only discoverable Skill entrypoint.
- `references/contracts.md` is the canonical contract definition.
- `references/capability-profiles.md` is the canonical runtime observation record.
- Translated README files explain the project; they are not independent protocol authorities.

Do not add translated copies such as `SKILL.zh-CN.md`. Avoid duplicating a contract into multiple files.

## Before opening a pull request

1. Create a focused branch.
2. Keep examples generic, anonymous, path-free, and secret-free.
3. Check all local Markdown links.
4. Confirm every README still reports version `0.2.0` unless a protocol release has been explicitly approved.
5. Search tracked files and Git history for credentials, personal paths, private URLs, logs, and conversation data.
6. Explain whether the change affects only documentation or changes the canonical Skill contract.

Documentation packaging alone does not require a protocol version bump.

## Runtime evidence

A runtime claim must include:

- runtime or harness name and exact version when known;
- observation date;
- Skill activation mechanism;
- repository, shared-memory, shell, Git, browser, and computer-use access as `available`, `conditional`, `unavailable`, or `unknown`;
- configuration and permission conditions;
- what was actually executed or observed;
- missing evidence and known limitations.

Do not infer runtime capability from the underlying model brand. Do not turn one passing case into universal compatibility.

## Contract changes

Changes to `SKILL.md` or canonical contracts should include:

- the failure mode or repeated need being addressed;
- why the change belongs in the shared protocol rather than an adapter or example;
- compatibility impact;
- at least one positive and one stop/boundary case;
- an explicit versioning decision.

## Pull request checklist

- [ ] The change stays within a lightweight Skill/protocol boundary.
- [ ] Capability and permission remain separate.
- [ ] Git remains the source of live engineering truth.
- [ ] Unknown change ownership still produces STOP.
- [ ] Claims match the evidence provided.
- [ ] No credentials, private paths, personal data, logs, or conversation dumps are included.
- [ ] Language files remain factually consistent when public facts changed.
- [ ] The canonical Skill version is unchanged for documentation-only work.

By contributing, you agree to follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) and the security guidance in [SECURITY.md](SECURITY.md).
