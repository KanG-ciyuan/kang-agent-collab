# Security policy

`kang-agent-collab` is a text-based Skill and protocol, but its artifacts can refer to repositories, shared memory, permissions, and working-tree state. Treat those records as potentially sensitive.

## Supported version

Security fixes are accepted for the current `0.2.x` line. Earlier snapshots may be used for historical comparison but are not maintained as separate supported releases.

## Report a vulnerability privately

Do not disclose credentials, private paths, private repository URLs, internal documents, or exploitable details in a public issue.

Prefer GitHub Private Vulnerability Reporting from the repository's **Security** tab when it is available. If it is not available, open a minimal public issue asking the maintainer for a private contact channel; include no sensitive detail in that issue.

Include only the minimum information needed to reproduce the problem:

- affected version or commit;
- relevant contract or file;
- impact and safe reproduction steps;
- whether credentials or private project material may have been exposed;
- a proposed mitigation, if known.

## Sensitive data rules

Never place these values in a Manifest, Handoff, shared-memory record, example, issue, pull request, or commit:

- API keys, tokens, passwords, cookies, private keys, or Authorization headers;
- complete credential files or environment files;
- private repository or internal-only URLs unless disclosure is explicitly authorized;
- personal local paths, private Vault paths, conversation dumps, or raw debug logs;
- unrelated personal or client information.

When reporting a possible secret, provide the variable name and file location, not the value. Existing credentials must not be moved, replaced, revoked, or deleted without explicit owner authorization.

## Safe recovery behavior

If a credential appears in project state or Git history, stop publication and preserve evidence without printing the value. If dirty-change ownership is unknown, do not stash, reset, clean, discard, or overwrite it.
