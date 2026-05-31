---
title: "PRSentinel"
summary: "Multi-agent pull request review powered by Xiaomi MiMo — Security, Quality, Test, and Architect agents in parallel"
coverImage: "/assets/prsentinel.svg"
order: 3
---

**PRSentinel** is a multi-agent pull request review system powered by
Xiaomi MiMo. Open or update a PR and four specialized AI agents —
**Security**, **Quality**, **Test**, and **Architect** — analyze the diff
in parallel, then post a single sticky comment with severity-ranked
findings, suggested fixes, and full token telemetry.

## Stack

- Next.js + TypeScript
- Xiaomi MiMo (with Claude / OpenRouter fallback)
- Octokit + GitHub Webhooks (HMAC-verified)
- Deployed on Vercel

## Links

- Live: [prsentinel.vercel.app](https://prsentinel.vercel.app)
- Source: [github.com/g4rrzx/prsentinel](https://github.com/g4rrzx/prsentinel)

## Notes

The pipeline is deliberately defensive. A webhook arrives, the HMAC
signature is verified, and the unified diff is pulled via Octokit. The
work then fans out to four agents, each with a focused system prompt:

- **Security Agent** — OWASP, injection, authn/authz, secrets, and
  Web3-specific risks like reentrancy and missing access control.
- **Quality Agent** — readability, naming, complexity, dead code, and
  error-handling gaps.
- **Test Agent** — coverage gaps, missing edge cases, untested failure
  paths.
- **Architect Agent** — coupling, layering, breaking API changes, and
  migration safety.

Each agent returns strict JSON; a normalizer drops malformed entries
instead of failing the whole run. The aggregator severity-ranks every
finding, computes an `approve` / `request-changes` / `comment` verdict,
and upserts a single PR comment that updates in place on each push — with
a per-agent token and latency footer. The multi-agent split matters
because one giant prompt dilutes attention; specialized reviewers each go
deep on their own concern.
