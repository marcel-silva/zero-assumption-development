# ZAD prompt library

These are starting points, not universal prescriptions. Supply actual context and define the action boundary. Every ZAD example below is a question ending in `?`.

## From commands to inquiry

| Traditional prompt | ZAD prompt | Initial action boundary |
| --- | --- | --- |
| Fix this bug. | What is causing this bug, which evidence supports the diagnosis, and how could it be fixed? | Investigate and recommend. |
| Implement authentication. | What authentication approach best fits this application's requirements and constraints? | Compare and recommend. |
| Refactor this class. | How could this class be simplified without changing its observable behaviour? | Assess and propose. |
| Write unit tests. | Which tests would verify this functionality and cover the likely failure cases? | Identify tests. |
| Optimise this query. | What is making this query slow, and which measurement would justify a particular optimisation? | Investigate and measure safely. |
| Review security. | What security weaknesses are supported by the available code and configuration evidence? | Review without exploitation or changes. |

The ZAD versions above do not automatically authorise implementation. Add a clearly scoped implementation question when needed.

## Discovery

> What problem are we actually solving, who is affected, and what observable outcome would count as success?

> Which assumptions in this request could change the solution if they are wrong?

> What can you establish from the existing repository before asking me for more information?

## Investigation

> Which code path produces this behaviour, and what evidence rules out the most plausible alternatives?

> Do the implementation, tests, and documentation agree about the intended behaviour?

> What is the smallest safe reproduction that would distinguish these two explanations?

## Design

> Which solution best satisfies the stated constraints, and what material trade-off would change your recommendation?

> What is the smallest change that solves the problem without widening the public interface?

> Which decision genuinely needs my input, and which implementation details can you resolve from the codebase?

## Authorised implementation

> Can you implement the selected solution, preserve the agreed interfaces, add the relevant tests, and avoid unrelated changes?

> Can you investigate and fix this bounded defect, explain any consequential decision, and stop only if an unresolved requirement prevents a safe choice?

> Can you prepare the migration and rollback plan for review without applying either to a live database?

## Validation and review

> Which checks did you actually run, what did they establish, and what remains unverified?

> What counterexample would show that this implementation does not satisfy the requirement?

> Does the diff introduce any behaviour, dependency, or data exposure outside the authorised scope?

## Developer answers that remain questions

> Can we choose option B and preserve the existing API for this release?

> Can you use a 30-minute timeout, as agreed, and leave production settings unchanged?

> Can we treat that assumption as unresolved and continue only with the independent local tests?

## Prompts to improve

“Can you make it better?” leaves the goal and authority unclear. Ask what must improve and how that improvement will be checked.

“Wouldn't rewriting everything in another framework be best?” embeds a preferred answer. Ask which options satisfy the constraints instead.

“Can you delete the failing tests?” may authorise the wrong action. Ask whether the tests or implementation conflict with the accepted contract before changing either.
