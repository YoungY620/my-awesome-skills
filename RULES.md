# MR Sniff Review Standard

This document is the single source of truth for MR review and merge checks.
Records of explicit user feedback live in `references/observations.md`; this
document describes only currently effective preferences. Assistant
suggestions, review-bot opinions, and assistant fix reports are not user
preferences.

## MR Workflow

### Before opening an MR

1. Review the split. Default: each MR is an indivisible small change; multiple
   features go into separate MRs even when related, as long as they can be
   reviewed and delivered independently. Never default to an all-in-one MR.
2. Base the branch on the latest target branch with a clean worktree and read
   the full diff.
3. Check implementation, configuration, contracts, state, security, naming,
   verification, and delivery residue against the rules below.
4. Run the narrowest relevant format checks, lint, tests, and at least one
   real smoke; for refactors also prove behavior equivalence.
5. Fix blockers first. If the change should be split, split branches and MRs
   instead of explaining the scope in review text.
6. Only after these checks, prepend `MR_SNIFF_REVIEWED=create;` to the
   creation command. The marker records that the process was followed; it
   does not replace the actual checks.

### Before merging

1. Re-read the MR's final head, target branch, and full diff; never reuse
   conclusions from older commits.
2. Check the MR is still an indivisible small change with no independently
   deliverable extras or unrelated edits.
3. Collect all discussions, CI, and final verification evidence. Open
   applicable threads, failing checks, final images/digests, and real
   end-to-end results must be closed.
4. Re-review the final state, focusing on complexity added during review,
   compatibility residue, contract changes, and verification gaps.
5. Stop when a blocker exists. Only after passing, prepend
   `MR_SNIFF_REVIEWED=merge;` to the merge command.
6. Apply the same process before merging manually in the GitLab web UI; local
   hooks cannot intercept web actions.

### Review only

Report blockers, verification gaps, and non-blocking suggestions. Each blocker
must name the file or behavior, the violated rule, and the fix direction. Do
not post GitLab comments, resolve human discussions, or change shared
standards or CI unless the user asks.

## Core Sniff Rules

### S01 — Indivisible small MRs; no all-in-one

- Priority: highest.
- Signals: one MR contains multiple independently reviewable/deliverable
  features; an MR keeps expanding after the approach changes; "related
  features" justifies a large diff.
- Direction: split into indivisible small MRs by default. Features in the same
  roadmap still get separate MRs when independently deliverable. Changes
  required for one feature stay together so it builds, tests, and reads
  cleanly.
- Review question: does this MR solve exactly one problem? Could any part ship
  independently? If yes, why is it here?
- Boundary: do not split mechanically by file or line count. Do not shred a
  feature into unverifiable fragments, and do not bundle features on "same
  semantics" grounds.

### S02 — Complexity must pay for itself now

- Priority: strong.
- Signals: dead parameters, fields with no consumer, redundant wrappers,
  duplicate nesting, placeholder features, generic design beyond current
  needs, unnecessary submodules/prechecks/persistence.
- Direction: remove mechanisms with no independent responsibility. Keep an
  abstraction only when it clearly improves readability, reuse, or boundary
  clarity.

### S03 — One core logic and one source of truth per concern

- Priority: strong.
- Signals: dual single/multi-mode paths, coexisting old and new adapters,
  double writes, duplicated validation, two components maintaining the same
  state.
- Direction: entry points may be thin, but core logic is shared; single mode
  is a special case of the general one; new designs replace old paths;
  duplicated rules drift.

### S04 — Keep shrinking the diff without shrinking functionality

- Priority: strong.
- Signals: unrelated churn, duplicate implementations, compatibility shells
  for abandoned designs, code kept "for later", large changes vs the latest
  main.
- Direction: re-review white-box after every reduction; delete duplicates and
  dead code. A percentage target is a hint to slim down, never a reason to cut
  features, required verification, or readability.
- Boundary: when a slim side branch blocks delivery, close the side branch
  instead of holding the main delivery hostage.

### S05 — Configuration, defaults, thresholds, and fields need justification

- Priority: strong.
- Signals: unexplained numeric bounds, volatile configuration hardcoded,
  environment hostnames hardcoded, silent clamping/overwriting,
  hash/path/parameter fields with no consumer.
- Direction: state the real failure, external contract, and consumer. Prefer
  honoring supplied values; fail explicitly when that is impossible. Derive
  environment values from the target.
- Boundary: thresholds with a clear purpose may stay; this is not a ban on
  defaults.

### S06 — No agent special-casing in the generic execution path

- Priority: strong.
- Signals: adding an agent requires editing an executor if/switch;
  configuration knowledge scattered; several extension entry styles
  (alias/args/functions) coexisting.
- Direction: the execution side calls one fixed generic Prepare; each agent's
  env, validation, config files, and arguments live in its own self-contained
  adaptation unit; one extension point, one mechanism.
- Boundary: an irreducible special case may exist but needs a one-line comment
  giving the real reason.

### S07 — Identity, configuration, and state need one authority and clear semantics

- Priority: strong.
- Signals: raw URLs or display names used as identity; async state inferred
  from result presence; browser holding the only task state; writes hidden in
  read APIs; snapshots without freshness.
- Direction: normalize sources and use stable keys (paths, immutable commits);
  async lifecycles are persisted and queryable; read APIs are read-only;
  state carries a timestamp or sample-independent semantics.

### S08 — Shared contracts must not be held hostage by one implementation

- Priority: strong.
- Signals: one runner's required field promoted to a platform-wide
  requirement; registration requiring values only available after execution;
  the narrowest interface hiding underlying streaming; preparing to copy an
  upstream internal algorithm to fit a contract.
- Direction: fix the contract and responsibility split first, then adapt or
  replicate; shared fields reflect each implementation's real capabilities.

### S09 — Verification must prove the claimed behavior really happened

- Priority: highest.
- Signals: only internal functions/mocks/old images exercised; judging by exit
  codes/completed/reward/approve; configuration present but not proven
  delivered; failing tests or open threads.
- Direction: public-API black-box tests with real agents/LLMs/judges, final
  code and images, raw logs/wire/artifacts/scores/upload evidence; reproduce
  the original failure conditions; diagnose even a single failure.
- Boundary: do not repeat expensive tests when the same evidence already
  exists.

### S10 — Environment variables and credentials are split by destination, consumer, and sensitivity

- Priority: strong.
- Signals: runner/Harbor/agent-sandbox sharing undemuxed env; classifying by
  TOKEN name rather than consumer; platform orchestration tools exposed to
  the evaluated agent; user keys baked into images.
- Direction: every variable has an explicit destination, consumer, and
  sensitivity; validate, redact, and assemble separately; unknown
  destinations are not forwarded by default; platform and agent credentials
  are separated; user run identities and directories are isolated.

### S11 — Commits stay minimal, public, and reproducible

- Priority: strong.
- Signals: files beyond code and public configuration; large attachments,
  build outputs, binaries, caches, local editor settings, worktrees, abandoned
  designs, dead code, or intermediate versions in the delivery; repo
  references absolute dev-machine paths, private environment details, names,
  or personal identifiers.
- Direction: commit only code and public configuration; remove residue and
  prevent recommitting. Summaries describe only the current change; temporary
  workarounds state their removal condition. Use project-relative paths and
  public contracts; environment differences come from configuration inputs,
  not hardcoded dev directories or personal data.

### S12 — Names and directories express responsibility and dependencies

- Priority: medium-strong.
- Signals: product names broader than actual scope; "Default" that is really
  hardcoding; initial and dynamic concurrency sharing a name; every file in
  one directory; messy cross-package references.
- Direction: names describe the real product/module/lifecycle; directories
  follow conceptual responsibility and limit cross-module dependencies; pure
  refactors preserve behavior and get real regression coverage.

## Special Rules

### D01 — Investigate data anomalies before explaining them

For abnormally large, abnormally good, missing, or unexplained results, first
check raw data, parsing, samples, timestamps, concurrency windows, and the
judge. Parallel intervals must not be summed as wall-clock time; residuals
and gaps must be exposed explicitly.

### D02 — Third-party updates are explicit and reversible

Pin external repos to commits and images to digests; third-party pushes must
not silently change deployments. Upgrades are explicit actions with a
rollback path to the previous version or digest.

## Candidate Rules

A new opinion starts here. It can be promoted to core after evidence from at
least two independent MRs/sessions, or when the user states it as a general
principle.

Each candidate records: status, emphasis count, independent scenarios,
signals, direction, applicable boundaries, and evidence.

## Continuous Learning

When the user explicitly corrects, rejects, reworks, or repeatedly emphasizes
an implementation approach:

1. Record only the user's own explicit opinions. Assistant suggestions,
   review-bot opinions, and assistant fix reports do not count.
2. Append the date, source, rule ID, the user's words, and the resolution to
   `references/observations.md`. Each explicit repetition may add a record.
3. A new pattern goes to candidates on first sighting; on recurrence, update
   the existing rule and its emphasis count instead of duplicating
   near-identical entries.
4. Promote to core with evidence from at least two independent MRs/sessions,
   or when the user states a general principle.
5. When the user refines, corrects, or retracts a rule, update the current
   definition and boundaries directly; keep the parts still binding and drop
   contradictory old wording.
6. Distinguish one-off project constraints from stable preferences; do not
   generalize a local decision into an absolute ban.

## Scope Boundaries

- Well-justified abstractions, defaults, thresholds, caches, compatibility
  layers, or platform changes are allowed.
- The MR split preference is explicit: indivisible small MRs by default,
  separate MRs for separate features, no all-in-one; do not re-expand an MR on
  "cohesion" grounds.
- Compatibility is judged by real adoption, migration cost, and whether the
  old mechanism will actually be removed.
- Tests should answer the current question, not chase uninformative
  repetition.
- Prefer the smallest change layer, but when the root cause is in the
  platform, a necessary platform fix is still allowed.
