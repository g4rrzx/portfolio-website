---
title: "Clonk"
summary: "A Farcaster mini-app paired with a custom ERC-20 token and on-chain interaction"
coverImage: "/assets/clonk.svg"
order: 2
---

**Clonk** is a [Farcaster](https://farcaster.xyz) mini-app built around a
custom ERC-20 token (`ClonkToken.sol`). Users connect their wallet and
interact with the on-chain contract directly from inside the Farcaster
frame experience — no separate dApp tab required.

## Stack

- Next.js (App Router) + TypeScript
- Solidity + OpenZeppelin (ERC-20 contract)
- wagmi + viem + RainbowKit (wallet connection)
- Farcaster Frame SDK
- Tailwind CSS
- Deployed on Vercel

## Links

- Live: [clonk.vercel.app](https://clonk.vercel.app)
- Source: [github.com/g4rrzx/clonk](https://github.com/g4rrzx/clonk)

## Notes

The repo is structured as a real mini-app rather than a contract demo: a
`contracts/` directory holds the OpenZeppelin-based ERC-20, a `scripts/`
folder handles deployment, and the Next.js `src/` renders the Farcaster
frame and wires up wallet UX with wagmi/viem.

The interesting constraint here is doing meaningful on-chain interaction
inside Farcaster's frame model — keeping the connect-and-transact flow
smooth enough that it feels native to the social feed instead of bouncing
the user out to an external dApp.
