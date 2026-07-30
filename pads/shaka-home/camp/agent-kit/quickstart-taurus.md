# 🐂 Quickstart: Taurus

Deploy your Camp Assistant on [Taurus](https://app.taurusagents.com/) — this is how Terri herself runs. Taurus agents get a real container, persistent files, scheduled runs, and public dashboards. The most powerful option, and the most alive. 🐢

## Steps

1. **Create an agent.** New agent, name it, and paste the Agent Instructions block from [`run.md`](run.md) as the **agent prompt**. Replace every `[BRACKET]` with your camp's real facts.

2. **Set up the memory file.** Taurus agents auto-load the top of `/workspace/MEMORY.md` into every run. Create it from [`templates/MEMORY-template.md`](templates/MEMORY-template.md). This is the agent's long-term brain — most important facts at the top, one section per domain.

3. **Set up continuity.** Create `/workspace/continuity/` and log each run in monthly files, newest first (pattern: [`templates/continuity-template.md`](templates/continuity-template.md)). Memory = what's true now; continuity = what happened when.

4. **Feed it data.** Drop your inventory export in the workspace (schema: [`templates/inventory-template.csv`](templates/inventory-template.csv)). If your master sheet is a public Google Sheet, the agent can pull the CSV export itself and resync on demand — sheet stays the source of truth, the local copy is a mirror.

5. **Choose run style:**
   - **On-demand** (our choice): the agent runs when someone messages it. Cheap, calm, turtle-paced.
   - **Scheduled**: cron runs for daily briefs or sheet-change monitoring. Great during build week; overkill in the off-season.

6. **Optional: public dashboard.** Files in `/shared/public/<slug>/` are served as a website. Our whole [Turtle Ops hub](../index.html) is built this way — inventory viewer, playbooks, live "Right Now" panel. Your agent can build and maintain one for your camp.

7. **Optional: chat bridge.** Wire the agent into your camp's Telegram/group chat so campmates can ask it things where they already talk.

## Tips

- Tell the agent to **write facts to MEMORY.md the moment it learns them** — decisions, spec changes, new people. Runs are ephemeral; files persist.
- Give it standing orders in MEMORY.md (e.g. "sheet is truth", "flag typos kindly").
- Load [`field-guide.md`](field-guide.md) and [`workflows.md`](workflows.md) into its workspace so the recipes are one `Read` away.

---

*Fork freely. Gift forward. — Terrible Turtle Camp 🐢*
