# ZAD repository instructions

Follow the Zero-Assumption Development agreement in `ZAD.md` when working in this repository. Investigate available evidence before consequential changes. Respond normally; do not force AI responses into question form.

Start by checking what is known about this task and which assumptions still need evidence. "Zero-assumption" means not treating unchecked assumptions as facts, not ignoring existing requirements or demanding certainty about every detail.

Developer task prompts are questions. Distinguish investigation from implementation authority. Ask only when a consequential decision cannot safely be made from available context. Make routine authorised decisions without unnecessary clarification.

Explain the evidence and scope for material changes, keep changes focused, and report actual verification and limitations. Never invent results or treat the demo as evidence that ZAD outperforms another method.

Repository checks: `python scripts/ValidateZADV2.py --allow-pending-readmes` and `python scripts/RunDemoV2.py`. The intentionally defective pagination starter must continue to fail the demo's behavioural tests.
