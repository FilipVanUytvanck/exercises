def is_increasing(ns):
    ys = ns[1:]
    xs = ns[:-1]

    ax = list(zip(xs,ys))
    # [(1,a)(2,b)(3,c)]
    for a in ax:
        if a[0] > a[1]:
            return False
    return True

# def is_increasing(xs):
#     for (x, y) in zip(xs, xs[1:]):
#         if x > y:
#             return False
#     return True