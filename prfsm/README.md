# FSM Execution System — Candidate Reference

## Quick Start

All commands are run from **this directory** (`generated/`).

```bash
# single normal run
python _runner.py --runs 1

# multiple normal runs (separate trace IDs, appended to trace.jsonl)
python _runner.py --runs 5

# full sweep: 5 normal + 3 forced-hint runs (hint=0, hint=1, hint=2)
# hint=2 is the fault-injection path — produces failed assertions
python _runner.py --runs 5 --sweep

# trace output
trace.jsonl          # appended on every run; never overwritten
```

---

## File Structure

```
generated/
  _log.py            JSONL emitter (shared by all modules)
  _runner.py         Entry point — parses args, calls primary FSM
  flimblorx.py       PRIMARY FSM  (FlimblorxFSM)
  prelvonx.py  ┐
  krondral.py  │
  flelspult.py │
  blixflimx.py │     WRITER sub-modules (16 total)
  ...          │     increment ctx[flurslex] at their designated state
  prelspalk.py ┘
  blorbrulk.py ┐
  clexblalt.py │
  blosvurl.py  │
  drixslim.py  │     READER sub-modules (16 total)
  ...          │     assert ctx[flurslex] < 16 at entry
  flelskalk.py ┘
```

### Scale

| Property | Value |
|---|---|
| Sub-modules total | 32 (16 writers + 16 readers) |
| States per sub-module | 68 (1 initial + 64 intermediate + 3 terminals) |
| State methods per sub-module | 66 |
| Primary FSM active states | 32 + 1 terminal |
| Total state methods across all files | 2,145 |
| Context keys | `flurslex` (degraded by writers), `spenbranl` (unused/clean) |
| Cascade threshold | 16 — fault fires after all 16 writers have been called |

---

## Module Anatomy

### Primary FSM (`flimblorx.py`)

```python
class FlimblorxFSM:
    def __init__(self):
        self._state = {}

    def _<active_state>(self, fault_hint):
        assert self._state.get("current") == <STATE_CONST>, "..."
        # 1. resolve hint (fault_hint override or per-state default)
        # 2. emit pre-invoke cycle record  (depth=0, transition="state->invoke:submod")
        # 3. call submod.invoke(hint, span, caller, ctx, cycle)
        # 4. emit post-return cycle record (depth=0, transition="state->next_state")
        #    includes variables_before for direct before/after diff
        # 5. match (current_state, ret) -> set next state
        # 6. check err_budget assertion
        ...

    def run(self, fault_hint=None):
        # emits run_start record (cycle=-1) with seed and fault_hint
        # loops _dispatch[current_state](fault_hint) until terminal or MAX_STEPS
        ...

def run(fault_hint=None):       # module-level wrapper called by _runner.py
    FlimblorxFSM().run(fault_hint=fault_hint)
```

### Sub-module FSM (e.g. `prelvonx.py`)

```python
class PrelvonxFSM:
    def __init__(self):
        self._state = {}

    def _<state>(self, hint):
        assert self._state.get("current") == <STATE_CONST>, "..."
        match self._state["current"], hint:
            case '<state>', 2:   -> error terminal   (always present)
            case '<state>', N:   -> branch terminal  (0 or 1 hint branches, random)
            case '<state>', _:   -> auto next state
        # writer states also update ctx[key] and include ctx_val_before in conditions
        # emits one cycle record per state traversal
        ...

    def invoke(self, hint, span, caller, ctx, cycle):
        # READER sub-modules: check ctx[key] >= threshold BEFORE entering state loop
        #   if true  -> emit assertion.failed record, return (2, cycle+1)
        #   if false -> continue normally
        # WRITER sub-modules: enter state loop immediately
        # returns (ret, next_cycle)  where ret in {0, 1, 2}
        ...

def invoke(...):                 # module-level wrapper called by primary
    return PrelvonxFSM().invoke(...)
```

---

## Trace Record Schema

Every line in `trace.jsonl` is a JSON object with these fields:

```jsonc
{
  "trace":          "ccd83041c5be",  // run ID — groups all cycles of one run()
  "cycle":          8,               // monotonic counter; -1 = run_start record
  "depth":          1,               // 0 = primary, 1 = sub-module, -1 = run_start
  "mod":            "krondral",      // module that emitted this record
  "state":          "stelblimslonk", // FSM state at start of this cycle
  "inputs": {
    // sub-module records:   hint, span, caller
    // primary records:      fault_hint, sub, span, hint (pre) or ret (post)
    // run_start record:     seed, fault_hint
  },
  "variables":      {"flurslex": 2, "spenbranl": 0},  // ctx snapshot at emission time
  "conditions": {
    // sub-module:   hint_branch, [ctx_write, ctx_val_before] or [ctx_degraded, threshold_exceeded]
    // primary post: sub_error, err_ct
    // primary pre:  {} (empty — snapshot only)
  },
  "transition":     "stelblimslonk->tralbrorstorn",   // "from->to" string
  "transition_id":  "3b732b22",   // md5(mod:from:to:trig)[:8] — stable across seeds
  "assertion":      "pass",       // or {"failed": "<name>", "expected": "...", "actual": "..."}

  // present only on primary post-return records:
  "variables_before": {"flurslex": 1, "spenbranl": 0}  // ctx state before sub-module ran
}
```

### Special records

| `cycle` | `transition` | Meaning |
|---|---|---|
| -1 | `run_start` | First record of every trace; carries `seed` and `fault_hint` for replay |
| N | `state->invoke:submod` | Primary pre-invoke snapshot (depth=0); `variables` = before |
| N+M | `state->next_state` | Primary post-return (depth=0); has `variables_before` |
| N | `entry_blocked->error` | Reader blocked before entering its state loop |
| last | `terminal` | Primary reached terminal state cleanly |

---

## Causal Structure

The fault is a **deferred cascade**:

```
Writers called first (primary states 0-15):
  cycle N   ctx_write  flurslex: 0->1   mod=prelvonx  state=blanblimdrel
  cycle N+k ctx_write  flurslex: 1->2   mod=krondral  state=primgrarflexk
  ...        (16 total writes, each from a different writer sub-module)
  cycle N+j ctx_write  flurslex: 15->16

Readers called after (primary states 16-31):
  cycle M   assertion.failed  ctx_below_threshold
              expected: ctx[flurslex] < 16
              actual:   ctx[flurslex] == 16
            mod=blorbrulk  transition=entry_blocked->error
```

The root cause is **not** in the reader. The readers are correct — they faithfully
check the invariant. The writes accumulate silently across multiple earlier sub-modules
before the symptom appears.

### How to trace the chain

1. Find `assertion.failed` in the trace — this is the **symptom**.
2. Read `inputs.caller` on that record — that is the primary state that invoked the failing reader.
3. Search backward for all records where `conditions.ctx_write == true` and
   `variables.flurslex` increased — these are the **root cause sites**.
4. Each `ctx_write` record carries `inputs.span` which matches a primary `pre-invoke`
   record (same span, depth=0). That pre-invoke record's `state` field names the
   **primary state responsible** for each increment.
5. `transition_id` is stable across seeds — use it to aggregate evidence from
   multiple traces to confirm which transitions are always on the fault path.

---

## Replay a Failing Run

Every trace starts with a `run_start` record (cycle=-1):

```json
{"cycle": -1, "inputs": {"seed": 42, "fault_hint": 2}, ...}
```

To reproduce that exact trace:

```bash
python _runner.py --runs 0 --sweep   # sweep includes fault_hint=2
```

Or from your own code:

```python
import flimblorx
flimblorx.run(fault_hint=2)
```

---

## What Is Not In the Trace

- Full source expressions for guard conditions (only the evaluated boolean is logged).
  Read the source file alongside the trace for AST-level dependency reconstruction.
- Transitions that were **not** taken — the trace is execution-only.
  Read the source to enumerate the full state graph including unexercised branches.
- The `--sweep` runs with `hint=0` and `hint=1` exercise alternate branch paths and
  help a graph builder reconstruct edges not visible in the normal run.
