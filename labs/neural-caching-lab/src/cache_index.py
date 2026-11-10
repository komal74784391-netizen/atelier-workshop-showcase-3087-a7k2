def build_index(records):
    """Reference implementation used in the workshop."""
    return {r["id"]: r for r in records}
