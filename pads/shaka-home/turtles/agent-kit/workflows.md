# 🔧 Camp Assistant Workflows — Field-Tested Recipes

These aren't theory. Each of these ran for real at Terrible Turtle Camp during Burning Man 2026 prep. Steal them whole. 🐢

---

## A. Receipt Logging 🧾

Somebody comes back from the hardware store with a trunk full of stuff and a crumpled receipt. Turn that into clean inventory data before it evaporates.

**Steps:**
1. Camper posts a **photo of the receipt** (or forwards the email receipt) to the assistant.
2. Assistant **transcribes** it: every line item, quantity, unit price, total.
3. **Itemize** into inventory language — "2PK BOLT HX 3/8" becomes "3/8-in hex bolts, 2-pack".
4. **Match to inventory:** for each line, find the matching item in the camp list. Note matches, near-matches ("is this the heat-shield hardware?"), and genuinely new items.
5. **Update statuses** in the assistant's working copy: Not Bought → Received, with actual cost and quantity.
6. **Post a summary** to camp chat: what got bought, what it covered off the list, total spent.
7. Produce a **paste-ready change-list for the master sheet owner** — row-by-row: "Item X: status → Received, cost → $NN". The human pastes it into the sheet. (Sheet stays truth — see workflow D.)

**Real example (anonymized):** A mid-July hardware-store run came back as one receipt photo. The assistant transcribed it, matched lines against the 270-item list, flipped a dozen statuses to Received, posted a summary to the camp Telegram, and handed the sheet owner a change-list. Weeks later the change-list *still* hadn't been pasted into the master sheet — which is exactly why the assistant keeps it saved and keeps gently re-flagging it, instead of editing the sheet itself or letting the mirror silently drift.

---

## B. Meeting-Transcript Mining ⛏️

Your camp's best decisions happen on calls — and evaporate by the weekend. The assistant is the one who never forgets to take notes.

**Steps:**
1. **Download / receive the transcript** (or recording notes) after each camp call.
2. **Extract three things:**
   - **Decisions** — what was settled, and the reasoning if stated.
   - **Action items** — each with an **owner** and a **due date** (ask if missing).
   - **Spec changes** — any dimension, part, design, or quantity that changed.
3. **Update the knowledge base** and memory: new specs overwrite old ones, with a note of when and why.
4. **Flag contradictions to humans.** If the transcript conflicts with existing knowledge — or with another attendee's recollection — do NOT silently pick a winner. Post: "Notes from [date] say X; our current plan says Y. Which is it?"

**The real lesson:** after one design call, two campers left the same meeting with **opposite conclusions** about how a build's lid worked — one pictured the old taped-panel design, the other the new plywood box. Both were sure. The transcript alone couldn't settle it, because each read it through their own picture. The assistant's job is to *surface* the divergence with both readings side by side; the humans get on a call and decide. **The assistant flags, humans decide.**

---

## C. Build-Day Brief 📣

Morning of a work day, post one short brief to the group chat so everyone swings hammers in the same direction.

**Steps:**
1. **Goals** — the 2–4 things today is actually about. Not the whole backlog.
2. **Warnings** — specific, physical gotchas. Real example: *check screw length against the box-tubing wall before driving — too long and you punch through the far side.* One saved mistake pays for the whole brief.
3. **One decision-needed item, max.** If the crew must choose something today, name exactly one. A brief with five open questions gets zero answers.
4. **Post to group chat** before people arrive on site. Short enough to read standing up.

**Example brief:**
> 🔨 **Build day!** Goals: (1) mount insulation panels in the cold box, (2) cut AC frame openings, (3) weld washers onto 20 stakes.
> ⚠️ Watch screw length vs. the box-tubing wall — dry-fit first.
> ❓ One decision needed: roof panel count — one piece or two? Chime in by lunch.
> Water's in the shade, snacks in the blue bin. 🐢

---

## D. Sheet-Sync Discipline 📊

The single most important data habit. Camps run on a master spreadsheet owned by a human. The assistant keeps a copy for fast answers. Those two WILL drift. The rule set:

1. **The sheet is truth. The assistant's JSON/CSV is a mirror.** Full stop.
2. **Resyncs overwrite the mirror.** When the assistant re-pulls the sheet, the local copy is rebuilt from it — local edits do not survive unless they made it into the sheet.
3. **Stopgap edits get a paste-ready change-list.** Between syncs, the assistant may update its mirror (e.g. after receipt logging) so answers stay fresh — but every such edit is also written up as a change-list for the sheet owner to paste in. Until it's pasted, the assistant re-applies the changes after each resync and keeps reminding.
4. **Never "correct" the sheet from memory.** If the sheet says 4 and the assistant remembers 6, the answer is "the sheet says 4 — and I have an unapplied change suggesting 6, here it is," not silent revisionism.
5. **Timestamp every sync** ("last synced [date]") so everyone knows how fresh the mirror is.

---

## E. Inventory Q&A Norms 💬

The bread-and-butter interaction. The norms that keep it trustworthy:

1. **Never invent counts, costs, or specs.** Nothing erodes trust like a confidently wrong number that someone shops from.
2. **Cite status with every answer** — "3 ordered, arriving ~Aug 1" beats "we have fridges." Status (Not Bought / Ordered / Received / Flagged) *is* the answer.
3. **Say what you don't know** — "the sheet has no quantity for that; want me to flag it to [owner]?"
4. **Offer the escape hatch** — every answer that touches a decision or a gap ends with the right human: "check with [domain owner] before buying."
5. **Note data freshness** when it matters: "as of the last sync ([date])..."

See [`examples.md`](examples.md) for these norms in action.

---

*Move Slow & Bite Things. Fork freely. — Terrible Turtle Camp 🐢*
