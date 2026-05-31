---
title: "MiMo Web3 Research Agent"
summary: "An AI-powered Web3 research agent that delivers daily briefings via Telegram"
coverImage: "/assets/mimo-web3-research.svg"
order: 4
---

**MiMo Web3 Research Agent** is an AI-powered research agent built on the
Xiaomi MiMo API. It collects on-chain whale activity, social sentiment,
and crypto news, then generates daily briefings delivered through a
Telegram bot. Built as a submission for the **Xiaomi MiMo Orbit 100T
Creator Program**.

## Stack

- Python
- Xiaomi MiMo API (analysis, summarization, sentiment)
- Telegram Bot API
- Arbiscan / on-chain RPC (whale watching)
- RSS feeds (news aggregation)
- SQLite (storage)

## Links

- Source: [github.com/g4rrzx/mimo-web3-research](https://github.com/g4rrzx/mimo-web3-research)

## Notes

The architecture is a clean orchestrator pattern: a research orchestrator
sits behind a Telegram bot interface (`/brief`, `/whales`, `/social`,
`/sentiment`) and coordinates three independent collectors —

- **On-chain collector** tracks large transactions on Arbitrum, Base, and
  Optimism.
- **Social collector** monitors Farcaster channels and X accounts for
  crypto sentiment.
- **News collector** pulls RSS from top outlets (The Defiant, Bankless,
  The Block, CoinDesk).

Everything funnels into the MiMo API for analysis and summarization, then
lands in SQLite with cron-ready scripts for scheduled collection and
briefing delivery. The goal was to compress a morning of scattered tab
hopping into a single, digestible briefing.
