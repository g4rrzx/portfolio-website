---
title: "SPK-SAW — Monitor Choice"
summary: "A Decision Support System for choosing computer monitors, using the Simple Additive Weighting method"
coverImage: "/assets/spk-saw.png"
order: 2
---

**SPK-SAW** (*Sistem Pendukung Keputusan — Simple Additive Weighting*) is
a decision-support web app that helps users rank computer monitors
against weighted criteria (resolution, refresh rate, panel type, price,
etc.) using the classical SAW method.

Built as a campus coursework project at Universitas Pamulang and deployed
as **Monitor Choice**.

## Stack

- Python (backend / SAW computation)
- SAW (Simple Additive Weighting) algorithm
- Web frontend deployed on Vercel

## Links

- Live: [monitorchoice-skp.vercel.app](https://monitorchoice-skp.vercel.app)
- Source: [github.com/g4rrzx/SPK-SAW](https://github.com/g4rrzx/SPK-SAW)

## Notes

The SAW method is one of the most widely used multi-criteria decision
making (MCDM) techniques — it normalises each criterion into a comparable
scale, weights them by importance, and sums the result so the highest
score wins. It is simple enough to explain to a non-technical user yet
powerful enough to drive real purchasing decisions.

Implementation-wise, the app lets users plug in their own weights and
candidate monitors, then shows the ranked result with a transparent
breakdown of each score — so the recommendation is never a black box.
