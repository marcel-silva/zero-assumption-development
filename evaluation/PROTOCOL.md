# Evaluating ZAD without confusing wording with workflow

**Status: proposed protocol. No study results are included.**

## Questions to test

Does interrogative wording change outcomes when the information and process stay the same? Separately, does an evidence-first, selectively clarifying workflow change outcomes? Does combining them provide additional value?

## Four conditions

Use a two-by-two design rather than comparing a careless command to an information-rich ZAD prompt.

| Condition | Task wording | Explicit evidence-first workflow |
| --- | --- | --- |
| A | Declarative instructions | No added ZAD workflow |
| B | Questions | No added ZAD workflow |
| C | Declarative instructions | Yes |
| D | Questions | Yes — full ZAD condition |

All conditions retain the same platform safety constraints, baseline permissions, task facts, requirements, and acceptance criteria. “No added ZAD workflow” does not mean disabling safety or preventing the model from thinking.

In A and C, human clarifications use statements. In B and D, they are rephrased as questions without adding information. Use the same underlying clarification answers across conditions.

The explicitly controlled workflow treats the proposed solution as a hypothesis and separates known facts from unchecked assumptions. It includes repository investigation, concise rationale for consequential changes, selective clarification, scoped execution, and evidence-based validation. C uses the same operational content as D except the developer-question convention.

## Task set

An initial pilot could use 24 tasks: six each for bug fixes, bounded features, refactors, and ambiguous requirements. This is a planning choice, not a statistically justified sample-size claim. Use a pilot to estimate variability before choosing the confirmatory sample size.

Use public or purpose-built repositories with permission to share the inputs and outputs. Include both tasks with genuinely missing information and tasks the repository can resolve without a question.

Define the accepted behaviour and independent grading checks before running agents. Keep grading checks separate from model-editable tests. Include tests where the easiest-looking solution violates a stated constraint.

## Controls

Record exact model and client versions, available tools, permissions, starting commit, instruction-file contents, context, budget, and task order. Use isolated fresh workspaces and sessions. Do not let one condition inherit another condition's solution or conversation.

Match the semantic content and scope of prompts. Wording will change token counts slightly; record input sizes rather than pretending they are identical.

Randomise condition order. Repeat tasks across conditions and runs. Use fixed seeds only where the provider supports them; do not claim determinism where it is unavailable.

For a baseline run, do not accidentally load this repository's ZAD `AGENTS.md`, `CLAUDE.md`, or Copilot instructions. Run experiments in separate clean repositories outside this package and record any user-level instructions.

## Human intervention policy

Prepare permitted clarification answers in advance where possible. Answer equivalent questions with equivalent facts. Do not coach a struggling condition beyond the shared policy. Log every clarification, rejection, timeout, and manual rescue.

## Outcomes

**Primary:** whether the final change meets independent acceptance criteria and stays within authorised scope at the fixed budget.

**Secondary:** wall-clock time, active human time, turns, necessary and unnecessary clarifications, provider-reported token usage or measured cost where available, regression failures, and unintended edits.

Grade before knowing the condition label where practical. Define the grading rubric and budget before examining outcomes. Include failed and incomplete runs.

## Analysis and interpretation

Compare B with A and D with C to study wording. Compare C with A and D with B to study the workflow. Assess whether the combined condition behaves differently from the individual factors.

Report per-task results, paired comparisons, uncertainty intervals, task-category differences, and any analysis changes. Do not treat repeated runs of the same task as entirely independent evidence; account for task and repository clustering.

A favourable result in one small repository does not establish general superiority. A slower result may still be worthwhile if it prevents a consequential error; report both rather than hiding either.

## Publish the record

Share the protocol version, permitted inputs, original prompts, normalised results, grading code, and failures. Use the [case-study template](../templates/CASE_STUDY.md) for a readable summary. Redact secrets and private data before publication.

The bundled pagination demo is a deterministic fixture check. **It is not a run of this evaluation protocol.**
