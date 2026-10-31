# Sniff Check Review Standard

This document is the single source of truth for pull request (PR) and merge
request (MR) review and merge checks on any Git platform. PRs and MRs are both
called requests below. Records of explicit user feedback live in
`references/observations.md`; this document describes only currently effective
preferences. Assistant suggestions, review-bot opinions, and assistant fix
reports are not user preferences.

## Request Workflow

### Before implementation and when explaining a design

Start with the user's requirements, relevant contracts, schema and recorded
decisions. Check the actual implementation and its callers; do not infer the
requirements from existing code or treat an assistant proposal as user approval.
Separate confirmed requirements, current behavior, proposed changes and unknowns.

For material architecture or cleanup, compare independently developed approaches
from more than one angle, then cross-check the combined proposal. Look for missing
consumers, lifecycle and failure paths, authority boundaries and unnecessary
complexity. Revisit the proposal when evidence changes it. A code review after
implementation does not replace this earlier design check.

Technical explanations also need evidence: trace the named component to its
callers, credentials, state and runtime role before making a claim. A filename or
configuration entry alone does not prove that a process runs or a path is used.
State what was checked and what remains unknown. Read-only consultation does not
start a code-review delivery cycle.

### Before opening a request

1. Review the split. Default: each request is an indivisible small change;
   multiple features go into separate requests even when related, as long as
   they can be reviewed and delivered independently. Never default to an
   all-in-one request.
2. Base the branch on the latest target branch with a clean worktree and read
   the full diff.
3. Check implementation, configuration, contracts, state, security, naming,
   verification, and delivery residue against the rules below.
4. Run the narrowest relevant format checks, lint, tests, and at least one
   real smoke; for refactors also prove behavior equivalence.
5. Fix blockers first. If the change should be split, split branches and
   requests instead of explaining the scope in review text.
6. Record the final head/base, rule version, independent findings and their
   disposition, validation evidence and remaining gaps. This is a manual Agent
   workflow, not a technical gate. Do not add hooks, wrapper commands, stage
   environment markers or background review services to start it.

### Independent cross-validation

- R1: use a fresh-context reviewer to read the requirements, affected contracts
  and complete diff for correctness, state, security, tests and regressions.
- The author checks each finding against files and observable behavior, fixes
  real issues and gives checkable reasons for false positives. Another model's
  disagreement is not itself a reason to reject a finding.
- R2: use another fresh context to check the repaired complete diff against
  original requirements, decisions, all S01-S12 and D01-D02 rules, and R1's
  disposition. Earlier findings are leads, not authority.
- If R2 still finds a real blocker, repair it and allow one final complete R3.
  If R3 still has a real blocker, stop delivery/merge, report it and reconsider
  the design. Do not change prompts or retry indefinitely to obtain approval.
- Reviewers are read-only: no edits, nested reviewers, PR writes or merges.
  Supply the repo, head/base, full diff, rule and source versions, requirements
  and test evidence. Do not give them the author's generation reasoning as facts.
- Keep findings, evidence, impact and disposition. A successful process exit,
  empty output, vote or "approve" is not proof of review. If independent review
  is unavailable or authentication fails, report the gap.

Review at independently deliverable request boundaries, not every commit. Reuse
valid evidence when code and requirements are unchanged; otherwise check the
impact. Before merge, the conclusion must cover the current complete diff and
all applicable discussions, not an older approved commit.

### Before merging

1. Re-read the request's final head, target branch, and full diff; never reuse
   conclusions from older commits.
2. Check the request is still an indivisible small change with no independently
   deliverable extras or unrelated edits.
3. Collect all discussions, CI, and final verification evidence. Open
   applicable threads, failing checks, final images/digests, and real
   end-to-end results must be closed.
4. Re-review the final state, focusing on complexity added during review,
   compatibility residue, contract changes, and verification gaps.
5. Stop when a blocker exists. Follow the user's authorization and the hosting
   platform's approval requirements; this skill does not grant permission to
   merge or release.
6. Apply the same process before merging manually in any Git platform's web UI;
   local hooks cannot intercept web actions.

### Review only

Report blockers, verification gaps, and non-blocking suggestions. Each blocker
must name the file or behavior, the violated rule, and the fix direction. Do
not post review comments, resolve human discussions, or change shared
standards or CI unless the user asks.

### Design iteration reports

Use Chinese unless the user requests another language. Lead with the conclusion
and this iteration's changes, then address the user's feedback in order, keeping
annotation correspondence when supplied. Explain the architecture, reasons,
boundaries and tradeoffs without listing every implementation detail. Name the
old approach being replaced or removed. Use a comparison table when it helps
review acceptance behavior and regressions. Separate confirmed/proposed and
implemented/verified/deployed states; a plan is not a completion report.

## Core Sniff Rules

### S01 — Indivisible small requests; no all-in-one

- Priority: highest.
- Signals: one request contains multiple independently reviewable/deliverable
  features; a request keeps expanding after the approach changes; "related
  features" justifies a large diff.
- Direction: split into indivisible small requests by default. Features in the
  same roadmap still get separate requests when independently deliverable.
  Changes required for one feature stay together so it builds, tests, and reads
  cleanly.
- Review question: does this request solve exactly one problem? Could any part
  ship independently? If yes, why is it here?
- Boundary: do not split mechanically by file or line count. Do not shred a
  feature into unverifiable fragments, and do not bundle features on "same
  semantics" grounds.
- When additions plus deletions exceed 1,000 lines, explicitly identify the
  independently deliverable requirements, dependencies and acceptance behavior.
  Keep one request only when a reasonable independent split is not possible;
  record why. Line count prompts this analysis, not automatic fragmentation.

### S02 — Complexity must pay for itself now

- Priority: strong.
- Signals: dead parameters, fields with no consumer, redundant wrappers,
  duplicate nesting, placeholder features, generic design beyond current
  needs, unnecessary submodules/prechecks/persistence.
- Direction: remove mechanisms with no independent responsibility. Keep an
  abstraction only when it clearly improves readability, reuse, or boundary
  clarity.
- Deployment default: prefer a monolith over distributed services, and a
  single-device network deployment over multiple devices. Independent module
  responsibilities do not require independent processes or machines. Depart
  from the default only with current evidence that it cannot satisfy an actual
  requirement; account for network/operations cost, verification and rollback.

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
- Once a one-off operation is complete and no active consumer needs it, remove
  its command, sole-use package, tests, build/deployment references and obsolete
  instructions together. Keep runtime schema handling or versioned migrations
  still needed for supported installations. Do not keep an unused command merely
  as a possible future fallback.
- When the task requires an invisible refactor, compare observable behavior
  before and after: interactions, presentation, navigation/reading position,
  loading/errors and API results. Removing functions or UI behavior is not code
  simplification. This applies to behavior-preserving work, not a ban on later
  product changes the user requests.

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
- For frontend effects, inspect the actual rendered application with browser
  or computer use: spacing, clicks, loading and results. Unit tests or screenshots
  without interaction cannot prove that copying, authentication or tool loading
  actually works. Exercise the original failing conditions and distinguish real
  services from mocks, recordings, QA identity fixtures and production ingress.
- For cleanup, enumerate consumers across code, scripts, clients and generated
  contracts, including string-based calls. A declaration or a test fixture alone
  does not establish a current product consumer; failure to find a function call
  alone does not establish that it is unused.

### S10 — Environment variables and credentials are split by destination, consumer, and sensitivity

- Priority: strong.
- Signals: runner/Harbor/agent-sandbox sharing undemuxed env; classifying by
  TOKEN name rather than consumer; platform orchestration tools exposed to
  the evaluated agent; user keys baked into images.
- Direction: every variable has an explicit destination, consumer, and
  sensitivity; validate, redact, and assemble separately; unknown
  destinations are not forwarded by default; platform and agent credentials
  are separated; user run identities and directories are isolated. When a
  configuration payload is passed through an environment variable, check its
  size against the transport's limits (per-string ~128 KiB, argv+env
  ~2 MiB, and platform-specific limits such as CI variables or
  ConfigMap/Secret ~1 MiB); for large or unbounded inputs, use a file or a
  structured spec instead of an env var.

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
least two independent request reviews/sessions, or when the user states it as
a general principle.

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
4. Promote to core with evidence from at least two independent request
   reviews/sessions, or when the user states a general principle.
5. When the user refines, corrects, or retracts a rule, update the current
   definition and boundaries directly; keep the parts still binding and drop
   contradictory old wording.
6. Distinguish one-off project constraints from stable preferences; do not
   generalize a local decision into an absolute ban.

## Scope Boundaries

- Well-justified abstractions, defaults, thresholds, caches, compatibility
  layers, or platform changes are allowed.
- The request split preference is explicit: indivisible small requests by
  default, separate requests for separate features, no all-in-one; do not
  re-expand a request on "cohesion" grounds.
- Compatibility is judged by real adoption, migration cost, and whether the
  old mechanism will actually be removed.
- Tests should answer the current question, not chase uninformative
  repetition.
- Prefer the smallest change layer, but when the root cause is in the
  platform, a necessary platform fix is still allowed.
