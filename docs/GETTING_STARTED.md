# Getting started with ZAD

Start with one bounded development task, not a reorganisation of your whole workflow. Assume you and the AI do not understand that task yet, then use the repository and supplied context to find out. Existing facts and decisions still count; the point is to check the assumptions that could change your solution.

## Load the agreement

Copy `ZAD.md` into the project where work will happen. Preserve existing team instructions. Use the [tool integration guide](TOOL_INTEGRATIONS.md) or attach the file directly to a session.

A setup question can be:

> Can we use the attached ZAD agreement for this task, with you responding normally, investigating available evidence, and asking only when an important unresolved decision needs my input?

Do not assume that merely creating a file named `ZAD.md` makes every assistant load it automatically.

## Ask about the problem

Provide useful data alongside a real question. The data may contain ordinary statements, test output, or code; it does not need question marks.

Context:

```text
Observed: page 1 omits the first ten records.
Expected: pages are one-based and contain ten records.
Constraint: preserve the public API and do not change database queries.
Scope: investigation only; no file edits yet.
```

Question:

> What is causing the missing records, which code and tests support that diagnosis, and what is the smallest fix that respects these constraints?

The assistant should inspect the implementation and existing tests. It should not ask you which file contains the paginator when it can search the repository.

## Resolve only decisions that matter

Suppose the tests and API documentation disagree about whether page zero is valid. The assistant should surface the conflict. It can recommend an interpretation, but should not silently redefine a public contract.

A useful AI clarification is:

> The documentation rejects page zero but an existing test accepts it; should we preserve the currently supported behaviour or change the public contract?

The developer can keep the question-only convention while deciding:

> Can we preserve the documented one-based contract, reject page zero, and update the contradictory test as part of this fix?

This is appropriate only when the developer actually has authority to make that choice. ZAD does not determine organisational approval rights.

## Authorise implementation clearly

> Can you implement the selected fix within that scope, add tests for the first, middle, final, and empty pages, and run the relevant checks?

The assistant should now implement rather than repeatedly ask whether it is allowed to begin. It should provide a concise explanation before a consequential change, not a transcript of internal reasoning.

## Review evidence

A useful completion report gives the changed paths, actual test command, actual outcome, and anything not checked. It should say when it could not run the tests.

> Which acceptance criteria are verified, what remains untested, and does the diff contain any unrelated changes?

## Use fewer turns for small tasks

Discovery, investigation, design, implementation, and validation can happen in one turn when the problem, authority, and constraints are clear:

> Can you investigate and fix the one-based pagination defect, keep the public API unchanged, add regression tests, and report the evidence and checks, asking me only if an important contract decision remains unresolved?

## Stop when the cost exceeds the value

Do not ask for alternatives where there is no meaningful trade-off. Do not generate a large decision record for a tiny change. Reduce ceremony while preserving the evidence and authority boundaries.
