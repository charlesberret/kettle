# How to check release readiness

**Goal:** Run the automated Kettle family gates and interpret the report.

**Assumes:** You have this product-home checkout and sibling repos where relevant (`kettle-core`, `kettle-vscode`, optionally `kettle-desktop` / legacy names).

## Steps

1. From the product home:

```sh
cd /path/to/kettle
./scripts/release-ready.sh
```

2. Optional:

```sh
./scripts/release-ready.sh --strict      # non-zero exit if a required gate fails
./scripts/release-ready.sh --require-live  # also require core on :4242
```

3. Fix any **FAIL** lines in the owning repository, then re-run.

4. For documentation link integrity:

```sh
python3 scripts/check-docs.py
```

## What success looks like

- Automated gates in [release gates](../reference/release-gates.md) report **PASS** (or an intentional **SKIP** you accept for a non-strict local run).  
- Manual dogfood gates are **not** run by the script — record them separately when cutting a preview. Use [stranger-path QA](./stranger-path-qa.md) for that checklist.

## Related

- [How to run a stranger-path dogfood pass](./stranger-path-qa.md)  
- [Reference: release gates](../reference/release-gates.md)  
- [Explanation: roadmap](../explanation/roadmap.md)  
