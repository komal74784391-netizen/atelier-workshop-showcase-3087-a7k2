def load_bands(path):
    with open(path) as fh:
        return [float(x) for x in fh.read().split()]
