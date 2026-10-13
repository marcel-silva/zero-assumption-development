# ZAD 1.0 — Zero-Assumption Development

**Preparation notes. A tagged release has not been published. README files are pending maintainer review.**

Start every task assuming you and the AI do not understand it yet. Check the problem before committing to a solution. "Zero-assumption" means not treating unchecked assumptions as facts; existing requirements, decisions, and evidence remain useful context.

Developer task prompts are questions. The AI responds normally, investigates available evidence, explains consequential choices, and implements clearly authorised work. It asks when an important decision cannot safely be made from the available information.

## Included in this publication

The manifesto, reusable `ZAD.md` agreement, prompt library, worked examples, task and experience-report templates, integration guidance, contribution materials, and proposed evaluation protocol have been adapted to the ZAD name.

The Python pagination fixtures and validation scripts use V2 filenames. Their public class and function names are unchanged. The demonstration checks a code fixture; it is not an AI benchmark.

## Pending review

The main README draft and demo README are held separately. The destination repository's initial README is not replaced. No README draft should be added on any branch until approved.

## Evidence status

No controlled study establishing ZAD's superiority is included. Tool-loading guidance is based on primary documentation, not end-to-end testing in each client. See [Validation](VALIDATION.md) for the checks performed on this package.

## Start

Use [Getting started](GETTING_STARTED.md), then load `ZAD.md` in one project and try a bounded task.

MIT licensed. Proposed by Marcel Silva.
