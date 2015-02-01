# -*- coding: utf8 -*-


def is_level1(numbers):
    return numbers == tuple(len(numbers) * [numbers[0]])


def is_level2(l):
    t = zip(l, l[1:])
    return all(x + 1 == y for x, y in t) or all(x - 1 == y for x, y in t)


def is_level4(l):
    return is_level1(l[::2]) and is_level1(l[1::2])


def is_level5(l):
    d = l[0] - l[1]
    return all(x - y == d for x, y in zip(l, l[1:]))


if __name__ == '__main__':
    tc = int(raw_input())
    slice_list = [5, 4, 3]
    cache5 = {}
    cache4 = {}
    cache3 = {}

    for x in xrange(tc):
        final_level_sum = 0
        pi = [int(i) for i in raw_input()]
        start = 0
        end = 0
        prev_list = [0, 0, 0]

        while True:
            for step in slice_list:
                for i, v in enumerate(prev_list):
                    prev_list[i] = v+step

                    if (v+step+1) - v >= 3 or (v+step+1) - v == 0:
                        current = tuple(pi[v:prev_list[i]])

                        if step == 5:
                            find_cache = cache5
                        elif step == 4:
                            find_cache = cache4
                        elif step == 3:
                            find_cache = cache3
                        else:
                            find_cache = []

                        if current in find_cache:
                            level = find_cache[current]
                        elif is_level1(current):
                            level = 1
                        elif is_level2(current):
                            level = 2
                        elif is_level4(current):
                            level = 4
                        elif is_level5(current):
                            level = 5
                        else:
                            level = 10
                    else:
                        pass
