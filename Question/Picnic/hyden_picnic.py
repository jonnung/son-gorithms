# -*- coding: utf-8 -*-

import sys

rl = lambda: sys.stdin.readline()


def f(l):
    if len(l) == 1:
        return 1
    i = 0
    for e in l:
        if l[0][0] in e:
            sub = [e_ for e_ in l if not (e[0] in e_ or e[1] in e_)]
            if sub:
                i += f(sub)
    return i


c = int(rl())
for s in range(c):
    rl()
    d = [int(v) for v in rl().split()]
    ind = zip(d[::2], d[1::2])
    print f(ind)