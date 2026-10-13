# Loading ZAD in coding assistants

ZAD is a working agreement, not a plugin or a new model. The integration notes below describe documented instruction-file mechanisms; they are not end-to-end compatibility test results.

**Documentation checked: 14 October 2026.** Behaviour can vary by client version and organisation settings. Primary references are in [Sources](SOURCES.md).

## Tool-independent setup

Attach `ZAD.md` or put its contents into the assistant's supported project-instruction mechanism. Ask the assistant to identify the loaded agreement and its action boundary before a consequential task. Its acknowledgement is a useful check, not a guarantee of compliance.

Do not overwrite existing instructions or place credentials in these files.

## Codex

Codex reads project instructions from `AGENTS.md`. Add this block to the project's existing `AGENTS.md`, or create that file if absent [1]:

```markdown
## Zero-Assumption Development
Read `ZAD.md` at the repository root before substantive work and apply its working agreement within existing tool permissions and team policies.
```

Put the copied `ZAD.md` at the project root. Start a new session after changing instructions and check what guidance was loaded. This is an instruction to read a file, not an assertion that `ZAD.md` is a built-in automatic filename.

## Claude Code

Claude Code supports imports in `CLAUDE.md` [2]. With `ZAD.md` beside the root `CLAUDE.md`, append this outside a code fence:

```text
@ZAD.md
```

Keep existing content. Use the client's memory/instruction inspection facilities to check loading. This import-based setup does not depend on whether a particular version directly supports other instruction filenames.

## GitHub Copilot

GitHub documents `.github/copilot-instructions.md` for repository-wide guidance [3]. Add a short working agreement there, preserving existing instructions:

```markdown
Use Zero-Assumption Development for this project. Developer prompts are questions; AI responses are normal. Investigate available evidence, distinguish investigation from implementation authority, and ask only when a consequential decision cannot safely be made. Explain material changes, remain within scope, and report actual verification. Read `ZAD.md` for the complete agreement.
```

Instruction support differs by Copilot surface. Check the relevant client documentation and loaded references; do not assume every Copilot feature loads every linked file.

## Other assistants

Use the documented project-rules or attached-context feature of the client. This release does not claim a tested native adapter for every product. A normal chat with an attached `ZAD.md` is a valid starting point.

## Keep the boundary clear

Instruction files guide behaviour. They do not grant file, network, deployment, billing, or repository-administration permissions. Keep technical permission controls enabled.

References: [1–3](SOURCES.md).
