def rotate(xs, n):
    xs = xs[n:] + xs[:n]
    return xs