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

    for x in xrange(tc):
        partial_pi = [int(i) for i in raw_input()]

        start = 0
        end = None
        last_seq = len(partial_pi)-1

        cache = {}
        min_level = 0

        while True:
            max_end = 0
            level = 0

            for step in slice_list:
                end = start + step

                if (last_seq+1) - end >= 3 or (last_seq+1) - end == 0:
                    read = tuple(partial_pi[start:end])

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

                    if level < 10:
                        if read not in cache:
                            cache[read] = level
                        max_end = end
                        break
                    else:
                        if end > max_end:
                            max_end = end
                else:
                    end = max_end
                    continue

            min_level += level
            start = max_end

            if end >= (last_seq+1):
                break

        print(min_level)
