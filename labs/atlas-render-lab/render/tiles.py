def layout(tiles, width):
    return [tiles[i:i + width] for i in range(0, len(tiles), width)]
