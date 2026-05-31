---
title: "FeryeGraph"
summary: "A cinematic, fully responsive single-page portfolio for a rally photographer"
coverImage: "/assets/feryegraph.svg"
order: 8
---

**FeryeGraph** is a cinematic, fully responsive single-page portfolio
built for a rally photographer. It pairs a dark, film-inspired hero with a
light editorial body, auto-playing project videos, and a set of custom
animated UI components.

## Stack

- React + Vite
- Tailwind CSS 3 (custom keyframes: `marquee`, `aperture`, `wave`, `film`,
  `float`, `grain`, `scroll-cue`)
- Framer Motion (scroll, stagger, parallax, in-view animations)
- lucide-react (icons)
- Google Fonts — Playfair Display + Inter

## Links

- Live: [ferye-graph.vercel.app](https://ferye-graph.vercel.app)
- Source: [github.com/g4rrzx/FeryeGraph](https://github.com/g4rrzx/FeryeGraph)

## Notes

The site is built around motion that reinforces the subject matter — an
aperture animation on skill cards, a film-strip marquee, 3D-tilt gear
cards, and project videos that only play once they scroll into view (via a
custom `useInViewVideo` hook) to keep things performant.

Content is fully data-driven: profile, projects, skills, gear, and
contacts all live in editable `data/` files, so the photographer can swap
media and copy without touching components. There's also explicit
reduced-motion handling, so the cinematic feel never comes at the cost of
accessibility.
