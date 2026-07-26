# Scripts

| Script | Purpose |
|---|---|
| [`check-docs.py`](./check-docs.py) | Verify relative Markdown links in the public product home |
| [`release-ready.sh`](./release-ready.sh) | Run local, network-free gates across sibling Kettle repositories |
| [`install-git-hooks.sh`](./install-git-hooks.sh) | Enable the optional `commit-msg` hook |
| [`git-hooks/commit-msg`](./git-hooks/commit-msg) | Validate messages against the [commit convention](../docs/reference/commit-conventions.md) |

```sh
python3 scripts/check-docs.py
python3 scripts/check-docs.py ../kettle-core
./scripts/release-ready.sh
./scripts/release-ready.sh --strict
./scripts/release-ready.sh --require-live
```

Sibling paths can be overridden with `KETTLE_CORE`, `KETTLE_VSCODE`, and
`KETTLE_DESKTOP`.
