# Tutorial: your first Kettle sitting

**You will:** install the core from source, open the web sitting, register a
project folder, and run a minimal review path (or founding if the desk is new).

**You need:** Python 3.11+, a supported agent CLI already authenticated on your
machine, about fifteen minutes.

This is a **lesson**, not a complete feature map. For packaging bars see
[release readiness](../how-to/check-release-readiness.md). For architecture see
[explanation](../explanation/architecture.md).

---

## 1. Get the core

To use Kettle without a checkout, the one line in the [product README](../../README.md)
is enough. This lesson uses a checkout so the files you read are the files that run.

```sh
git clone https://github.com/charlesberret/kettle-core.git
cd kettle-core
python3 -m venv .venv
.venv/bin/pip install -e .
.venv/bin/kettle doctor
```

If `doctor` reports PATH issues, use the venv binary for the rest of this tutorial
(`.venv/bin/kettle …`).

---

## 2. Start the local server

```sh
.venv/bin/kettle --web
```

Open [http://127.0.0.1:4242](http://127.0.0.1:4242). Leave this process running.

---

## 3. Register a project

Pick a **folder under your home directory** that you do not mind Kettle writing
desk files into (`.kettle/` — or legacy `.setsweep/` if dual-read applies).

In the web UI: add / register the project (name + folder).  
Or in another terminal:

```sh
.venv/bin/kettle add ~/path/to/a-project
```

---

## 4. Found or open the desk

- **New / unfounded project:** complete the founding interview in the agent pane
  until you have a proposal you accept, then found the desk so a content queue
  appears.
- **Already founded:** select the project and open a queue entry.

You are not graded on a perfect charter — the goal is to **see the loop**.

---

## 5. One review pass

1. Open a queue entry (or the proposal if still founding).  
2. Read the **brief**.  
3. Edit the file if needed.  
4. Optionally leave a **comment** for the sweep.  
5. **Approve** when your ruling is done (bookmark — it does not publish outward).  
6. When ready, run a **sweep** (or note that you reached the control and stop).

---

## 6. Optional: same desk from the shell

```sh
.venv/bin/kettle projects
.venv/bin/kettle queue <project>
.venv/bin/kettle chat <project>   # optional; curator must already be authenticated
.venv/bin/kettle doctor
```

Shell and web should describe the **same** desk. That pairing is intentional
product craft, not a side effect. Plugin chat (VS Code / Cursor) is the same
stream rendered in the editor, not a second product.

---

## You finished when…

- [ ] Core installs and `doctor` is usable  
- [ ] Web UI loads on port 4242  
- [ ] A project is registered  
- [ ] You completed at least one approve (or a clear founding step)  

**Next:** [how-to: stranger-path QA](../how-to/stranger-path-qa.md) for a full
dogfood checklist; [how-to: check release readiness](../how-to/check-release-readiness.md)
if you are contributing; [explanation: architecture](../explanation/architecture.md)
if you want the family map.
