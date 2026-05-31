---
title: "Portfolio Website"
summary: "This site — a fast, static personal portfolio built on a custom Jinja2 + Tailwind generator"
coverImage: "/assets/portfolio-website.svg"
order: 1
---

**Portfolio Website** is my personal portfolio — the very site you're
reading now. It's a fully static site built on a custom static-site
generator (originally by
[@sagarreddypatil](https://github.com/sagarreddypatil/portfolio-website),
MIT licensed) with a CLI-terminal aesthetic, then reworked with my own
content, projects, and styling.

## Stack

- Python ([`uv`](https://docs.astral.sh/uv/) toolchain) for the build step
- Jinja2 templates + a custom `build.py` generator
- Tailwind CSS (JIT) for styling
- Markdown + front-matter for content (projects live in `posts/projects/`)
- Flask dev server for local preview
- Deployed on Vercel

## Links

- Live: [tegar-andri.vercel.app](https://tegar-andri.vercel.app)
- Source: [github.com/g4rrzx/portfolio-website](https://github.com/g4rrzx/portfolio-website)

## Notes

The build is deliberately framework-free: `pnpm build` runs three pieces —
Tailwind compiles to `dist/index.css`, `build.py` renders every Markdown
post and the index through Jinja2, and the static assets are copied over.
The result is a zero-JS-runtime bundle that loads instantly and is trivial
to host anywhere.

Content is data-driven — each project is just a Markdown file with
front-matter (`title`, `summary`, `coverImage`, `order`), so adding a new
project never touches a template. That separation of content from
presentation is what makes the site quick to maintain.
