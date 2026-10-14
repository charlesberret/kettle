# Commit conventions (Kettle family)

These conventions keep the independent Kettle repositories easy to read. An implementation repository may document a stricter local rule.

## Message shape

```text
<optional-type>: <imperative subject>

<body: why>

<footer: optional trailers>
```

Types: `feat` `fix` `docs` `chore` `refactor` `test` `ci` `style` (+ optional scope).

## Kettle automation

Install the family **commit-msg** hook:

```sh
# from kettle home
./scripts/install-git-hooks.sh
```

Or point any family repo at shared hooks:

```sh
git config core.hooksPath /path/to/kettle/scripts/git-hooks
```

See `scripts/git-hooks/README.md`. Escape hatch: `git commit --no-verify`.

The hook is optional. Pull requests are judged on clear intent and a readable history, not on whether a contributor installed local tooling.

## Trailers useful here

```text
Gate: G-core-test
```

Link issues and [release gate](./release-gates.md) IDs when a commit is meant to move them.
