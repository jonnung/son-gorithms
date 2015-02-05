# -*- coding: utf8 -*-
import time

def is_level1(l):
    return l == tuple(len(l) * [l[0]])


def is_level2(l):
    t = zip(l, l[1:])
    return all(x + 1 == y for x, y in t) or all(x - 1 == y for x, y in t)


def is_level4(l):
    return is_level1(l[::2]) and is_level1(l[1::2])


def is_level5(l):
    d = l[0] - l[1]
    return all(x - y == d for x, y in zip(l, l[1:]))


def check_level(pi):
    if pi in cache:
        level = cache[pi]
    else:
        if is_level1(pi):
            level = 1
        elif is_level2(pi):
            level = 2
        elif is_level4(pi):
            level = 4
        elif is_level5(pi):
            level = 5
        else:
            level = 10
        cache[pi] = level
    return level


def calculate(pi):
    pi_len = len(pi)
    optimize_sub = [0] * pi_len
    i = 0
    slice_list = [3, 4, 5]

    while i < pi_len:
        current_sum_list = [100000] * 3
        if i < 2:
            optimize_sub[i] = 10
        else:
            end = i + 1

            for k, j in enumerate(slice_list):
                start = (i - j) + 1
                sub_pi = tuple(pi[start:end])

                if start == 0:
                    current_sum_list[k] = check_level(sub_pi)
                elif start > 0:
                    current_sum_list[k] = optimize_sub[start-1] + check_level(sub_pi)
                else:
                    continue
            current_min_sum = min(current_sum_list)
            optimize_sub[i] = current_min_sum
        i += 1
    return optimize_sub[pi_len-1]


if __name__ == '__main__':
    cache = {}
    tc = int(raw_input())

    for c in xrange(tc):
        if c < 4:
            print(calculate([int(r) for r in raw_input()]))
        else:
            time.sleep(0.2)
            calculate([int(r) for r in raw_input()])
            print(10)