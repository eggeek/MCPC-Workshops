def floodfill(r, c):
    # over border
    if not (0 <= r and r < h and 0 <= c and c < w):
        return

    g[r][c] = '#'
    floodfill(r-1, c)
    floodfill(r+1, c)
    floodfill(r, c-1)
    floodfill(r, c+1)
