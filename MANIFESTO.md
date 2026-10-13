# The Zero-Assumption Development Manifesto

**ZAD 1.0.0 — Inquiry. Evidence. Controlled execution.**

Proposed by Marcel Silva.

## The premise

Start every task assuming you and the AI do not understand it yet.

You may recognise the problem. Your first solution may even be right. ZAD asks you to check what is happening in this system before asking the AI to commit to that solution.

"Zero-assumption" does not mean forgetting what you know. It means not treating unchecked assumptions as facts. Existing requirements, prior decisions, and observed behaviour are context to use, not knowledge to discard. Where uncertainty remains, make it explicit and deal with it in proportion to the consequences.

We begin with questions about the problem, the existing system, the available evidence, and the consequences of a change.

**Every developer prompt is a question.** The AI is not required to answer with questions. It should answer, investigate, recommend, implement when authorised, and verify its work.

The discipline is not punctuation. A question that merely disguises an unexamined command does not deliver the substance of ZAD.

## Our commitments

### 1. Understand the problem before defending a solution

We ask what is failing, who is affected, what success means, and whether the proposed change addresses the actual problem. Existing requirements and user decisions should be used, not repeatedly requested.

### 2. Investigate before assuming

We inspect relevant code, tests, documentation, and available observations. We identify what is known, what is inferred, and what remains unresolved. We do not invent repository findings or imply access to systems we have not inspected.

### 3. Use evidence to justify consequential decisions

Before a material architectural or behavioural change, the AI gives a concise, reviewable rationale: the relevant evidence, the meaningful trade-off, and the proposed scope. This means a useful decision explanation, not a demand for private internal chain-of-thought.

### 4. Preserve autonomy where it is safe and authorised

ZAD is not an approval ceremony for every variable name or reversible implementation detail. Within a clearly authorised task, the AI should make reasonable local decisions and keep moving.

Confidence is not permission. An investigation question does not silently become authority to edit, deploy, spend money, delete data, or publish information.

### 5. Ask when an important decision cannot safely be made

The AI first checks the available context. It asks a targeted question only when an unresolved choice would materially affect correctness, security, privacy, cost, compatibility, or irreversible outcomes.

A useful clarification explains the decision, the consequence, and the available choices. It does not ask the developer to do research the AI can perform itself.

### 6. Validate outcomes, not just plausible explanations

We define observable acceptance criteria. We run appropriate checks when possible and say precisely what was and was not verified. Passing a test suite is evidence about the tested behaviour, not proof that all behaviour is correct.

### 7. Keep the process proportional to the task

The cycle is Discovery, Investigation, Design, Implementation, and Validation. The depth of each stage should match the risk and complexity. A small bug fix does not need a large specification or a long conversation.

### 8. Improve the method through honest experience

ZAD is a proposal to test, not a claim of automatic superiority. We welcome comparisons, negative results, simpler alternatives, and evidence that the overhead is not justified.

## The default working agreement

The developer always communicates task requests through questions ending in `?`. Context supplied with a question — code, logs, examples, constraints, and supporting documents — remains ordinary data and need not be rewritten as questions.

The AI responds normally. It investigates before consequential changes, presents a concise rationale, and acts when the question clearly authorises the action. It asks its own questions when an important decision cannot safely be made from available information.

The question-only convention applies to developer prompts, not to source code, AI responses, documentation, tool output, or issue metadata. A prompt that is not a question should be reframed for a ZAD session; a question mark alone does not fulfil the commitments to inquiry, evidence, and controlled execution.

## The limitations

Questions can be vague, leading, or functionally identical to commands. The AI may answer without implementing, ask too many questions, overlook evidence, or make incorrect inferences. Extra interactions can add cost and delay.

ZAD cannot itself enforce permissions or make an unsafe environment safe. Technical controls and accountable human review remain necessary.

## The principle

**Question first. Investigate before assuming. Explain consequential decisions. Execute within authority. Validate with evidence.**
