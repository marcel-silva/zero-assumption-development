# Validation record

**Preparation date:** 14 October 2026.  
**Local runtime:** Python 3.13.5 on Linux.  
**Package:** ZAD 1.0.0, renamed toolkit with V2 script filenames.

## Publication boundary

The main README draft and demo README are held outside the publication tree for maintainer review. The destination repository's existing one-line README and MIT licence are preserved. The old repository is not modified or deleted, and its commit history is not imported into the new repository.

## Executed local checks

`python scripts/ValidateZADV2.py --allow-pending-readmes` completed successfully. It checked 25 required non-README files, existing inline relative Markdown links, Python syntax, selected question examples, and basic issue-template metadata. The explicit flag does not certify README publication readiness. It does not validate external URLs or every Markdown feature.

The same validator without the flag correctly rejected the pending publication. In a separate disposable copy containing both proposed README files, full validation passed. Those draft files were not added to the publication tree.

`python scripts/RunDemoV2.py` completed successfully:

| Fixture | Tests run | Failures | Errors | Skipped |
| --- | ---: | ---: | ---: | ---: |
| Intentionally defective starter | 16 | 6 | 0 | 0 |
| Reference correction | 16 | 0 | 0 | 0 |

The starter's failures are expected. The runner checks that its defect is detected and the reference satisfies the tested contract.

## Additional QA

15 local scenarios passed their expected outcomes. These included publication-tree validation, rejection of the pending READMEs in full mode, full validation with local drafts, fixture checks, candidate acceptance/rejection, and a missing-candidate error.

Disposable-copy mutation tests also confirmed rejection of a missing agreement, broken and escaping local links, invalid Python syntax, a non-question example, an accidentally repaired starter, and a broken reference.

Class and function names were compared with the source scripts and preserved. File paths and text were checked for obsolete branding. The existing README and licence bytes were checked separately to ensure they were not part of the write set.

## Limits

No live Codex, Claude Code, or GitHub Copilot integration session was run. Integration documentation was checked; behaviour was not tested end to end in each client.

No comparative AI experiment was run. These checks do not establish that ZAD improves accuracy, speed, security, or developer outcomes.

No README draft, tagged release, or social announcement is authorised by this publication step. The prepared repository tree and its commit must be checked separately after upload.
