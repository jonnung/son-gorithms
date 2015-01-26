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
    cache = {}

    for x in xrange(tc):
        partial_pi = [int(i) for i in raw_input()]
        start = 0
        end = None
        last_seq = len(partial_pi)-1
        total_level = 0

        while True:
            max_end = 0
            level = 0
            step_by_level = {
                3: 0,
                4: 0,
                5: 0
            }

            for step in slice_list:
                end = start + step

                if (last_seq+1) - end >= 3 or (last_seq+1) - end == 0:
                    read = tuple(partial_pi[start:end])

                    # print(tuple(input[start:end]))

                    if read in cache:
                        level = cache[read]
                    elif is_level1(read):
                        level = 1
                    elif is_level2(read):
                        level = 2
                    elif is_level4(read):
                        level = 4
                    elif is_level5(read):
                        level = 5
                    else:
                        level = 10

                    step_by_level[step] = level
                    cache[read] = level
                else:
                    continue
            filter_level = dict((k, v) for k, v in step_by_level.items() if v > 0)
            min_level = min(filter_level.values())

            if min_level < 10:
                consider_step = max([int(s) for s, v in step_by_level.items() if v == min_level])
            else:
                consider_step = min(filter_level.keys())

            total_level += min_level
            start = start + consider_step

            if start >= (last_seq+1):
                break

        print(total_level)
