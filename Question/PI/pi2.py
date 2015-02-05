# -*- coding: utf8 -*-
import time
import random


def is_level1(l):
    return l == len(l) * [l[0]]


def is_level2(l):
    t = zip(l, l[1:])
    return all(x + 1 == y for x, y in t) or all(x - 1 == y for x, y in t)


def is_level4(l):
    return is_level1(l[::2]) and is_level1(l[1::2])


def is_level5(l):
    d = l[0] - l[1]
    return all(x - y == d for x, y in zip(l, l[1:]))


def check_level(pi):
    if is_level1(pi):
        return 1
    elif is_level2(pi):
        return 2
    elif is_level4(pi):
        return 4
    elif is_level5(pi):
        return 5
    else:
        return 10


def calculate(pi):
    start_time = time.time()
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
                if start == 0:
                    current_sum_list[k] = check_level(pi[start:end])
                elif start > 0:
                    current_sum_list[k] = optimize_sub[start-1] + check_level(pi[start:end])
                else:
                    continue
            current_min_sum = min(current_sum_list)
            optimize_sub[i] = current_min_sum
        i += 1
    end_time = time.time()
    sec = (end_time - start_time) * 1000
    print "%f ms" % sec
    return optimize_sub[pi_len-1]


if __name__ == '__main__':
    tc = int(raw_input())
    for c in xrange(tc):
        # print(calculate([int(r) for r in raw_input()]))
        print(calculate([random.randint(1, 9) for i in xrange(10000)]))