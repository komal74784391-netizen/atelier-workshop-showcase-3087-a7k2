def run_eval(cases, index):
    hits = sum(1 for c in cases if c in index)
    return hits / max(len(cases), 1)
