# Changelog

All notable changes to `kang-agent-collab` are documented here. Dates use `YYYY-MM-DD`.

## Unreleased

- No changes yet.

## 0.2.0 — 2026-09-14

### Added

- Recovery from a known `project_id` through project authority, canonical repository identity, live Git state, and current task permission.
- Explicit safe-stop behavior when required recovery entries are inaccessible or identity sources conflict.
- A minimum engineering handoff schema and takeover context declaration.
- English, Simplified Chinese, Japanese, Korean, and Spanish public README files.
- Generic Quick Start, architecture, runtime integration, validation boundaries, and copyable examples.
- Contribution, security, conduct, GitHub template, and repository hygiene files.

### Notes

- The open-source packaging does not change the canonical Skill contract.
- The protocol version remains `0.2.0`.

## 0.1.0 — 2026-09-12

### Added

- Initial platform-neutral collaboration Skill.
- Shared contracts for Manifest, Project Identity, drift, Result State, Write-back Candidate, Handoff, and Takeover Check.
- Dated capability profiles for several runtimes with explicit unknown and conditional states.
