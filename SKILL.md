---
name: kang-agent-collab
description: Use when work must continue across agents through shared project identity, scoped task state, Git evidence, write-back candidates, handoff, or takeover. Also use when resuming an interrupted engineering task without relying on full chat history. Do not use for agent selection, delegation, orchestration, routing, automatic Vault writes, or worktree management.
metadata:
  author: Kang
  version: "0.2.0"
---

# Kang Agent Collaboration

Carry project state safely between different agents through a platform-neutral contract. Preserve the distinction between Agent capability, current-task permission, semantic project memory, and engineering truth.

## Activation

Use this Skill when a task requires one or more of:

- resuming a project from shared memory and Git;
- verifying project identity or current engineering state;
- preparing or consuming a cross-agent handoff;
- recording a bounded write-back candidate;
- recovering an interrupted task without full chat history.

Do not use it to choose agents, delegate roles, schedule work, create infrastructure, or grant permissions. If team composition or specialist delegation is the job, route to `kang-agent-workforce`; that Skill may reference this contract for state transfer.

## Core workflow

1. **START** — identify the requested outcome, current agent, risk, and whether Lite or Full Manifest is required.
2. **READ** — locate the authoritative project entry and current handoff; load only the smallest necessary decisions or reusable knowledge.
3. **VERIFY STATE** — confirm Project Identity and, for engineering work, independently inspect repository root, branch, HEAD, upstream, staged, unstaged, and untracked state.
4. **WORK** — act only inside the Manifest scope and current permissions. Capability never implies permission.
5. **VERIFY RESULT** — record `done`, `partial`, `blocked`, or `failed` with evidence against acceptance criteria.
6. **COMMIT** — follow the Manifest commit policy. Never force a commit, overwrite unrelated work, or guess change ownership.
7. **DISTILL** — retain only durable project state, decisions, results, failures, lessons, reusable knowledge, and unresolved facts.
8. **WRITE-BACK CANDIDATE** — propose a bounded update; do not write to shared memory unless the task grants that authority.
9. **HANDOFF** — produce the minimum state another agent needs when an event-driven handoff is required.
10. **TAKEOVER** — consume the handoff, recheck identity and engineering state, classify drift, and continue only when safe.

## Recovery from a project ID

When a compatible Agent is started with a known `project_id`, recover through existing entries in this order:

```text
project_id
-> Agent Knowledge Routing Index
-> project Obsidian Authority
-> canonical_repo and current recovery state
-> repository PROJECT_IDENTITY
-> live Git state
-> current Manifest or task permissions, when present
-> safe_to_continue decision
```

Treat the routing index as discovery, the Authority as shared project memory, `PROJECT_IDENTITY` as repository identity, and live Git as current engineering truth. Prefer references between these entries; do not copy whole project descriptions, Manifests, or Handoffs into each other.

If the Runtime cannot access the routing index, Authority, or repository, stop and request the minimum missing entry. Never guess a path, select a semantically similar project, or infer the canonical repository from a historical folder name. If Authority, `PROJECT_IDENTITY`, Git, and the Manifest conflict on project identity, set identity to `to_verify` and stop for Kang's decision.

This recovery contract makes Level 3 testing possible; it does not prove that autonomous Level 3 recovery has succeeded in any Runtime.

## Stop conditions

Stop and escalate when:

- Project Identity is ambiguous or conflicts with the authoritative project entry;
- task scope, acceptance, required permission, or allowed write paths are missing for risky work;
- dirty changes cannot be reliably attributed, producing D3;
- required evidence cannot be produced;
- the requested action would exceed the Manifest or alter another agent's work;
- secrets or credential values would need to enter a contract, handoff, shared memory, or Git.

Do not stash, reset, clean, discard, move, or commit unknown changes to satisfy this workflow.

## Reference routing

- Read [contracts.md](references/contracts.md) when creating or consuming a Manifest, Project Identity record, Drift classification, Result State, Write-back Candidate, Handoff, or Takeover Check.
- Read [capability-profiles.md](references/capability-profiles.md) only when deciding how the current runtime can load the Skill or access tools and context.
- Treat a Capability Profile as descriptive evidence, never as task authorization.

## Required output

Return the current result state, supporting evidence, unresolved drift or decisions, and the next safe action. Produce a Handoff or Write-back Candidate only when its trigger is present.
