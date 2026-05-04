# Tegar Andriyansyah — Portfolio

Personal portfolio of **Tegar Andriyansyah** (Developer, Researcher, and
Web3 Enthusiast). Built on the custom static site generator created by
[@sagarreddypatil](https://github.com/sagarreddypatil/portfolio-website)
(MIT licensed, original `LICENSE` preserved).

Content (name, projects, research, contact) is sourced from my previous
site at <https://tegar-andri.vercel.app/>; the generator, templates, and
CLI-terminal look are from upstream.

## Dependencies

- [`uv`](https://docs.astral.sh/uv/) — Python toolchain
- [`pnpm`](https://pnpm.io/) — JS package manager

```sh
uv sync
pnpm install
```

## Development

```sh
pnpm dev
```

Runs three concurrent watchers:

- `pnpm watch:tailwind` — Tailwind CSS JIT → `dist/index.css`
- `pnpm watch:html` — rebuilds HTML via `uv run python src/build.py`
- `pnpm flask-dev` — Flask dev server at <http://localhost:8000>

## Production

```sh
pnpm build
```

Outputs a fully static bundle to `dist/`. Preview with:

```sh
pnpm preview
```

## Replacing the profile photo

`public/assets/me.jpg` ships as a 700×700 placeholder. Overwrite it
with a real photo (same filename) to update both the landing page image
and the OpenGraph preview — no template change required.

## Project structure

```
tegar/
├── README.md                # this file
├── LICENSE                  # MIT (upstream, preserved)
├── package.json             # JS deps & dev scripts
├── pnpm-lock.yaml
├── pyproject.toml           # Python deps
├── uv.lock
├── tailwind.config.js
├── build.sh                 # prod build script, invoked by `pnpm build`
├── posts/
│   └── projects/
│       ├── hashrush.md
│       ├── fcscheduler.md
│       └── farcaster-roulette.md
├── public/
│   ├── favicon.svg          # "t" monogram
│   ├── robots.txt
│   └── assets/
│       ├── github.svg
│       ├── linkedin.svg
│       ├── me.jpg           # profile photo (OG image + landing page)
│       ├── hashrush.png
│       ├── fcscheduler.png
│       └── rouletee.png
└── src/
    ├── build.py             # main entrypoint (identity vars at top)
    ├── dev-server.py        # flask live-reload server
    ├── index.css            # tailwind imports + prose tweaks
    └── templates/
        ├── layout.html      # base layout, header, footer
        ├── index.html       # landing page (about · projects · research · contact)
        ├── components/
        │   ├── button.html
        │   └── fieldset.html
        └── posts/
            └── projects/
                ├── list.html  # card grid rendered into index
                └── page.html  # individual project page
```

## Editing content

- **Name / SEO / domain** — top of `src/build.py` (`first_name`,
  `last_name`, `domain`, `generic_username`).
- **Header title + social buttons** — `src/templates/layout.html`.
- **About / Research / Contact sections** — `src/templates/index.html`.
- **Projects** — add a new markdown file in `posts/projects/` with
  frontmatter `title`, `summary`, `coverImage`, `order`. Drop the cover
  image into `public/assets/`.