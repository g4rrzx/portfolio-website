---
title: "Crypto Price Monitor"
summary: "A real-time tracker for the top 20 coins with threshold alerts and browser notifications"
coverImage: "/assets/crypto-price-monitor.svg"
order: 6
---

**Crypto Price Monitor** (CryptoMonitor) is a real-time cryptocurrency
price tracker that follows the top 20 coins by market cap, refreshing
automatically every 30 seconds. It supports configurable price-threshold
alerts and live browser notifications, all powered by the public CoinGecko
API.

## Stack

- Next.js 15 (App Router)
- TypeScript
- Tailwind CSS
- CoinGecko Public API (no auth required)
- React Hooks + localStorage (state)
- Browser Notifications API
- Deployed on Vercel

## Links

- Live: [crypto-price-monitor-chi.vercel.app](https://crypto-price-monitor-chi.vercel.app)
- Source: [github.com/g4rrzx/crypto-price-monitor](https://github.com/g4rrzx/crypto-price-monitor)

## Notes

The app leans on a no-auth public API and client-side persistence to stay
dead simple to deploy — there's no backend to run. Users set their own
price thresholds, which are stored in localStorage, and the app fires a
native browser notification when a coin crosses a configured level.

Small touches make it usable: an auto-refresh toggle, a manual refresh
button, and proper loading and error states so a flaky network never
leaves the UI in a confusing place.
