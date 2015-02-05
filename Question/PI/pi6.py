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


def check_level(pi, i, j):
    if j is 3:
        sub_pi = [pi[i-2], pi[i-1], pi[i]]
    elif j is 4:
        sub_pi = [pi[i-3], pi[i-2], pi[i-1], pi[i]]
    elif j is 5:
        sub_pi = [pi[i-4], pi[i-3], pi[i-2], pi[i-1], pi[i]]

    if is_level1(sub_pi):
        level = 1
    elif is_level2(sub_pi):
        level = 2
    elif is_level4(sub_pi):
        level = 4
    elif is_level5(sub_pi):
        level = 5
    else:
        level = 10
    return level


def calculate(pi):
    start_time = time.time()
    # 리스트(pi)의 전체 길이(length)를 구함 (처음부터 끝까지 완전 탐색을 위한 것임)
    pi_len = len(pi)
    # 최적 부분 구조 리스트
    optimize_sub = [0] * pi_len
    # 현재 위치를 알아야 한다. (i)
    i = 0
    slice_list = [3, 4, 5]

    # 리스트 끝까지 갈때까지 무한루프(while) 시작
    while i < pi_len:
        min_sum = 10000 * 10
        # 현재 위치가 2보다 작으면 모두 레벨 10이다.(i가 1부터 시작하면 3보다 작을때가 해당)
        if i < 2:
            optimize_sub[i] = 10
        else:
            end = i + 1

            for k, j in enumerate(slice_list):
                start = (i - j) + 1
                if start == 0:
                    current_sum = check_level(pi, i, j)
                elif start > 0:
                    current_sum = optimize_sub[start-1] + check_level(pi, i, j)
                else:
                    continue

                if current_sum < min_sum:
                    min_sum = current_sum
            # 그 위치와 -3, -4, -5 전에 있던 것들과의 레벨을 각각 계산한다. (단, 이들 3개의 결과는 서로 영향을 주지 않는다.)
            # 각각 계산된 레벨들과 그 범위들 바로 전 위치(예: i-3)의 계산된(저장된) 값의 합이 현재까지 알고 있는 가장 최소값보다 작으면 대체된다.
            # 리스트의 끝까지 가기전에는 가장 최소값은 의미가 없다. 리스트 끝에서 계산되는 레벨합 중에 가장 최소값(최종해)을 구하면 된다.
            optimize_sub[i] = min_sum
        i += 1
    end_time = time.time()
    sec = (end_time - start_time) * 1000
    print "%f ms" % sec
    return optimize_sub[pi_len-1]


if __name__ == '__main__':
    for c in xrange(int(raw_input())):
        # print(calculate([int(r) for r in raw_input()]))
        print(calculate([random.randint(1, 9) for i in xrange(10000)]))