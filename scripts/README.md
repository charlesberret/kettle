# Scripts

| Script | Purpose |
|--------|---------|
| [`release-ready.sh`](./release-ready.sh) | Automated family gates for Release 0.1+ (`docs/RELEASE.md`) |

```sh
./scripts/release-ready.sh
./scripts/release-ready.sh --strict
./scripts/release-ready.sh --require-live
```

Environment overrides: `KETTLE_CORE`, `KETTLE_VSCODE`, `SETSWEEP_CORE`.

| [`install-git-hooks.sh`](./install-git-hooks.sh) | Enable `commit-msg` hook (`git-hooks/`) |
| [`git-hooks/commit-msg`](./git-hooks/commit-msg) | Validate commit messages ([docs/COMMIT.md](../docs/COMMIT.md)) |
