# Capability Profiles

Profiles describe runtime differences only. They do not copy the Core workflow and do not grant task permission.

The profile subject is the Runtime or Harness. An underlying model may be recorded as a verification variable, but model brand or version does not establish Runtime capability.

Capability values:

- `available`: verified as directly available in the identified runtime.
- `conditional`: available only with a tool, configuration, path grant, or session capability.
- `unavailable`: verified absent in the identified runtime.
- `unknown`: insufficient evidence; treat as `to_verify`.

## Profile contract

```yaml
profile_id:
runtime:
skill_activation:
context_access:
  repository:
  obsidian:
execution:
  shell:
  git:
  browser:
  computer_use:
handoff:
  can_consume:
  can_produce:
permission_notes:
escalation_conditions:
last_verified:
verification_notes:
```

## Codex

```yaml
profile_id: codex-local
runtime: Codex desktop or CLI with local workspace tools
skill_activation: available
context_access:
  repository: conditional
  obsidian: conditional
execution:
  shell: available
  git: available
  browser: conditional
  computer_use: conditional
handoff:
  can_consume: available
  can_produce: available
permission_notes: Filesystem scope, tools, network, Git actions, and writes remain task- and environment-specific.
escalation_conditions: Missing path access, missing tools, Project Identity uncertainty, or D3.
last_verified: 2026-09-12
verification_notes: Verified in the current local Codex environment; availability in another Codex session must be rechecked.
```

## ChatGPT Work

```yaml
profile_id: chatgpt-work-session
runtime: ChatGPT Work or ChatGPT session
skill_activation: unknown
context_access:
  repository: conditional
  obsidian: conditional
execution:
  shell: conditional
  git: conditional
  browser: conditional
  computer_use: conditional
handoff:
  can_consume: available
  can_produce: available
permission_notes: Use only capabilities exposed in the current session; local Vault or repository access is never assumed.
escalation_conditions: Required local context or execution capability is not exposed in the session.
last_verified: 2026-09-12
verification_notes: Text contract exchange is available; a universal local Skill loader and local tool set remain to_verify per session.
```

## Claude Code

```yaml
profile_id: claude-code-local
runtime: Claude Code 2.1.215
skill_activation: available
context_access:
  repository: available
  obsidian: conditional
execution:
  shell: available
  git: available
  browser: conditional
  computer_use: conditional
handoff:
  can_consume: available
  can_produce: available
permission_notes: Repository-external paths and optional tools require runtime configuration or explicit access.
escalation_conditions: Vault path is unavailable, required optional tools are absent, Project Identity is uncertain, or D3.
last_verified: 2026-09-12
verification_notes: Local version and official Skills, memory, hooks, and agents documentation were checked; optional integrations remain configuration-dependent.
```

## Hermes

```yaml
profile_id: hermes-local
runtime: Locally installed Hermes Agent
skill_activation: available
context_access:
  repository: conditional
  obsidian: conditional
execution:
  shell: conditional
  git: conditional
  browser: conditional
  computer_use: conditional
handoff:
  can_consume: conditional
  can_produce: conditional
permission_notes: Skill visibility and execution depend on configured external directories and enabled toolsets.
escalation_conditions: The required Skill or file tools are not visible, paths are not granted, Project Identity is uncertain, or D3.
last_verified: 2026-09-12
verification_notes: Local source confirms indexed on-demand Skill loading and configurable toolsets; the active session configuration must be rechecked.
```

## OpenClaw

```yaml
profile_id: openclaw-local
runtime: OpenClaw 2026.6.10
skill_activation: available
context_access:
  repository: conditional
  obsidian: conditional
execution:
  shell: conditional
  git: conditional
  browser: conditional
  computer_use: conditional
handoff:
  can_consume: conditional
  can_produce: conditional
permission_notes: Skill visibility does not grant shell, filesystem, browser, or other tool permission.
escalation_conditions: Skill allowlist or workspace access is missing, required tools are disabled, Project Identity is uncertain, or D3.
last_verified: 2026-09-12
verification_notes: Local version and documented workspace, managed, and shared Skill roots were checked; tool grants remain agent-specific.
```

## DeepSeek Harness

```yaml
profile_id: deepseek-harness
runtime: DeepSeek Harness
skill_activation: unknown
context_access:
  repository: unknown
  obsidian: unknown
execution:
  shell: unknown
  git: unknown
  browser: unknown
  computer_use: unknown
handoff:
  can_consume: unknown
  can_produce: unknown
permission_notes: Do not infer Harness capabilities from the DeepSeek model API or from another project's adapter design.
escalation_conditions: Before participation, verify how this concrete Harness loads instructions, accesses files, executes tools, and exchanges handoffs.
last_verified: 2026-09-12
verification_notes: No general local or official Harness Skill runtime was verified; all operational capabilities remain to_verify.
```

## Adding a runtime

Add one profile using the contract above. Record only observed or authoritative capabilities, mark missing evidence `unknown`, and keep invocation details here. Do not modify the Core workflow unless the shared interoperability contract itself changes.
