import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import flimblorx

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--runs",  type=int, default=1)
    p.add_argument("--sweep", action="store_true")
    a = p.parse_args()
    total = 0
    for _ in range(a.runs):
        flimblorx.run()
        total += 1
    if a.sweep:
        for _fh in [0, 1, 2]:
            flimblorx.run(fault_hint=_fh)
            total += 1
    print(f"{total} run(s) complete -- trace.jsonl updated")
