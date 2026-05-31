---
title: "MiMo Playground"
summary: "An interactive playground for testing Xiaomi MiMo models in real time"
coverImage: "/assets/mimo-playground.svg"
order: 12
---

**MiMo Playground** is an interactive demo for testing Xiaomi MiMo models
through the Hermes Agent framework. Pick a model, enter a prompt, and get
instant AI-generated responses — then switch models to compare outputs
side by side. Submitted to the **Xiaomi MiMo 100T Token Creator Incentive
Program**.

## Stack

- Vanilla HTML / CSS / JavaScript (zero dependencies)
- Xiaomi MiMo series (Reasoner v2.5, Chat v1, Code v1)
- Hermes Agent framework (by Nous Research)
- Deployed on Vercel

## Links

- Live: [mimo-playground.vercel.app](https://mimo-playground.vercel.app)
- Source: [github.com/g4rrzx/mimo-playground](https://github.com/g4rrzx/mimo-playground)

## Notes

The flow is deliberately minimal: select a MiMo model from a dropdown,
enter a prompt, and get a sub-second response. The real value is the
ability to switch between Reasoner, Chat, and Code variants and compare how
each handles the same prompt — useful when you're deciding which model fits
a given task.

Like the rest of my MiMo work, it's framework-free on the frontend and
built on the open-source Hermes Agent, which keeps the surface area small
and the inference loop tight.
