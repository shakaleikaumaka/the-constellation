# 🧠 Quickstart: Claude Projects

Deploy your Camp Assistant on [Claude](https://claude.ai) in ~10 minutes. 🐢

## Steps

1. **Create a Project.** In Claude, go to **Projects → New Project**. Name it after your agent (e.g. "Sandy — Dusty Dolphin Camp Assistant").

2. **Paste the instructions.** Open the project's **Custom Instructions** (project settings) and paste the Agent Instructions block from [`run.md`](run.md). Replace every `[BRACKET]` with your camp's real facts.

3. **Upload knowledge files.** Add to **Project Knowledge**:
   - Your inventory export (CSV or JSON — schema: [`templates/inventory-template.csv`](templates/inventory-template.csv))
   - Your memory file (start from [`templates/MEMORY-template.md`](templates/MEMORY-template.md))
   - Build plans / playbooks, camp roster, meeting notes
   - Optionally [`field-guide.md`](field-guide.md) and [`workflows.md`](workflows.md) so the agent has the recipes on hand

4. **Test it.** Ask "what's our water plan?" and "what's still Not Bought in the kitchen?" — it should answer from your files, and say "I don't know" where the data is thin.

## The one gotcha: project knowledge is static 📌

Claude Projects don't sync to your Google Sheet. Uploaded files are **snapshots**.

- **Re-upload your inventory export periodically** — weekly during prep, more often near build week. Delete the old file when you upload the new one so the agent doesn't read two conflicting versions.
- Same for the memory file: when the agent learns something important in a chat, ask it to output an updated MEMORY file, then replace the one in Project Knowledge. That's your persistence loop.
- Your **master sheet stays the source of truth** — the project files are mirrors. See "Sheet-sync discipline" in [`workflows.md`](workflows.md).

## Tips

- Each project chat shares the knowledge but not other chats' conversation — put anything that must persist into the knowledge files.
- Paste meeting transcripts straight into a chat and use the mining workflow from [`workflows.md`](workflows.md); ask for an updated memory file at the end.
- Share the project with your whole camp lead crew — Communal Effort. 🤝

---

*Fork freely. Gift forward. — Terrible Turtle Camp 🐢*
