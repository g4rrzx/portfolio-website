---
title: "HashRush"
summary: "A Web3 crypto-mining mini-app on Farcaster and Base"
coverImage: "/assets/hashrush.png"
order: 18
---

**HashRush** is a Web3 crypto-mining simulation mini-app built for
[Farcaster](https://farcaster.xyz) and [Base](https://base.org). Users can
earn "HP" points, climb the leaderboard, and claim on-chain rewards by
interacting with smart contracts directly from their social feed.

## Stack

- Next.js
- TypeScript
- Ethers.js
- Farcaster Frames
- Solidity

## Links

- Live: [hashrush.vercel.app](https://hashrush.vercel.app/)
- Source: [github.com/g4rrzx/hashrush](https://github.com/g4rrzx/hashrush)

## Notes

The goal was to blend a casual, tap-to-earn loop with real onchain
settlement — every "mining" action ultimately reconciles against a smart
contract on Base, and rewards are claimable to the user's connected wallet
without ever leaving the Farcaster feed. The Frame is rendered server-side
by Next.js so the social preview always reflects the current leaderboard
state.
