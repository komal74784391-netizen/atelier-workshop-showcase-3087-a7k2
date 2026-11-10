def summarize(columns):
    return {c["name"]: c["type"] for c in columns}
