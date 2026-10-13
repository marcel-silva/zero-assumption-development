# Contributing to ZAD

Contributions should make ZAD easier to use, easier to evaluate, or clearer about its limits.

## Useful contributions

Practical experience reports, failure cases, clearer questions, verified tool-loading instructions, translations, relevant prior work, and controlled comparisons are welcome.

Use the issue templates for methodology proposals and experience reports. For a larger change, describe the problem and evidence before rewriting the agreement.

## Preserve the core

ZAD means inquiry, evidence, and controlled execution. Preserve its starting point: neither the developer nor the AI should assume the task is understood before checking the relevant context. The name does not require zero uncertainty; it requires separating evidence from unchecked assumptions. Developer prompts are questions. AI responses are normal. Clarification is selective, not continuous. Keep authority separate from confidence.

Do not introduce unsupported claims of speed, accuracy, safety, adoption, or originality. Label authored demonstrations as illustrative and report actual measurements separately.

## Changes and review

Keep pull requests focused. Explain what problem the change addresses, what evidence supports it, and whether it changes the working agreement. Update affected examples and version notes together.

Run the repository checks with Python 3.10 or newer:

```sh
python scripts/ValidateZADV2.py --allow-pending-readmes
python scripts/RunDemoV2.py
```

The README files are pending maintainer review. The flag above explicitly validates the rest of the toolkit; after those files are approved and added, omit it to run the full check. Do not publish README drafts without approval.

The intentionally defective starter is a fixture, not an unfixed production defect. Preserve its purpose.

## Privacy and conduct

Publish only material you are entitled to share. Remove secrets, private customer information, and employer code without publication permission. Critique claims and implementations rather than contributors. Do not fabricate endorsements or results.

For a suspected sensitive data exposure, do not repeat the exposed data in a public issue. Use an available private reporting channel; this initial release does not promise a dedicated security-response service.

## Licence and attribution

Contribute original or appropriately licensed material. Contributions are offered under the repository's MIT licence unless explicitly agreed otherwise before inclusion. Keep required third-party notices and identify external sources.

This proposal is maintained initially by Marcel Silva. Substantive changes to the core methodology should receive maintainer review. No contributor is required to disclose private internal AI reasoning; concise evidence and decision explanations are sufficient.
