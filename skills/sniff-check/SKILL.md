---
name: sniff-check
description: "Personal PR/MR review and preference-learning workflow for any Git platform: mandatory checks before creating or merging pull requests or merge requests; use when reviewing PRs/MRs, handling review feedback, or when the user corrects an implementation."
type: prompt
whenToUse: "Before creating or merging a pull request (PR) or merge request (MR) on any Git platform, including GitHub, GitLab, Bitbucket, and others, whether through a platform CLI such as gh or glab, git push, or the web UI; when reviewing whether a PR/MR is deliverable; when the user explicitly corrects, rejects, or repeatedly emphasizes an implementation approach."
disableModelInvocation: false
arguments:
  - stage
  - target
---

Run the personal Sniff Check workflow. Arguments: `stage` is one of `create`,
`merge`, `review`, or `learn`; `target` is a PR/MR, a branch, or feedback text.
Infer both from the current task when omitted.

Rules are maintained in exactly one place:

- Review standard: `${KIMI_SKILL_DIR}/references/rules.md` (English,
  project-agnostic; no dev-environment or project-specific statements).
- Explicit user feedback records: `${KIMI_SKILL_DIR}/references/observations.md`.

Run the matching process from `references/rules.md`:

- `create`: full pre-PR/MR checks. Only after passing, prepend
  `SNIFF_CHECK_REVIEWED=create;` to the creation command.
- `merge`: re-check the final head completely. Only after passing, prepend
  `SNIFF_CHECK_REVIEWED=merge;` to the merge command.
- `review`: output blockers, verification gaps, and non-blocking suggestions
  only; perform no PR/MR writes.
- `learn`: update `references/rules.md` and `references/observations.md`
  following the continuous-learning rules, keeping a single source of truth
  instead of duplicating rules into the skill.

Never add the confirmation marker, create, or merge when a blocker exists.
The same review applies before merging manually in any Git platform's web UI.

Manual entry points:

- `/skill:sniff-check create`
- `/skill:sniff-check merge <PR/MR>`
- `/skill:sniff-check review <PR/MR>`
- `/skill:sniff-check learn <new user feedback>`
