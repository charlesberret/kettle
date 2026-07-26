# Kettle product home

This repository is the **product home** for Kettle (star / clone target).

Local checkouts may live under `~/cloud/git-projects/kettle`. Public name: **Kettle**.

## Planning vs public docs

| Path | In git? | Purpose |
|------|---------|---------|
| `docs/` | yes | Public product docs, architecture, shipping notes |
| `planning/` | **no** (gitignored) | Private design, renames, open questions, scratch — **same name in every family repo** |

Do not put secrets in either tree. Keep launch strategy and unfinished naming debates in `planning/`.

## Roadmap & release

- [`ROADMAP.md`](./ROADMAP.md) — phases  
- [`RELEASE.md`](./RELEASE.md) — gates  
- [`WORKFLOW.md`](./WORKFLOW.md) — how work is divided  
- [`briefs/`](./briefs/) — work packages  

```sh
./scripts/release-ready.sh
```

## Related (pre-Kettle)

Earlier work may still live under `setsweep` / `setsweep-plugin` / `setsweep-desktop` checkouts. Migration into this tree is intentional and gradual — not a bulk copy on day one.
