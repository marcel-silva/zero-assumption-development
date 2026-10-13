# Frequently asked questions

## What does "zero-assumption" mean?

Start every task assuming you and the AI do not understand it yet. Check the relevant evidence before committing to a solution. "Zero-assumption" means not treating unchecked assumptions as facts; it does not mean that all uncertainty can be eliminated.

## Should we ignore experience or previous decisions?

No. Use existing requirements, documentation, prior decisions, and observations. Experience suggests explanations to investigate. Do not discard known facts or make the developer repeat context already available. Focus on uncertainties that could materially change the outcome.

## Is this just adding a question mark?

No. Every developer prompt is a question, but the substantive commitments are inquiry, evidence, and controlled execution. "Can you do exactly what I already decided?" is grammatically a question; without examining important assumptions it may add little to the workflow.

## Must the AI answer only with questions?

No. The AI responds normally. It asks only when an important decision cannot safely be made from available information.

## Is “Can you implement this?” allowed?

Yes. ZAD needs a way to authorise implementation. The question form does not remove the need to understand the problem, inspect relevant evidence, and validate the result.

## Must every sentence end with a question mark?

Task prompts must be questions. Supporting logs, source code, specifications, and other context may be normal statements. Static project instructions and AI responses are not subject to the question-only rule.

## What happens when I accidentally use a command?

For a ZAD session, rephrase the task request as a question. The question form is necessary for the convention, but is not sufficient: the task must still follow inquiry, evidence, and controlled execution.

## Does an investigation question authorise edits?

No. “What is causing this?” requests an investigation. A scoped implementation question makes editing authority explicit. Existing, clearly established project authority can also be relevant; the AI should not ask for the same permission repeatedly.

## Does the AI need to reveal its chain-of-thought?

No. It should provide a concise rationale, evidence, assumptions, and trade-offs that a developer can assess. ZAD does not require access to private internal reasoning.

## How is ZAD different from specifications or tests?

ZAD defines how the developer and assistant move from uncertainty to a justified, authorised change. A specification can capture the answers. Tests can check the behaviour. They can be used together.

## Is ZAD faster or more accurate?

That has not been established by this project. Questions can expose important uncertainty, but can also add delay. The evaluation protocol is designed to test the claimed benefits rather than assume them.

## Is the included demo evidence that ZAD works?

No. It verifies an intentionally defective fixture and its reference correction. It does not compare AI agents or prompting strategies.

## Is ZAD a safety mechanism?

It is a process convention, not an enforced security boundary. Keep access controls, sandboxes, secret handling, tests, and review.

## Who created this proposal?

This formulation is proposed by Marcel Silva. It does not claim exclusive ownership of the name or invention of inquiry-based development. Contributions and relevant prior work are welcome.
