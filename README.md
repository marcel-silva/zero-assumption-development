# ZAD — Zero-Assumption Development

**Because your first idea might be the wrong one.**

An AI-assisted development methodology focused on inquiry, evidence, and controlled execution.

Proposed by Marcel Silva (@marcel-silva). Methodology version 1.0.0.

## The idea

Question first. Then build with evidence.

ZAD wants you to ask before you commit to a solution.

Start every task assuming you (and the AI) don’t understand it yet.

Because when you ask your coding assistant:

> "Add caching to this endpoint."

You’ve already decided what the problem needs. The AI is now working on your answer, not investigating your problem.

Instead, try asking:

> Why is this endpoint slow, and what evidence would tell us whether caching is the right fix?

This way, caching is still an option. You just haven’t asked AI to commit to it before looking.

That is the habit behind Zero-Assumption Development. Start with what you need to understand, rather than what you want the AI to implement.

Ask about the problem, establish what supports your answer, and make changes within the agreed scope.

You don't have to investigate everything. Focus on the questions whose answers could change the solution.

## Install ZAD

Install the skill from this repository with the [Skills CLI](https://skills.sh/docs/cli):

```sh
npx skills add marcel-silva/zero-assumption-development --skill zad
```

Run it from your project folder and select your coding assistant when prompted. Add `--global` to install at user scope instead.

The [installable skill](skills/zad/SKILL.md) contains the same working agreement as `ZAD.md`, with a bundled [MIT licence](skills/zad/LICENSE). It does not need the rest of this repository.

After installation, ask your assistant:

> Can you use ZAD to investigate this task before choosing a solution, and ask me only about important decisions the available evidence cannot resolve?

Skills are loaded when activated; installation alone does not make ZAD an always-on rule. For every-task use, keep the project instructions described in the [integration guide](docs/TOOL_INTEGRATIONS.md).

## Try it on one task

1. Copy [ZAD.md](ZAD.md) into your project, preserving existing instructions.
2. Attach it to your coding assistant or load it using the [integration guide](docs/TOOL_INTEGRATIONS.md).
3. Ask a bounded question with context, constraints, and a clear action boundary.

Example:

**First, an investigation question only:**

> What is causing this pagination bug, which evidence supports the diagnosis, and what is the smallest fix you would recommend without changing files yet?

**Then, with the evidence in hand, an implementation question to authorise:**

> Can you implement the selected pagination fix, preserve the public API, add regression tests, and report what you actually verified?

The first question requests an answer. The second authorises a scoped implementation. Neither authorises a production deployment.

**ZAD calls this inquiry, evidence, and controlled execution.**

See [Getting started](docs/GETTING_STARTED.md) for a complete session.

## Three pillars

| Pillar | What it means in practice |
| --- | --- |
| Inquiry | Understand the problem and challenge material assumptions before committing to a solution. |
| Evidence | Ground decisions in code, requirements, documentation, tests, or measurements. Distinguish findings from assumptions. |
| Controlled execution | Make scoped, authorised changes. Explain consequential decisions. Validate and report limitations. |

## The working cycle

Discovery → Investigation → Design → Implementation → Validation

These are checkpoints, not five mandatory meetings or five separate prompts. A small, clear fix can pass through the cycle in one interaction. A consequential design decision may need several.

## In this repository

| Resource | What it is for |
| --- | --- |
| [Working agreement](ZAD.md) | The reusable instructions for your coding assistant. |
| [Manifesto](MANIFESTO.md) | The principles behind the workflow. |
| [Prompt library](examples/PROMPT_LIBRARY.md) | Examples for investigation, design, implementation, and review. |
| [Worked examples](examples/WORKED_EXAMPLES.md) | Illustrative sessions, including when the AI should ask for input. |
| [Demo files](demo/) | A small pagination defect, reference correction, and shared tests. |
| [Task template](templates/TASK.md) | A place to record the problem, assumptions, scope, and acceptance criteria. |
| [Evaluation protocol](evaluation/PROTOCOL.md) | A plan for comparing question wording and the wider workflow separately. |
| [Experience report](templates/CASE_STUDY.md) | A way to report what helped, failed, or added unnecessary work. |
| [Contribution guide](CONTRIBUTING.md) | How to propose improvements. |
| [Launch plan](docs/LAUNCH_PLAN.md) | A proposed sequence for trying the method with other developers. |

## What has been tested?

The repository includes checks for its files and a runnable code demonstration. Those checks do not establish that ZAD makes an AI more accurate or development faster. No controlled comparative study is included.

Questions can still be vague or leading. The AI can still be wrong. Tests, review, and permission controls still matter. ZAD can be used alongside specifications, test-first development, and your existing engineering practices.

## Contribute

Try ZAD on one task and tell us what happened. Did a question change the solution? Did the AI find something you had overlooked? Did it ask too much and slow you down?

Use the experience-report issue template or the [case-study template](templates/CASE_STUDY.md). Reports where the approach added no value are useful too.

Proposed by Marcel Silva (@marcel-silva). Methodology version 1.0.0. This repository defines a proposed workflow; it does not claim to have invented inquiry-based development.

## Licence

[MIT](LICENSE). The licence covers this toolkit. It does not change the licence of a project where you use it.
