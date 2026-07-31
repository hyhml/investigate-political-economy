---
name: investigate-political-economy
description: "Conduct source-heavy political-economy investigations and turn them into long-form Chinese analytical essays through three mandatory human-reviewed stages: factual research, interpretive argument formation, and hidden-structure writing. Use when investigating policies, firms, finance, commodities, supply chains, imperialism, war economies, state-capital relations, or similar topics for an evidence-grounded article, especially when reference prose should shape the voice. Never skip the stage gates or draft the article before explicit user approval."
---

# Investigate Political Economy

Build a political-economy essay with the user instead of generating one in a single pass. Keep the research framework rigorous backstage and the finished prose natural, argumentative, and visibly authored.

## Enforce the workflow

Treat the project as a state machine. Never collapse stages, silently approve a gate, or interpret silence as permission.

1. Complete Stage 1 research and discussion. Stop until the user explicitly approves entering Stage 2.
2. Complete Stage 2 interpretation and discussion. Stop until the user explicitly approves entering Stage 3.
3. In Stage 3, present a short narrative brief before drafting. Stop until the user explicitly approves drafting.

Allow the user to request more research or return to an earlier stage at any time. If new evidence discovered during writing materially changes the argument, return to Stage 2 and discuss it rather than silently rewriting the thesis.

Do not draft article prose during Stages 1 or 2. Short examples used to clarify a distinction are allowed, but do not produce a disguised draft.

## Start or resume a project

Create a separate project directory in the user's current workspace unless the user specifies another writable location. Use `scripts/init_project.py` to create the working files. Read `project-state.md` before every substantive turn and update it with `scripts/set_stage.py` only after the required action or explicit approval.

Keep full working material in project files and give the user a readable discussion brief in chat. Record user decisions faithfully; do not later neutralize or overwrite an agreed political judgment without explaining the new evidence.

Read these references when relevant:

- `references/workflow.md`: stage deliverables, gate rules, project files, and discussion protocol.
- `references/research-method.md`: source hierarchy, evidence and interpretation ledgers, saturation, causal discipline, and counterevidence.
- `references/style-profile.md`: current authorial style model.
- `references/style-sample-aca-vault-plan.md`: current primary prose sample. Read it before building the Stage 3 narrative brief; update the profile when the user supplies more samples.

## Stage 1: establish the factual terrain

Research broadly before asking interpretive questions. Resolve discoverable factual questions yourself instead of delegating them to the user.

Build the chronology, actor map, source ledger, money/material/control flows, corporate actions, document status, source conflicts, and unresolved gaps. Search primary materials in their original languages where useful. Distinguish announcements, authorizations, signed agreements, closing, disbursement, construction, production, shipment, and realized results.

Actively seek disconfirming evidence and meaningful perspectives from resource-producing states, workers, allied states, firms, regulators, and critics. Use parallel research agents only for bounded independent lines when it materially improves coverage; the main agent must read, reconcile, and record their evidence.

At provisional saturation, provide a Stage 1 discussion brief containing:

- what is established;
- the emerging factual chains;
- anomalies and contradictions;
- what public evidence cannot establish;
- several research-generated interpretive forks;
- only the high-value questions that require human judgment.

Enter `stage_1_discussion` and stop. Continue Stage 1 if the user asks for more investigation. Advance only after explicit approval.

## Stage 2: form and test interpretations

Use the user's Stage 1 decisions to conduct targeted research. Develop two to four competing or nested explanations rather than decorating the first intuition. For each, identify its mechanism, supporting evidence, counterevidence, rival explanations, scope limits, and what would falsify it.

Separate direct coordination from policy-induced convergence, ordinary profit seeking, and temporal coincidence. Identify one governing thesis, supporting propositions, the best cases, necessary counterexamples, and claims that remain bold but defensible.

Update `argument-map.md`, `unresolved-questions.md`, and `user-decisions.md`. Then provide a Stage 2 discussion brief containing:

- the competing explanations and their relative strength;
- the proposed governing thesis;
- the causal mechanism in plain language;
- strongest counterevidence and vulnerabilities;
- proposed case selection and exclusions;
- questions about thesis, political vocabulary, certainty, audience, and argumentative risk.

Enter `stage_2_discussion` and stop. Advance only after the user explicitly approves the thesis and entry into Stage 3.

## Stage 3: build the hidden structure and write

First perform targeted verification for the chosen argument and read the current style profile and prose samples. Decide what evidence belongs in the article and what should remain backstage.

Create `narrative-brief.md` with a hidden movement of thought, not a visible report outline. Present the user with a compact prewriting brief containing the opening tension, governing thesis, main cases, boldest inference, strongest counterweight, intended register, citation treatment, and expected length. Enter `stage_3_prewrite` and stop.

Draft only after explicit approval. During drafting:

- let political judgment emerge and intensify through the investigation;
- embed evidence limits naturally in sentences rather than displaying audit labels;
- use a small number of organic headings and uneven section lengths when the material calls for them;
- narrate companies as developing trails of action, not identical case-study templates;
- preserve authorial intervention, transitions, recursions, and widening historical perspective;
- support terms such as imperialism, extraction, war preparation, or unequal exchange with concrete mechanisms;
- retain counterevidence without dissolving the conclusion into false balance;
- avoid think-tank symmetry, checklist prose, canned neutrality, and a conclusion announced in full at the opening.

After drafting, run separate factual and stylistic audits. Correct errors but do not flatten the voice. Deliver the draft with a concise list of genuine revision decisions for the user.

## Distinguish questions

Do not ask the user questions that research can answer.

- Resolve factual questions through investigation.
- Discuss interpretive forks with the user.
- Reserve thesis, political vocabulary, intended audience, speculative risk, and final emphasis for author decisions.

Ask a small number of consequential questions grounded in the completed stage. Do not use a fixed questionnaire merely to simulate collaboration.

## Preserve the research-writing firewall

Keep tables, evidence grades, exhaustive timelines, and claim ledgers in the project files. Transform them into natural prose only in Stage 3. Do not write directly from search-result order, include facts merely because they were found, or expose the full backstage framework as the article's visible structure.
