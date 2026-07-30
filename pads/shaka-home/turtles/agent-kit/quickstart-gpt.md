# 💬 Quickstart: Custom GPT (ChatGPT)

Deploy your Camp Assistant as a Custom GPT in ~10 minutes. 🐢

## Steps

1. **Create the GPT.** In ChatGPT: **Explore GPTs → Create** (requires a paid plan to build). Switch to the **Configure** tab — skip the conversational builder, it's faster to configure directly.

2. **Name + description.** e.g. "Sandy — Dusty Dolphin Camp Assistant. Inventory, builds, water math, and playa wisdom for our camp."

3. **Instructions.** Paste the Agent Instructions block from [`run.md`](run.md) into the **Instructions** field. Replace every `[BRACKET]` with your camp's real facts.

4. **Knowledge.** Upload files under **Knowledge**:
   - Inventory export (CSV works great — schema: [`templates/inventory-template.csv`](templates/inventory-template.csv))
   - Memory file (start from [`templates/MEMORY-template.md`](templates/MEMORY-template.md))
   - Playbooks, roster, [`field-guide.md`](field-guide.md), [`workflows.md`](workflows.md)

5. **Enable Code Interpreter.** Under **Capabilities**, turn on **Code Interpreter & Data Analysis**. This is the killer feature for camps: the GPT can actually *compute* over your inventory CSV — sum budgets per domain, count Not-Bought items, filter by owner — instead of eyeballing it. Real math beats vibes. 📊

6. **Test it.** "How many items are still Not Bought, and what's the estimated cost?" should trigger it to load your CSV and compute, not guess.

7. **Share.** Publish to "Anyone with the link" and drop it in your camp chat.

## Gotchas

- **Knowledge files are snapshots.** Re-upload your inventory export periodically (weekly during prep; more often near build week). Remove the stale one — two versions in Knowledge means conflicting answers.
- The **master sheet stays the source of truth**; the GPT's files are mirrors. When the GPT drafts inventory changes, have it produce a paste-ready change-list for the sheet owner (see [`workflows.md`](workflows.md)).
- Custom GPTs have no cross-chat memory of their own — persistence = updating the Knowledge files.

---

*Fork freely. Gift forward. — Terrible Turtle Camp 🐢*
