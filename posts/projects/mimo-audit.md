---
title: "MiMo Audit"
summary: "A Next.js app for MiMo-assisted auditing of code and smart contracts"
coverImage: "/assets/mimo-audit.svg"
order: 14
---

**MiMo Audit** is a Next.js application in my Xiaomi MiMo project series,
focused on MiMo-assisted auditing — surfacing issues and risks in code or
smart contracts with help from a MiMo model.

## Stack

- Next.js (App Router) + TypeScript
- React
- Xiaomi MiMo (analysis / auditing)
- Geist font via `next/font`
- Deployed on Vercel

## Links

- Live: [mimo-audit.vercel.app](https://mimo-audit.vercel.app)
- Source: [github.com/g4rrzx/mimo-audit](https://github.com/g4rrzx/mimo-audit)

## Notes

Audit is the companion to MiMo Explain in the series — where Explain
clarifies, Audit critiques. The aim is to take a piece of code or a
contract and use a MiMo model to flag potential problems, which pairs
naturally with my interest in Web3 and contract safety.

It runs on the standard Next.js App Router stack and is deployed on Vercel,
keeping the infrastructure boring so the interesting part stays the MiMo
audit logic.
