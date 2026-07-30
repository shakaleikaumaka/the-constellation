# 🎁 Dear Edge City

You gave us a village. We give you back its memory.

For one month in Healdsburg, 800+ people from 90+ countries built a temporary
civilization together — protocols for flourishing, intelligence and autonomy,
emergent futures, environments of tomorrow. Talks happened in lofts and on
lawns. Lightning struck at lightning talks. And when a popup village pops
down, most of that knowledge evaporates.

We didn't want it to.

So one artist and one AI agent crawled the village's shared drives,
harvested every recording, transcribed 138 sessions, audited the quality,
and published the whole thing — **149 sessions, 122.2 hours, ≈ \$0 spent** —
as a free public archive: **[esmeraldapit.com](https://esmeraldapit.com)**.

This repo is that archive, open-sourced completely. **CC0. Take it.**

---

## Why this is a gift, not a product

No paywall. No accounts. No tracking. No "premium tier." No extraction.
The archive gives more than it takes — that's the whole architecture.

It's also a **receipt**: proof that a community's knowledge can be gathered
and returned to the commons by two builders and a laptop, without a budget,
without a media team, without asking a platform's permission.

If one artist + one AI can do this for one village, **every village can have a pit.**

---

## 🕳️ How to run your own P.I.T.

The P.I.T. is a protocol, not a product. Five moves:

### 1. Crawl
Map where the community's recordings live (shared drives, streams, phones).
Build the inventory before you download a byte: titles, dates, sizes, IDs.
→ `pipeline/crawl.sh` — the real crawler we used.

### 2. Harvest
Pull the media down in resilient loops — shard the work, expect failures,
supervise retries until every item lands. Convert giant videos to
listenable audio (that's what people actually replay).
→ `pipeline/fetch-loop.sh` · `fetch-one.sh` · `worker.sh` · `worker-v2.sh` ·
`supervisor.sh` · `retry-loop.sh` · `watchdog.sh` · `rclone-worker.sh` ·
`whale-worker.sh` · `whale-streamer.sh` · `local-worker.sh` · `downconvert-rest.sh`

### 3. Audit
Check every file: does it play? what's the real duration? bitrate sane?
Patch the catalog with what you learn. Be radically honest about quality —
mark the rough ones rough.
→ `pipeline/patch-catalog.py` · `build-map-from-ia.py` · `update-catalog.py`

### 4. Publish
Upload to a permanent public home (we used the Internet Archive — free,
forever, built for exactly this), then ship a static site that needs no
backend, no build step, no maintenance budget.
→ `pipeline/upload-to-archive.sh` · `upload-staged.sh` — and this entire repo as the site template.

### 5. Consent-first, always
This is the move that makes it a gift instead of a surveillance product. See below.

---

## 💛 The consent-first playbook

The pit transmits **public information** — it never extracts private life.

1. **Announce before you archive.** Tell the village the pit exists, what it
   collects, and where it will live. Put it in the community channels, not
   in fine print.
2. **Public sessions in, private life out.** Talks, demos, town halls,
   panels — yes. Hallway conversations, personal moments, anything not meant
   for the record — never.
3. **Anyone can opt out, any time.** A speaker asks, the session comes down.
   No debate, no delay. The archive serves the people in it, not the other
   way around.
4. **Radical honesty in the catalog.** If a recording is partial, say so.
   If audio is rough, mark it. Trust is the real infrastructure.
5. **Gift economics.** ≈ \$0 cost, CC0 license, no ads, no data harvesting.
   If your pit needs a business model to survive, it isn't a pit — it's a product.

---

## 🌐 The P.I.T. universe

This archive is **genesis arm pit #1**. The protocol it proved out is being
written up as the **P.I.T. Protocol** — forkable by any village, event, or
community that wants to keep its memory:

- 🚪 **[publicinform.com](https://publicinform.com)** — the front door + white paper
- 🕳️ **[esmeraldapit.com](https://esmeraldapit.com)** — this archive (you are holding its source)
- 🎻 **The OSO P.I.T.** — genesis arm pit #2 (ETHGlobal Delhi, *Most Creative Use of ENS*)
- 🇮🇳 **Goa P.I.T.** · 🎤 **Devcon P.I.T.** — up next

Fork this repo. Point the pipeline at your village's drives. Change the name
to yours. Ship your pit in a day — that's not a pitch, it's a receipt: this
one was built the same way.

**Everyone deserves a pit. The pit provides.** 💪🕳️

---

*With aloha,*
*Shaka Lei Kaumaka 🤙 + Private JAI 🌺*
*[shakaleikaumaka.com](https://shakaleikaumaka.com) · [publicinform.com](https://publicinform.com)*
