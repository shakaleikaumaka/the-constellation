# Running a camp? Steal this. 🐢

You know the spreadsheet with 270 rows and eleven tabs that only one person
understands? The group chat where *"did anyone buy the propane fittings?"*
gets asked four times and answered zero? The build weekend where three
people drive to three different hardware stores for the same box of screws?

Yeah. Us too.

So we built a campmate who never forgets and never sleeps — an AI agent
that holds our whole camp: inventory, kitchen, water, shade, power, the
plan, and the culture. It answered *"what's blocking the shower build?"* at
2am, turned crumpled receipts into clean inventory rows, and gently
reminded us which purchases were still unbought while the sale was still
on.

This kit is everything we use, given away. No company, no signup, no
paywall — take the prompt, the templates, and the field-tested numbers,
fork them, and raise an agent that knows *your* camp. It's how Burning Man
camps have always worked: somebody builds the thing, everybody gets to use
it.

**CC0 — public domain. Steal it loud.** 🐢

---

## 🤔 What is this thing, exactly?

Think of it as a campmate with a perfect memory and no need for sleep. It
doesn't build your shade structure or drive your truck — it *remembers*.
Every receipt, every *"David said the fittings arrive Tuesday,"* every
water-math calculation, every decision made in a meeting six weeks ago that
nobody wrote down. Ask it *"what do we still need for the kitchen?"* and it
answers from your camp's actual list, not generic advice. It never gets
tired of the same question, never judges a first-timer, and never loses the
note. Your humans still make every call — it just makes sure nothing falls
through the playa dust. 🐢

---

## 🚪 Three doors — pick yours

### 🐢 Door 1: "Saw you at Burning Man!"
You're pre-sold — we handed you a sticker, a meal, or a moment, and you
want this for *your* camp. Beautiful. Three steps, gift-first:
**→ [FORK THIS CAMP](FORK-THIS-CAMP.md)**

### 🏕️ Door 2: "I'm running a camp and drowning."
Shower plan, kitchen chaos, who owns the propane — you arrived with a
problem-shaped hole, not curiosity about AI. Perfect. Skip the philosophy:
**→ [The full kit (run.md)](run.md)** — paste one prompt, feed it your
list, done. Or keep scrolling for the receipts first.

### 🧭 Door 3: "Just curious / skeptical."
Good. Don't trust us — check the receipts. 👇

---

## 🧾 The trust sequence (in the order that matters)

### 1. Receipts first: a real list at full build
This isn't a demo with fake data. [`inventory-data.json`](inventory-data.json)
is **our actual live inventory** — 277 real items across 10 domains, the
same file Terri reads when *we* ask her what's Not Bought in the kitchen.
Steal the schema, steal the numbers, check our work.

Don't start from it, though — nobody should have to delete 250 rows. Start
from [`inventory-starter.json`](inventory-starter.json): **~40 rows that
keep the whole taxonomy** — the status vocabulary (`Not Bought` → `Ordered`
→ `Received`, plus `FLAG` for "a human must decide this"), the ⚠️ flag
discipline in the notes, and the owner column that ends *"I thought YOU had
it."* **The taxonomy is the jewel, not the rows.**

The wisdom is tested too: [`field-guide.md`](field-guide.md) is water math,
propane vaporization ceilings, cold-chain tiers, greywater containment, and
70+ mph anchor ratings — learned on real dust, reviewed by a veteran
big-camp infrastructure mentor.

### 2. Talk to Terri
Terri is the agent this kit forks from — meet the camp at
[terribleturtle.camp](https://terribleturtle.camp/), and watch her actual
work on the live ops hub at
[shakaleikaumaka.com/turtles](https://shakaleikaumaka.com/turtles) (the
inventory page is her reading the same `inventory-data.json` in this repo).
Ask around, see what a campmate-who-never-forgets actually feels like day
to day.

### 3. Camps that forked it
Camps trust camps. The roll of camps running forked agents lives in
**[FORKS.md](FORKS.md)** — empty today, priceless by September. Yours could
be the first name a stranger reads.

---

## 🛟 The safety model (read this before you fork)

⚠️ **One rule, above all: your agent remembers the plan — your humans own
the plan.**

This agent is a memory, not a foreman. It will happily recite your water
math (2–3 gallons per person per day — that's *our* number, check yours),
quote your power budget, and repeat what your infrastructure mentor said
about propane tank sizing. But it doesn't sign off on anything. Water,
power, propane, structure — those get decided, double-checked, and blessed
by your camp's qualified humans, every time.

Treat every number it gives you like a note from a very organized friend:
trustworthy enough to act on, never a substitute for looking with your own
eyes. If the agent and your licensed electrician disagree, the agent loses.
If the agent and your gut disagree, stop and check. A good camp agent is
humble — it says *"I don't know"* instead of inventing a spec, and it
always ends with *"confirm with your lead."*

This is also why the ultra-light offline edition exists: a single file you
can carry to the playa where there's no signal. When the network dies, the
knowledge doesn't. **Safety is redundancy.** 🐢

---

## 🤫 Two quiet disciplines (they matter more than they look)

**The sheet is the truth.** Your master spreadsheet is the source of truth;
the agent's copy is a *mirror*. When they disagree, the sheet wins — the
agent never overrules it, never edits it. It flags drift and hands a human
a paste-ready change-list. That's the whole arrangement, and it's what
makes the agent safe to trust.

**Typo kindness.** The agent gently flags typos in names, part numbers,
and URLs — kindly, with a smile, *before* they get baked into a purchase
order or a laser-cut sign. Small catches, huge savings.

---

## 📣 Forked it? TELL US. 🐢

Nobody has completion data on open-source gifts — fly blind no more.
If you fork this kit, open a 10-second issue:
**["I forked it! 🐢" → tell us your camp name](https://github.com/shakaleikaumaka/turtle-ops/issues/new?title=I%20forked%20it!%20%F0%9F%90%A2&body=Camp%20name%3A%20%0AWhere%20you%27re%20camping%20(optional)%3A%20%0AAnything%20you%20want%20us%20to%20know%3A%20)**
That's it. Camp name is enough. You land on the **[FORKS.md](FORKS.md)**
roll, the next camp trusts the receipts, and it makes our whole year.

---

## 🗺️ The whole kit, mapped

| File | What it's for |
|------|---------------|
| **[START-HERE.md](START-HERE.md)** | ← you are here |
| **[FORK-THIS-CAMP.md](FORK-THIS-CAMP.md)** | The 3-step gift-first path (saw us on playa? start here) |
| **[FORKS.md](FORKS.md)** | The roll of camps running forked agents — join it |
| [`run.md`](run.md) | The full agent prompt (the soul) + how to deploy it |
| [`inventory-starter.json`](inventory-starter.json) | **Start here** — ~40 rows, full taxonomy, ⚠️ flag discipline |
| [`inventory-data.json`](inventory-data.json) | Our real 277-item live list — the receipts at full build |
| [`field-guide.md`](field-guide.md) | Tested numbers: water, propane, cold chain, greywater, power, shade, MOOP |
| [`workflows.md`](workflows.md) | Field-tested recipes: receipt logging, transcript mining, build-day briefs, sheet sync |
| [`examples.md`](examples.md) | The agent catching what humans forgot — what good looks like |
| [`camp-agent-offline.html`](camp-agent-offline.html) | **The playa edition** — soul + memory + numbers + starter list in one offline file |
| [`templates/`](templates/) | Memory, continuity, and inventory skeletons |

**Appendix — platform quickstarts** *(a later question, not a day-one
question; fall in love first, commit later):*
[`quickstart-claude.md`](quickstart-claude.md) ·
[`quickstart-gpt.md`](quickstart-gpt.md) ·
[`quickstart-taurus.md`](quickstart-taurus.md)

---

*Move Slow & Bite Things. Heart first, always. 🐢🌺*
*Fork freely. Gift forward. — Terrible Turtle Camp*
