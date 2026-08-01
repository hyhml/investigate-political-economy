---
name: investigate-political-economy
description: "Conduct source-heavy political-economy investigations and turn them into long-form Chinese analytical essays through three mandatory human-reviewed stages: factual research, interpretive argument formation, and hidden-structure writing. Use for policies, firms, finance, commodities, supply chains, imperialism, war economies, state-capital relations, class formation, land conflicts, labor, social movements, or organizational histories, especially when reference prose should shape the voice. Never skip the stage gates or draft the article before explicit user approval."
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
- `references/method-clusters.md`: optional, cross-compatible research methods for institutional networks and collective-subject histories. Read before planning Stage 1 searches.
- `references/evidence-and-publication.md`: inference tracking, scene reconstruction, and the separation between a fully sourced working record and lightly cited publication prose.
- `references/style-profile.md`: calibrated authorial style model. Read before Stage 2 argument design and again before Stage 3 prewriting.
- `references/style-sample-aca-vault-plan.md` and `references/style-sample-mst-history.md`: foundational prose samples. Read both before building the Stage 3 narrative brief unless the user explicitly limits the relevant sample set.

## Stage 1: establish the factual terrain

Research broadly before asking interpretive questions. Resolve discoverable factual questions yourself instead of delegating them to the user.

Build the chronology, actor map, source ledger, relevant money/material/control flows, organizational changes, document status, source conflicts, and unresolved gaps. Identify the material relations that distribute action capacity and the actor or network that changes through the investigation. Search primary materials in their original languages where useful. Distinguish announcements, authorizations, signed agreements, closing, disbursement, construction, production, shipment, and realized results.

Choose methods from `references/method-clusters.md` according to the causal gap and available evidence, not the topic label. Record one provisional primary causal method, any nested supporting method, the necessary cross-cutting lenses, evidence forms, and explicitly excluded methods. Do not activate an entire cluster because a topic resembles one sample. Reassess the selection after the basic chronology and actor map, and again at Stage 1 saturation. When combining clusters, name which method is primary so that policy files, enterprise trails, oral histories, and scenes do not become disconnected collections.

Actively seek disconfirming evidence and meaningful perspectives from resource-producing states, workers, allied states, firms, regulators, movement members, intermediaries, and critics. Investigate differences within states, firms, movements, and alliances; never presume a seamless single will. Use parallel research agents only for bounded independent lines when it materially improves coverage; the main agent must read, reconcile, and record their evidence.

At provisional saturation, provide a Stage 1 discussion brief containing:

- what is established;
- the emerging factual chains;
- anomalies and contradictions;
- what public evidence cannot establish;
- methods retained, added, removed, or excluded, and what each explains;
- several research-generated interpretive forks;
- only the high-value questions that require human judgment.

Enter `stage_1_discussion` and stop. Continue Stage 1 if the user asks for more investigation. Advance only after explicit approval.

## Stage 2: form and test interpretations

Use the user's Stage 1 decisions to conduct targeted research. Develop two to four competing or nested explanations rather than decorating the first intuition. For each, identify its mechanism, supporting evidence, counterevidence, rival explanations, scope limits, and what would falsify it.

Separate direct coordination from policy-induced convergence, ordinary profit seeking, and temporal coincidence. Treat clustered timing, aligned interests, personnel links, policy instruments, and parallel deployments as legitimate clues to strategic convergence. Preserve the capacity for bold structural inference: trace the inference in the working record and test alternatives, but do not weaken a well-supported conclusion merely because the actors have not publicly admitted coordination.

Identify contradictions that generate change: how an attempted solution answers an earlier problem, creates a new problem, and alters the actor's capacities or organization. Identify one governing thesis, supporting propositions, the best cases, necessary counterexamples, and claims that remain bold but defensible.

Update `argument-map.md`, `unresolved-questions.md`, and `user-decisions.md`. Then provide a Stage 2 discussion brief containing:

- the competing explanations and their relative strength;
- the proposed governing thesis;
- the causal mechanism in plain language;
- strongest counterevidence and vulnerabilities;
- proposed case selection and exclusions;
- questions about thesis, political vocabulary, certainty, audience, and argumentative risk.

Enter `stage_2_discussion` and stop. Advance only after the user explicitly approves the thesis and entry into Stage 3.

## Stage 3: build the hidden structure and write

First perform targeted verification for the chosen argument and read the current style profile and both foundational prose samples. Decide what evidence belongs in the article and what should remain backstage. Follow `references/evidence-and-publication.md` for source visibility and any scene reconstruction.

Create `narrative-brief.md` with a hidden movement of thought, not a visible report outline. Present the user with a compact prewriting brief containing the opening tension, governing thesis, main cases, boldest inference, strongest counterweight, intended register, citation treatment, and expected length. Enter `stage_3_prewrite` and stop.

Draft only after explicit approval. During drafting:

- establish a concrete tension and an early interpretive direction, then let the judgment intensify, acquire complications, and become more precise through the investigation;
- use chronology to show causal change rather than to compile an event list;
- let contradictions drive section transitions: show what an arrangement solves, what it newly produces, and how it changes the moving subject;
- use cases to move across scales—concrete action, exposed relation, wider structure, then a new case that tests the interpretation;
- preserve internal unevenness within states, capital, movements, and alliances without turning this into ritual balance;
- embed evidence limits naturally in sentences rather than displaying audit labels;
- use a small number of organic headings and uneven section lengths when the material calls for them;
- narrate firms, organizations, and communities as developing trails of action, not identical case-study templates;
- preserve authorial intervention, transitions, recursions, and widening historical perspective;
- let concepts arise through concrete material and organizational relations instead of pausing for textbook definitions;
- allow forceful political vocabulary when the demonstrated structure calls for it; do not mechanically intensify the diction or neutralize a supported judgment;
- retain counterevidence without dissolving the conclusion into false balance;
- choose a systemic synthesis or an earned symbolic scene for the ending, and use it to reclassify the opening problem rather than summarize sections;
- avoid think-tank symmetry, checklist prose, canned neutrality, forced concept invention, and a conclusion announced in full at the opening.

After drafting, run separate factual and stylistic audits. Correct errors but do not flatten the voice. Deliver the draft with a concise list of genuine revision decisions for the user.

## Distinguish questions

Do not ask the user questions that research can answer.

- Resolve factual questions through investigation.
- Discuss interpretive forks with the user.
- Reserve thesis, political vocabulary, intended audience, speculative risk, and final emphasis for author decisions.

Ask a small number of consequential questions grounded in the completed stage. Do not use a fixed questionnaire merely to simulate collaboration.

## Preserve the research-writing firewall

Keep tables, evidence grades, exhaustive timelines, reconstruction labels, and claim ledgers in the project files. Transform them into natural prose only in Stage 3. The publication draft may omit dense visible citations when the target publication calls for it, but the working record must preserve complete sourcing and inference paths. Do not write directly from search-result order, include facts merely because they were found, or expose the full backstage framework as the article's visible structure.
