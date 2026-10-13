# Working in the ZAD repository

Read `ZAD.md` before substantive work. It is the canonical working agreement.

This repository contains a proposed methodology, documentation, templates, and a Python demonstration. Keep the distinction between a proposal, an illustration, and an empirical result explicit.

Preserve the three pillars: inquiry, evidence, and controlled execution. Start by checking understanding of the task, not by assuming a proposed solution is correct. "Zero-assumption" means not treating unchecked assumptions as facts; it does not require ignoring established requirements or rechecking every minor detail. Do not redefine ZAD as punctuation alone or require the AI to respond only with questions.

Do not edit `demo/PaginationStarterV2.py` to make it pass: its defect is intentional. The demo runner checks that the starter fails and the reference passes. Make experiment copies outside this repository.

Use Python 3.10 or newer, with no third-party Python dependencies:

```sh
python scripts/ValidateZADV2.py --allow-pending-readmes
python scripts/RunDemoV2.py
```

The README files are awaiting maintainer review and are not included in this publication step. Do not add, replace, or publish them without explicit approval. The `--allow-pending-readmes` flag checks the remaining toolkit; omit it for a full validation after the reviewed README files have been added.

The validation commands are local. They do not call an AI provider or publish anything. Do not claim that they benchmark ZAD.

For code deliverables, preserve public class and function names. Keep the version suffix on script filenames. Canonical integration files such as `AGENTS.md` and `ZAD.md` retain their recognised names.

Never publish private source code, secrets, personal correspondence, or fabricated user testimonials. Do not push, create a release, or change repository visibility without clear authorisation.
