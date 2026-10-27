# my-awesome-skills

A personal, battle-tested standard for reviewing and merging merge requests —
small-MR discipline, contract and configuration hygiene, environment/credential
separation, and verification that proves the claimed behavior actually happened.

The complete standard lives in **[RULES.md](RULES.md)**. It is written to be
project-agnostic: no repo-specific paths, no environment assumptions, no
personal identifiers.

## What is in the standard

- **Workflow**: what must be true before opening an MR, before merging, and
  when doing a review-only pass (including the `MR_SNIFF_REVIEWED` markers).
- **Core rules S01–S12**: indivisible small MRs; complexity must pay for
  itself now; one source of truth per concern; shrinking diffs without
  shrinking functionality; justified configuration and defaults; no agent
  special-casing in generic paths; one authority for identity/config/state;
  shared contracts not held hostage by one implementation; verification that
  proves real behavior; env/credential separation by destination, consumer and
  sensitivity; minimal, public, reproducible commits; names and directories
  that express responsibility.
- **Special rules D01–D02**: investigate data anomalies before explaining
  them; third-party updates are explicit and reversible.
- **Candidate rules, continuous learning, and scope boundaries**: how new
  feedback becomes a rule, and where the standard deliberately does not apply.

## How to use it

1. Before opening an MR, run the "Before opening an MR" checklist and only
   then prepend `MR_SNIFF_REVIEWED=create;` to your creation command.
2. Before merging, re-read the final head and full diff, close every open
   thread and failing check, and only then prepend
   `MR_SNIFF_REVIEWED=merge;` to your merge command.
3. For review-only, report blockers, verification gaps, and non-blocking
   suggestions without writing to the MR.

## License

Content is provided as-is for review and reuse.
