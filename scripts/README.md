# Scripts

| Script | Purpose |
|---|---|
| [`check-docs.py`](./check-docs.py) | Verify relative Markdown links in the public product home |
| [`release-ready.sh`](./release-ready.sh) | Run local, network-free gates across sibling Kettle repositories |

```sh
python3 scripts/check-docs.py
./scripts/release-ready.sh
./scripts/release-ready.sh --strict
./scripts/release-ready.sh --require-live
```

Sibling paths can be overridden with `KETTLE_CORE`, `KETTLE_VSCODE`, and
`KETTLE_DESKTOP`.

| [`install-git-hooks.sh`](./install-git-hooks.sh) | Enable `commit-msg` hook (`git-hooks/`) |
| [`git-hooks/commit-msg`](./git-hooks/commit-msg) | Validate commit messages ([docs/reference/commit-conventions.md](../docs/reference/commit-conventions.md)) |
