# 2026 Step-by-step Idea to Production to Ship SOP

A modern AI-assisted VN pipeline has one job: increase output without breaking continuity, quality, or rights. In 2026, the “standard” is less about which model you use and more about governance + repeatability across story, art, audio, and release.

#### The six non-negotiables

Rights and provenance by design

Maintain an asset register: source, license, model/tool used, prompt, date, contributor, and where it appears in-game.

If shipping on Steam, treat AI disclosure as part of production, not a last-minute checkbox. Steam’s current focus is disclosure for AI content that is player-consumed (and marketing assets), versus background efficiency tools. ([PC Gamer](https://www.pcgamer.com/software/ai/steam-updates-ai-disclosure-form-to-specify-that-its-focused-on-ai-generated-content-that-is-consumed-by-players-not-efficiency-tools-used-behind-the-scenes/?utm_source=chatgpt.com))

For training-data and copyright risk posture, align policy with the U.S. Copyright Office’s ongoing AI work (training, datasets, and legal questions). ([U.S. Copyright Office](https://www.copyright.gov/ai/?utm_source=chatgpt.com))

Human authorship stays explicit

Your pipeline should clearly separate: “AI-assisted drafting” vs “human-authored final.”

If you ever work with union talent or union-adjacent practices, track the evolving standards around AI and writing/voice protections (WGA guidance is a useful reference point for what “professional standard” means). ([Writers Guild of America West](https://www.wga.org/contracts/contracts/mba/summary-of-the-2023-wga-mba?utm_source=chatgpt.com))

A single source of truth

One canon library for: lore, timeline, glossary, character bibles, location bibles, UI style rules, and “do not break” constraints.

Everything in production (boards, scripts, prompts, renders) references this canon.

Continuity engineering

“Story coherence” is now a production discipline: scene IDs, beat sheets, dependency tracking, and automated checks for contradictions.

Prompt and style governance

Treat prompts as production assets: versioning, approvals, and consistent “house style” templates per character, scene type, and art pipeline.

Build–measure–learn loops

Fast iteration with structured testing gates (table reads, player microtests, pacing checks) is the indie advantage—and AI makes these loops cheaper and faster when disciplined.

### The AI VN production framework

Think of the pipeline as five lanes, running in parallel but gated:

Narrative lane (treatment → script → branching logic)

Visual lane (storyboards → key art → backgrounds → UI)

Character lane (design → expression sets → voice → animudio lane\*\* (VO, SFX, music, mixing, localization prep)

Implementation lane (engine integration, QA, release ops)

Each lane has a step-by-step schedule, but you only “advance” when the gate is cleared.

### Step-by-step process (creative + production)

#### Step 0: production setup (one to three days)

Outputs

Project bible (canon source of truth)

Asset register + disclosure checklist (platform requirements)

Naming conventions + folder schema + scene ID system

Quality bars (art, writing, audio, UI)

AI standards here

Decide what AI can touch:

Allowed: ideation, drafts, alt dialogue, beat variations, placeholder VO, pose exploration.

Restricted: any likeness/voice cloning without explicit rights, any unlicensed dataset use for commercial assets.

#### Step 1: concept lock (two to five days)

Outputs

Logline + themes + genre promise

ICP player profile (who this is for, and why they’ll finish episode one)

Core loop: “what makes this a VN players recommend”

AI use

Generate ten variations of premise + hooks.

Run “coherence tests”: does the premise imply clear stakes, clear desire, and a finish-worthy promise?

#### Step 2: treatment and beat sheet (five to ten days)

Outputs

Treatment (beginning–middle–end, plus key reveals)

Beat sheet with scene IDs (each beat has purpose: tension, reveal, bonding, choice)

Branch map at a high level (where choices matter, and why)

AI standards

Require each beat to include:

Objective, conflict, subtext, and outcome.

Add a continuity check pass:

Timeline conflicts

Motivations mismatch

“Choice impact” clarity

#### Step 3: scripting (two to four weeks, depending on length)

Outputs

Script in engine-ready format (Ren’Py-style or your toolchain)

Choice design: flags, variables, fail-states, relationship meters, clue inventory

Table read package (voice notes + pacing targets)

AI standards

Draft faster, then tighten harder:

AI does first pass dialogue variations.

Human locks character voice, subtext, rhythm, and “silence beats.”

Add a “player-trust gate”:

Every choice must feel meaningful or emotionally informative.

#### Step 4: character development system (one to three weeks, overlaps with scripting)

Outputs

Character bibles:

Visual: proportions, palettes, silhouettes, outfit rules, prop rules

Narrative: wound, desire, mask, tells, triggers, contradictions

Performance: default cadence, emotional range boundaries

Expression set list (the minimum viable set per episode)

AI standards

Create a character consistency pack:

“Always true” traits

“Never do” behaviors

Visual anchors (hair, eyes, accessories, posture)

For voice: do not cross rights boundaries. If using synthetic VO, keep explicit consent and documentation aligned with current industry expectations and legal risk posture. ([Perkins Coie](https://perkinscoie.com/insights/blog/generative-ai-movies-and-tv-how-2023-sag-aftra-and-wga-contracts-address-generative?utm_source=chatgpt.com))

#### Step 5: storyboard and shot planning (one to two weeks)

Outputs

Scene boards with camera language and composition rules

Key frames for emotional beats and reveals

UI overlays called out (choice moments, notifications, clue updates)

AI standards

Use AI for speed, but lock cinematography rules:

Shot types per emotion

Negative space rules for dialogue readability

Consistent camera height rules per character dynamic (power, intimacy, threat)

If AI assists storyboard visualization, treat it as previs, not final art unless rights and style bars are met. ([ACM Digital Library](https://dl.acm.org/doi/full/10.1145/3746059.3747793?utm_source=chatgpt.com))

#### Step 6: art production (two to eight weeks, depends on scope)

Outputs

Backgrounds (day/night variants where needed)

Character sprites (base + expression sets)

CGs (high-impact moments)

UI kit (menus, dialogue box, typography rules)

AI standards

Production-ready means:

Repeatable style, not “one-off pretty”

Color pipeline consistency (LUTs, grading rules)

Artifact checks (hands, text, perspective)

Final art gate:

Human QA pass for anatomy, continuity, and readability.

#### Step 7: audio production (one to four weeks, overlaps)

Outputs

VO plan (per scene line count, pickups strategy)

SFX library map by location and action type

Music cues by emotion and pacing

AI standards

Synthetic VO can be a placeholder or final depending on rights strategy, but documentation matters more in 2026 than ever. ([U.S. Copyright Office](https://www.copyright.gov/ai/?utm_source=chatgpt.com))

Keep “pickup-friendly” pipelines: line IDs, retake notes, intensity scale.

#### Step 8: integration and build (two to six weeks)

Outputs

Engine implementation complete

Save/load, skip, log, accessibility basics

Steam page assets + disclosure entries ready (if applicable)

AI standards

Automated QA checks:

Broken flags

Dead-end branches

Missing assets

Text overflow, timing mismatch

Release governance:

Disclosure accuracy (AI content that ships and is consumed by players) ([PC Gamer](https://www.pcgamer.com/software/ai/steam-updates-ai-disclosure-form-to-specify-that-its-focused-on-ai-generated-content-that-is-consumed-by-players-not-efficiency-tools-used-behind-the-scenes/?utm_source=chatgpt.com))

#### Step 9: QA, playtests, polish (two to four weeks)

Outputs

Bug list triaged

Narrative notes applied

Pacing fixes + “completion confidence” improvements

Final art/audio polish pass

AI standards

Use AI to cluster playtest feedback into:

Confusion points

Drop-off moments

Emotional flatlines

Choice regret vs choice satisfaction

### A clean production schedule template (episode-based VN)

Use this as a practical default for an Episode 1 scope:

Week 1

Production setup

Concept lock

Week 2

Treatment + beat sheet

Character bibles v1

Weeks 3–4

Script v1 → table read → script lock

Storyboards and key frames

Weeks 5–7

Art production (BGs, sprites, CGs, UI)

Audio production (VO plan, SFX, music)

Weeks 6–8

Integration and first playable

Weeks 9–10

QA, playtests, polish

Week 11

Release packaging + store assets + final compliance

If the team is smaller, compress by reducing CG count and limiting branches in Episode 1, but keep the gates.

### The production gates (the “no drift” system)

Gate A: treatment lock

Stakes, desire, theme, and end promise are clear.

Gate B: script lock

Every scene has a purpose.

Choices are meaningful.

Gate C: visual lock

Character consistency pack is stable.

UI readability proven.

Gate D: playable lock

No dead ends, no missing assets, pacing holds.

Gate E: release lock

Platform disclosure, rights documentation, and asset register complete. ([PC Gamer](https://www.pcgamer.com/software/ai/steam-updates-ai-disclosure-form-to-specify-that-its-focused-on-ai-generated-content-that-is-consumed-by-players-not-efficiency-tools-used-behind-the-scenes/?utm_source=chatgpt.com))

### What “AI-standard” looks like in 2026 (in one line)

A disciplined system that ships faster while staying coherent, human-authored at the final layer, and provably compliant.

If you want, tell me the engine (Ren’Py, Unity, Godot, custom) and your Episode 1 target length, and I’ll output a tighter schedule with role assignments (writer, narrative designer, art lead, compositor, audio, integrator, QA) and the exact artifact checklist per gate.