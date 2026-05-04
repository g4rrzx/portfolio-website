---
title: "Avalanche Full-stack dApp"
summary: "A 5-day full-stack dApp built on Avalanche Fuji — smart contracts, Next.js frontend, NestJS backend"
coverImage: "/assets/avalanche-fullstack-dapp.png"
order: 4
---

**Avalanche Full-stack dApp** is a complete Web3 application built on
the [Avalanche](https://www.avax.network/) C-Chain as part of a 5-day
short course at Universitas Pamulang. The goal was to go from an empty
repo to a working, deployed dApp — smart contracts, frontend, and
backend — in one week.

## Stack

**Blockchain**

- Avalanche C-Chain (Fuji Testnet)
- Solidity
- Hardhat
- Viem + Wagmi

**Frontend**

- Next.js (App Router)
- TypeScript
- Tailwind CSS

**Backend**

- NestJS
- PostgreSQL (transaction data)
- MongoDB (event / log storage)

**Deployment**

- Vercel (frontend)
- VPS / Cloud (backend)

## Links

- Live:
  [avalanche-fullstack-dapp-sigma.vercel.app](https://avalanche-fullstack-dapp-sigma.vercel.app)
- Source:
  [github.com/g4rrzx/avalanche-fullstack-dapp](https://github.com/g4rrzx/avalanche-fullstack-dapp)

## Notes

The project is deliberately structured as a *real* full-stack dApp rather
than a toy contract demo — state that must live on-chain goes on-chain,
high-volume event/log data lives in MongoDB, and normalised transaction
records live in PostgreSQL so the app stays cheap and fast to query.

Working on this solidified three things for me: (1) how to split
responsibilities between contract, backend, and frontend; (2) how to use
Viem/Wagmi idiomatically for wallet UX; and (3) how to ship a Web3 app
that looks and feels like a normal web app to the user.
