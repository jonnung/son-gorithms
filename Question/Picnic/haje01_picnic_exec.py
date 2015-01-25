# -*- coding: utf8 -*-


def count(fa, d):
    if len(fa) == 0:
        return 1 if d == 0 else 0
    h = fa[0][0]
    s = 0
    for f in fa:
        if h in f:
            ffa = [(x, y) for x, y in fa if not(x in f or y in f)]
            s += count(ffa, d-1)
    return s


if __name__ == "__main__":
    c = int(raw_input())
    for i in xrange(c):
        n, _ = [int(v) for v in raw_input().split()]
        f = [int(v) for v in raw_input().split()]
        print count(zip(f[::2], f[1::2]), n/2)
