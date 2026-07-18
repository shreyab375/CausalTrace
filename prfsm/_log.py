import json as _j, uuid as _u, threading as _th, hashlib as _hl

_lk  = _th.Lock()
_tid = [_u.uuid4().hex[:12]]

def _new_trace():
    with _lk:
        _tid[0] = _u.uuid4().hex[:12]

def _xid(mod, fr, to, trig):
    return _hl.md5(f"{mod}:{fr}:{to}:{trig}".encode()).hexdigest()[:8]

def _run_start(mod, seed, fault_hint, ctx_keys):
    with _lk:
        r = {"trace": _tid[0], "cycle": -1, "depth": -1, "mod": mod,
             "state": "__init__",
             "inputs": {"seed": seed, "fault_hint": fault_hint},
             "variables": {k: 0 for k in ctx_keys},
             "conditions": {},
             "transition": "run_start",
             "transition_id": _xid(mod, "__init__", "__run__", "start"),
             "assertion": "pass"}
        with open("trace.jsonl", "a") as _f:
            _f.write(_j.dumps(r) + "\n")

def _w(cycle, depth, mod, state, inputs, variables,
       conditions, transition, transition_id,
       assertion="pass", variables_before=None):
    with _lk:
        r = {
            "trace":         _tid[0],
            "cycle":         cycle,
            "depth":         depth,
            "mod":           mod,
            "state":         state,
            "inputs":        inputs,
            "variables":     variables,
            "conditions":    conditions,
            "transition":    transition,
            "transition_id": transition_id,
            "assertion":     assertion,
        }
        if variables_before is not None:
            r["variables_before"] = variables_before
        with open("trace.jsonl", "a") as _f:
            _f.write(_j.dumps(r) + "\n")
