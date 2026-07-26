# Commit conventions (Kettle family)

**Fleet default (canonical):**  
`~/cloud/sync/system/commit-conventions.md`  
— promoted 2026-07-25 as the system-wide agent commit format.

This file is the **Kettle-local** note: same message shape, plus where hooks live
for this family. If the two ever disagree, **system `commit-conventions.md` wins**
for shape; this file wins for **Kettle hook install paths**.

## Message shape

See the system doc. Short form:

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

Hook is optional for contributors; agents writing in this family should still
match the message shape.

## Trailers useful here

```text
Brief: 01
Gate: G-core-test
```

Link work packages and [release gate](./release-gates.md) IDs when a commit is
meant to move them.
