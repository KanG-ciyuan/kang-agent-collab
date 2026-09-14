# Shared Contracts

These contracts carry task state between agents. Omit optional fields that add no decision value; never replace unknown facts with guesses.

Existing evidence or result artifacts MUST NOT be overwritten unless the Manifest explicitly authorizes replacement.

## Sources of truth and reference rule

Each entry owns one kind of truth. Prefer a pointer to the owning entry over copying its content.

| Entry | Owns | Must not become |
|---|---|---|
| `AGENTS` | Stable execution, safety, Git, and project-boundary rules | Current task state or Handoff |
| `PROJECT_IDENTITY` | `project_id`, canonical repository, Authority pointer, and relationships to other projects | Task history or changing test status |
| `README` | Human-facing purpose, stable usage, and stable capabilities | Manifest or current Handoff |
| Manifest | Current scope, exclusions, acceptance, write paths, baseline, commit policy, and stop conditions | A copy of Project Identity or project history |
| Handoff | Previous result, current engineering state, evidence, breakpoint, next action, blockers, and do-not-do guidance | A copy of the Manifest or chat transcript |
| Obsidian Authority | Stable project truth, current phase, decisions, repository pointer, recovery state, and evidence status | Source-level detail or full logs |
| Git | Live HEAD, working tree, ancestry, and tracked engineering content | Project purpose or decision rationale |

Authority and Handoff guide recovery but never override live Git engineering facts. Verify Git at takeover. Capability Profiles describe a Runtime; they do not replace Manifest permissions. A shared worktree has one writer at a time, and unknown change ownership still requires STOP.

## Lite Manifest

Use only for low-risk, single-agent work with clear boundaries that does not modify code or use Git.

```yaml
objective:
scope:
acceptance:
agent:
```

## Full Manifest

Use for code changes, Git operations, cross-agent takeover, high-risk or multi-module work, permissions, cost, deployment, state drift, or restricted write paths.

```yaml
task_ref:
objective:
scope:
out_of_scope:
acceptance:
agent:
risk:
allowed_write_paths:
state_baseline:
git_commit: allowed | recommended | required | forbidden
vault_writeback: candidate_only
permissions_and_cost:
handoff_trigger:
```

The Manifest defines what the agent is permitted to do in this task. It does not inherit permission from a Capability Profile.

## Project Identity

```yaml
project_id:
authoritative_entry:
repository_or_workspace:
relationship_to_other_projects:
status: verified | historical | to_verify
confirmed_by:
last_verified:
```

Do not infer identity from repository, directory, worktree, note name, semantic similarity, or historical context alone. If continuing an old project, creating a new project that reuses old work, sharing code, planning a future merge, and using a historical project as reference cannot be distinguished from evidence, set `status: to_verify` and stop changes to authoritative ownership.

## Project ID recovery

For a known `project_id`, use the existing recovery chain:

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

The routing index discovers an Authority; it is not another project-state store. The Authority should point to the canonical repository and current recovery state, while repository `PROJECT_IDENTITY` should point back to the Authority. Do not add a new Project Entry merely to duplicate these links.

If an entry is inaccessible, request the minimum missing entry, such as the Authority or canonical repository path. This is a safe recovery failure, not permission to guess. Any identity conflict among the Authority, `PROJECT_IDENTITY`, Git, and Manifest makes Project Identity `to_verify` and requires STOP.

## State Drift

| Level | Meaning | Required action |
|---|---|---|
| D0 | Handoff and observed state agree; working tree is clean | Continue within the Manifest |
| D1 | Explainable, non-overlapping difference with known ownership | Record evidence and continue |
| D2 | Difference affects acceptance but can be safely isolated | Isolate it and record the boundary in the Full Manifest |
| D3 | Overlap, conflict, or dirty-change ownership is unknown | Stop writes and escalate |

Never guess ownership. Never stash, reset, clean, discard, or overwrite changes to reduce a Drift level.

When the authorized evidence cannot reliably attribute a dirty change, `unknown` is a valid ownership conclusion. Do not exceed the permitted context boundary merely to force attribution.

## Result State

```yaml
result_state: done | partial | blocked | failed
acceptance_checked:
evidence:
unverified_or_remaining:
```

- `done`: every acceptance criterion has supporting evidence.
- `partial`: useful verified progress exists, but acceptance is incomplete.
- `blocked`: progress requires a decision, permission, dependency, or external state.
- `failed`: the attempted result did not meet acceptance; preserve evidence needed to avoid repetition.

## Write-back Candidate

```yaml
target_note:
category: project_state | decision | result | failure | lesson | reusable | to_verify
candidate:
evidence:
status: verified | historical | to_verify
supersedes:
sensitive_check: passed | blocked
```

Default to candidate-only. Exclude raw chat, hidden reasoning, full shell logs, temporary output, credential values, and unsupported inference. A user decision requires explicit user confirmation.

## Handoff

```yaml
handoff_updated:
last_agent:
task_ref:
current_goal:
result_state: done | partial | blocked | failed
current_state:
completed_and_evidence:
current_breakpoint:
next_action:
blockers_or_decisions:
do_not_do:
owned_changes:  # required when the working tree is not clean
  created_by_current_agent:
  pre_existing:
  unknown:
```

When the working tree is clean, omit `owned_changes`. When it is dirty, identify current-agent, pre-existing, and unknown changes from evidence. Any material unknown ownership is D3 and requires STOP.

Create a formal Handoff only when an agent takeover, resumable interruption, important milestone, material state change, consequential failure, or unfinished end-of-session state occurs.

### Engineering recovery minimum

Use this minimum only for an engineering takeover. Ordinary non-engineering Handoffs keep the smaller schema above and omit irrelevant fields.

```yaml
task_ref:
project_id:
authority_note:
canonical_repo:
result_state: done | partial | blocked | failed
current_state:
  branch:
  head: <full 40-character commit SHA>
  working_tree:
    status: clean | dirty
    staged:
    unstaged:
    untracked:
completed_and_evidence:
current_breakpoint:
next_action:
do_not_do:

# Required when continuing work may write engineering files.
allowed_write_paths: <list or exact Manifest reference>

# Required when the project has automated tests.
tests:
  command: <exact command>
  observed_result:
  expected_count:  # required only when a stable baseline exists
  observed_count:

# Required only when the working tree is dirty.
owned_changes:
  created_by_current_agent:
  pre_existing:
  unknown:

# Required only for push, pull request, or remote synchronization work.
upstream_or_remote:

# Required only for external systems, paid APIs, deployment, or material cost.
permissions_and_cost:

# Recommended when they add recovery value.
last_agent:
runtime:
blockers_or_decisions:

# Optional; do not require these merely for completeness.
handoff_updated:
model_version:
commit_trailer:
```

Required fields are `task_ref`, `project_id`, `authority_note`, `canonical_repo`, `result_state`, branch, full 40-character HEAD, staged/unstaged/untracked state, `completed_and_evidence`, `current_breakpoint`, `next_action`, and `do_not_do`. Apply each conditional field only under its stated trigger. A commit trailer is optional auxiliary metadata; Runtime and Agent identity belong primarily in the Handoff, and historical commits must not be amended merely to normalize trailers.

## Takeover Check

```yaml
task_ref_matches:
project_identity_reverified:
authoritative_entry_read:
manifest_understood:
git_state_reverified:
owned_changes_reconciled:
drift_level: D0 | D1 | D2 | D3
acceptance_and_evidence_understood:
permissions_reconfirmed:
safe_to_continue: yes | no
reason:
```

The receiving agent treats the Handoff as a navigation aid, not unquestionable truth. `safe_to_continue: yes` requires a known Project Identity, adequate permission, and no unresolved D3.

## Takeover context declaration

Use this declaration only for a Pilot, collaboration audit, or session-isolation evaluation. It is not required for ordinary engineering Handoffs.

```yaml
session_context:
  fresh_session: declared_yes | declared_no | unknown
  previous_agent_chat_received: declared_yes | declared_no | unknown
  kang_reexplanation_required: yes | no | unknown
```

Declared Evidence is not Independently Verified Evidence. Do not infer any of these values from Git, commit authorship, a model name, or a commit trailer. Do not add hidden-reasoning receipt, token counts, context-window size, Agent scores, or benchmark scores.
