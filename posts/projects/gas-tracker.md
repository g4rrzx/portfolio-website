---
title: "GasTrack"
summary: "A real-time, multi-chain gas fee dashboard across five EVM networks"
coverImage: "/assets/gas-tracker.svg"
order: 7
---

**GasTrack** is a real-time gas price tracker across five EVM chains,
built for traders, builders, and anyone tired of overpaying for gas. It
shows live gas prices, historical trends, and instant USD transaction-cost
estimates — with no wallet connection required.

## Stack

- Node.js + Express
- ethers.js v6
- Vanilla JS + Chart.js (frontend)
- Public RPC endpoints (LlamaRPC + official chain RPCs)

## Links

- Source: [github.com/g4rrzx/gas-tracker](https://github.com/g4rrzx/gas-tracker)

## Notes

GasTrack tracks **Ethereum, Arbitrum, Base, Optimism, and Polygon**,
auto-refreshing every 15 seconds and charting the last 60 readings per
chain. A transaction cost estimator converts gas into USD for common
actions like swaps, transfers, and NFT mints.

The design priority was privacy and speed: no wallet connection, no
tracking — just read-only RPC queries behind a small set of clean
endpoints (`/api/gas`, `/api/gas/:chain`, `/api/history/:chain`,
`/api/estimate/:chain`). It's intentionally framework-free on the
frontend, which keeps it lightweight and fast. The motivation was simple —
finding clean, ad-free gas data across L2s shouldn't take five browser
tabs and a wallet prompt.
