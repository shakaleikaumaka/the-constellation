#!/usr/bin/env python3
"""x-post.py — post to X via OAuth 1.0a (never expires).
IRON RULE: only post what the human has personally blessed.
Usage: x-post.py "your blessed text 🌺"

CC0 — fork me like crazy 🍴 · github.com/shakaleikaumaka/agent-tweets
Setup: pip install requests requests_oauthlib
Keys:  four lines of NAME=value in a chmod-600 vault file (never in git/chat/prompts):
         X_API_KEY / X_API_SECRET / X_OAUTH1_TOKEN / X_OAUTH1_SECRET
       All four must come from the SAME generation set — regenerating consumer
       keys silently invalidates old access tokens.
Gotcha: on the free tier, the console's OAuth 2.0 "Generate" token has NO
        tweet.write scope. Use OAuth 1.0a — it's what the free tier honors."""
import sys, requests
from requests_oauthlib import OAuth1

VAULT = '/shared/.x-keys'  # ← change to your vault path, chmod 600

def load():
    d = {}
    for line in open(VAULT):
        line = line.strip()
        if line and not line.startswith('#') and '=' in line:
            k, v = line.split('=', 1); d[k] = v
    return d

if __name__ == '__main__':
    text = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read().strip()
    if not text: raise SystemExit('no text')
    d = load()
    auth = OAuth1(d['X_API_KEY'], d['X_API_SECRET'],
                  d['X_OAUTH1_TOKEN'], d['X_OAUTH1_SECRET'])
    r = requests.post('https://api.twitter.com/2/tweets',
                      auth=auth, json={'text': text})
    print(r.status_code, r.text[:400])
    sys.exit(0 if r.status_code in (200, 201) else 1)
