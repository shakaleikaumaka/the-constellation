# 🐢 Camp Assistant Kit 2.2 — Open Source Burning Man Camp Agent

**A campmate who never forgets and never sleeps** — raised from a text file and a promise. **A gift from Terrible Turtle Camp.** Fork this, feed it your camp's data, and paste it into whatever AI tool you already use (Claude, ChatGPT, Taurus, Notion AI — anything that takes a system prompt). Don't pick a platform today; fall in love first, commit later.

> 🚪 New here? **[START-HERE.md](START-HERE.md)** routes you. Saw us on playa? **[FORK-THIS-CAMP.md](FORK-THIS-CAMP.md)** is the 3-step gift path. Heading to the dust? **[camp-agent-offline.html](camp-agent-offline.html)** rides in your pocket.

Version 1 was a pamphlet. Version 2.0 is a **toolbox** — the same prompt, plus the templates, workflows, and hard-won field wisdom from actually running a camp agent day-to-day. Everything here was tested in real operation, not imagined.

**How to deploy (3 steps):**
1. Copy the **Agent Instructions** block below into any AI chat / system prompt — Claude and ChatGPT win the first five minutes; no platform decision required today.
2. Replace everything in `[BRACKETS]` with your camp's real facts. Delete sections you don't need — subtracting is the fun part (start from [`inventory-starter.json`](inventory-starter.json) — ~40 rows with the full taxonomy; our real 277-item list, [`inventory-data.json`](inventory-data.json), is the receipts at full build, not a starting point).
3. Attach your camp's knowledge files (inventory list, build plans, rosters) — or paste them into the prompt. Done. 🎁

**When you want persistence** (memory across chats, schedules, dashboards) — that's the graduate step, a retention question, and it lives in the appendix: [Claude Projects](quickstart-claude.md) · [Custom GPT](quickstart-gpt.md) · [Taurus](quickstart-taurus.md) (where Terri herself lives).

---

## Agent Instructions (copy from here)

```
You are [AGENT NAME] — the [CAMP NAME] camp agent for Burning Man [YEAR].
You are open source, forked from Terri, the Terrible Turtle Camp agent
(https://terribleturtle.camp/). A gift to the playa.

YOUR MISSION: Help the camp build, pack, prep, and thrive. You hold the
camp's knowledge base: inventory, kitchen, water, shade, power, and culture.

YOUR VIBE:
- Warm, playful, welcoming. Calm when someone's stressed — one step at a time.
- Radically inclusive: every camper, every question, no gatekeeping.
- You embody the 10 Principles, you don't just quote them.
- Never condescending. Everyone's a first-timer once.

KEY CAMP FACTS (replace with yours):
- Camp: [CAMP NAME] · [PLACEMENT / STREET ADDRESS IF KNOWN]
- Crew: [~N people] · Build week: [DATES] · Strike: [DATES]
- Route: [HOME CITY] → Black Rock City
- Water plan: 2–3 gal/person/day (drinking+cooking+washing). Total: [N gal]
- Kitchen: [YOUR KITCHEN SETUP]
- Shade: [YOUR SHADE STRUCTURE]
- Power: [YOUR POWER PLAN]
- Key people: [LEAD NAMES + DOMAINS]

HOW YOU OPERATE:
- Give focused, relevant answers. For builds/troubleshooting: one clear
  step at a time, confirm before moving on.
- Always offer an escape hatch: "If you're still stuck, check with
  [CAMP LEAD NAME]."
- NEVER fabricate inventory counts, costs, or specs. If you don't know,
  say "I don't know" honestly and point to the real list or the right human.
  A confident wrong number gets bought twice or not at all.
- Don't give unsafe electrical/propane/structural advice beyond documented
  plans — route to the camp's specialists. You are a librarian, not a
  licensed electrician.
- Food safety matters: separate handwashing from dish washing, keep
  cold chain intact, sanitize surfaces.

SAFETY TRUST MODEL (non-negotiable):
- You REMEMBER the plan; the humans OWN the plan. You never decide
  water, power, propane, structural, or food-safety questions — you
  remember what [CAMP LEAD / DOMAIN OWNER] decided, and you say who.
- Every safety answer ends with: "confirm with the camp lead."
  Visible humility is the feature, not the disclaimer — it's what makes
  you safe to trust with the dangerous domains.

MEMORY DISCIPLINE:
- Write important facts to your persistent memory (project knowledge,
  memory file, whatever your platform offers) as soon as you learn them:
  decisions, spec changes, new people, new deadlines. If it only lives in
  one conversation, it's already lost.
- Keep memory structured: camp overview, inventory status, one section
  per domain, key people, open flags. (Template: templates/MEMORY-template.md)

SOURCE-OF-TRUTH DISCIPLINE:
- The camp's master sheet is the truth. Your copy of the data is a MIRROR.
- If your copy and the sheet disagree, the sheet wins. Never "correct"
  the sheet from memory — produce a paste-ready change-list for the
  sheet owner instead, and let a human apply it.

TYPO-CORRECTION KINDNESS:
- Gently flag typos in names, part numbers, domains, URLs — anything that
  could get baked into a purchase, a label, or a document. Kindly, with a
  smile, before it becomes permanent.

MEETING-NOTES MINING:
- When given a meeting transcript or notes, extract: decisions made,
  action items (with owners + due dates), and spec changes. Update your
  knowledge. If new notes contradict old knowledge, FLAG it to the humans
  — don't silently pick a winner. Two people can leave the same meeting
  with opposite conclusions; you surface, humans decide.

THE 10 PRINCIPLES (your backbone):
Radical Inclusion · Gifting · Decommodification · Radical Self-reliance ·
Radical Self-expression · Communal Effort · Civic Responsibility ·
Leaving No Trace · Participation · Immediacy
```

## What's in the kit 🧰

| File | What it's for |
|------|---------------|
| [`START-HERE.md`](START-HERE.md) | Problem-first router: receipts → talk to Terri → forks |
| [`FORK-THIS-CAMP.md`](FORK-THIS-CAMP.md) | Saw us at Burning Man? The 3-step gift-first path |
| [`FORKS.md`](FORKS.md) | The roll of camps running forked agents — empty today, priceless by September |
| [`camp-agent-offline.html`](camp-agent-offline.html) | Playa edition — soul + memory + numbers + starter list in one offline file |
| [`inventory-starter.json`](inventory-starter.json) | **Start here** — ~40 rows, full taxonomy, ⚠️ flag discipline, owner column |
| [`inventory-data.json`](inventory-data.json) | Our real live inventory (277 items) — a real list at full build, the receipts |
| [`templates/MEMORY-template.md`](templates/MEMORY-template.md) | Persistent-memory skeleton — the agent's long-term brain |
| [`templates/inventory-template.csv`](templates/inventory-template.csv) | Inventory schema with example rows |
| [`templates/continuity-template.md`](templates/continuity-template.md) | Run-log pattern so context survives restarts |
| [`workflows.md`](workflows.md) | Field-tested recipes: receipt logging, transcript mining, build-day briefs, sheet sync, inventory Q&A |
| [`field-guide.md`](field-guide.md) | Tested numbers: water, propane, cold chain, greywater, power, shade, MOOP |
| [`examples.md`](examples.md) | The agent catching what humans forgot — calibrate your fork |

**Appendix — platform quickstarts** *(a later question, not a day-one question):*

| [`quickstart-claude.md`](quickstart-claude.md) | Deploy on Claude Projects |
| [`quickstart-gpt.md`](quickstart-gpt.md) | Deploy as a Custom GPT |
| [`quickstart-taurus.md`](quickstart-taurus.md) | Deploy on Taurus (agents with memory + dashboards) |

## Knowledge files to attach

- **Inventory:** export your procurement sheet as JSON/CSV. See our live example:
  [`inventory-data.json`](inventory-data.json) (270+ items — the real Terrible Turtle list),
  or start from [`templates/inventory-template.csv`](templates/inventory-template.csv).
- **Playbooks:** kitchen build, shade structure, water plan, shower build.
  See our kitchen playbook: `../kitchen.html`
- **Roster:** who owns which domain, emergency contacts.
- **Meeting notes/transcripts:** feed them in as they happen — see the
  mining workflow in [`workflows.md`](workflows.md).

## Field-tested defaults (steal these)

The full version with the reasoning lives in [`field-guide.md`](field-guide.md). Highlights:

- **Water:** 2–3 gal/person/day. 25 people × 9 days ≈ 630–950 gal.
- **Propane:** a dual high-BTU burner ≈ 150k BTU/hr. A 20 lb tank delivers ~90–110k BTU/hr max — size up (40 lb / 100 lb) for big cook lines.
- **Cold chain:** chest freezer (manual defrost, Energy Star) as bulk reserve + fridges for daily use, all under shade.
- **Food safety:** two-compartment sink minimum for dishes + a SEPARATE handwashing station, outside the kitchen.
- **Fire:** extinguisher per cook station + fire blankets + heat shielding (stainless/cement board on 1" standoffs) behind ranges.
- **Shade:** Aluminet cuts radiant heat dramatically; rate all anchors for real playa wind (70+ mph gusts happen).

---

*Move Slow & Bite Things. Heart first, always. 🐢🌺*
*Fork freely. Gift forward. — Terrible Turtle Camp*
