---
name: sniff-check
description: "Personal design, PR/MR review and preference-learning workflow: cross-check material plans, verify claims against evidence, and check final changes before creating or merging requests on any Git platform."
type: prompt
whenToUse: "Before creating or merging a pull request (PR) or merge request (MR) on any Git platform, including GitHub, GitLab, Bitbucket, and others, whether through a platform CLI such as gh or glab, git push, or the web UI; when reviewing whether a PR/MR is deliverable; when the user explicitly corrects, rejects, or repeatedly emphasizes an implementation approach."
disableModelInvocation: false
arguments:
  - stage
  - target
---

Run the personal Sniff Check workflow. Arguments: `stage` is one of `plan`, `create`,
`merge`, `review`, or `learn`; `target` is a PR/MR, a branch, or feedback text.
Infer both from the current task when omitted.

Rules are maintained in exactly one place:

- Review standard: `references/rules.md`, relative to this skill (English,
  project-agnostic; no dev-environment or project-specific statements).
- Explicit user feedback records: `references/observations.md`.

Run the matching process from `references/rules.md`:

- `plan`: cross-check the requirements, current behavior, alternatives and
  material technical claims before implementation; report decisions and gaps.
- `create`: full pre-PR/MR checks, including independent review and evidence.
- `merge`: re-check the final head, target, discussions and verification.
- `review`: output blockers, verification gaps, and non-blocking suggestions
  only; perform no PR/MR writes.
- `learn`: update `references/rules.md` and `references/observations.md`
  following the continuous-learning rules, keeping a single source of truth
  instead of duplicating rules into the skill.

Never create or merge when a blocker exists. These are Agent workflow
instructions, not an installed technical gate. Do not add hooks, wrapper
commands, stage environment markers or background review services to activate them.
The same review applies before merging manually in any Git platform's web UI.

Manual entry points:

- `/skill:sniff-check create`
- `/skill:sniff-check plan <design or claim>`
- `/skill:sniff-check merge <PR/MR>`
- `/skill:sniff-check review <PR/MR>`
- `/skill:sniff-check learn <new user feedback>`
