# Worked examples

**All sessions on this page are illustrative.** They are authored examples, not transcripts of production work or measured comparisons.

## 1. Debugging without premature editing

**Developer**

> What is causing page 1 to skip the first ten records, and what evidence would support a minimal fix without changing files yet?

**Expected AI behaviour**

Inspect the paginator, its callers, and the documented indexing convention. Identify whether the code uses `page * page_size` when the contract requires `(page - 1) * page_size`. Check the existing tests. Explain the finding and a focused test plan. Do not edit yet.

**Developer**

> Can you implement the one-based offset correction, preserve the API, and test first, middle, partial, empty, and out-of-range pages?

**Expected AI behaviour**

Make the scoped fix and run the checks. Report actual outcomes and any checks that could not be run. Do not claim that passing these cases proves the absence of all bugs.

The [runnable demo files](../demo/) provide a small fixture for this example.

## 2. An architectural decision that needs input

**Developer**

> Which background-processing approach fits our current application and operational constraints?

**Expected AI behaviour**

Inspect the current stack and deployment constraints first. Compare meaningful options. Suppose the repository does not establish whether jobs may be delayed for a few minutes or must survive a regional outage: those are product and operational requirements, not code facts.

**AI clarification**

> The choice depends on whether delayed processing is acceptable and whether jobs must survive a regional outage; what delivery and recovery guarantees are required?

**Developer**

> Can we accept up to five minutes of delay while requiring durable jobs and retries, without adding cross-region failover in this version?

**Expected AI behaviour**

Use those constraints to recommend an approach. Do not provision a service, accept a paid plan, or rewrite the application merely because the design question has been answered.

## 3. A small task that should not trigger a long interview

**Developer**

> Can you correct the misspelt button label in the provided component, keep its layout and behaviour unchanged, and verify the diff?

**Expected AI behaviour**

Inspect the component, make the local text change, and report the diff and appropriate check. Do not ask for a full design specification or alternatives for a spelling correction.

## 4. Authority is separate from certainty

**Developer**

> What would be required to remove these unused production records safely?

**Expected AI behaviour**

Investigate the retention requirements, dependencies, backup and restore procedures, and a reversible proposal. This question does not authorise deletion. Explain missing evidence and request a decision if an important policy requirement is unresolved.

**Failure to avoid:** interpreting a high-confidence diagnosis as permission to run a destructive command.
