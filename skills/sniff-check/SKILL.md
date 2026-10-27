---
name: sniff-check
description: "Personal MR review and preference-learning workflow: mandatory checks before creating or merging MRs; use when reviewing MRs, handling MR feedback, or when the user corrects an implementation."
type: prompt
whenToUse: "Before glab mr create, glab mr merge, or creating an MR by git push; when reviewing whether an MR is deliverable; when the user explicitly corrects, rejects, or repeatedly emphasizes an implementation approach."
disableModelInvocation: false
arguments:
  - stage
  - target
---

Run the personal Sniff Check workflow. Arguments: `stage` is one of `create`,
`merge`, `review`, or `learn`; `target` is an MR, a branch, or feedback text.
Infer both from the current task when omitted.

Rules are maintained in exactly one place:

- Review standard: `${KIMI_SKILL_DIR}/references/rules.md` (English,
  project-agnostic; no dev-environment or project-specific statements).
- Explicit user feedback records: `${KIMI_SKILL_DIR}/references/observations.md`.

Run the matching process from `references/rules.md`:

- `create`: full pre-MR checks. Only after passing, prepend
  `SNIFF_CHECK_REVIEWED=create;` to the creation command.
- `merge`: re-check the final head completely. Only after passing, prepend
  `SNIFF_CHECK_REVIEWED=merge;` to the merge command.
- `review`: output blockers, verification gaps, and non-blocking suggestions
  only; perform no MR writes.
- `learn`: update `references/rules.md` and `references/observations.md`
  following the continuous-learning rules, keeping a single source of truth
  instead of duplicating rules into the skill.

Never add the confirmation marker, create, or merge when a blocker exists.
The same review applies before merging manually in the GitLab web UI.

Manual entry points:

- `/skill:sniff-check create`
- `/skill:sniff-check merge !123`
- `/skill:sniff-check review !123`
- `/skill:sniff-check learn <new user feedback>`
