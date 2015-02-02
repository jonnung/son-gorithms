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


def calculate(pi):
    # 리스트(pi)의 전체 길이(length)를 구함 (처음부터 끝까지 완전 탐색을 위한 것임)
    pi_len = len(pi)
    # 최적 부분 구조 리스트
    optimize_sub = [0] * pi_len
    # 현재 위치를 알아야 한다. (i)
    i = 0
    min_sum = 0
    # 리스트 끝까지 갈때까지 무한루프(while) 시작
    while i < pi_len:
        # 현재 위치가 2보다 작으면 모두 레벨 10이다.(i가 1부터 시작하면 3보다 작을때가 해당)
        if i < 2:
            level = 10
        else:
            start = (i - 3) + 1
            end = i + 1

            # pi[(i - 3) + 1, i + 1]  # 1, 4 [1, 2, 3]
            # pi[(i - 4) + 1, i + 1]  # 0, 4 [0, 1, 2, 3]
            # pi[(i - 5) + 1, i + 1]  # -1, 4 [4, 0, 1, 2, 3]

            if start == 0:
                pass
            elif start > 0:
                pass
            else:
                pass
            # 그 위치와 -3, -4, -5 전에 있던 것들과의 레벨을 각각 계산한다. (단, 이들 3개의 결과는 서로 영향을 주지 않는다.)
            # 각각 계산된 레벨들과 그 범위들 바로 전 위치(예: i-3)의 계산된(저장된) 값의 합이 현재까지 알고 있는 가장 최소값보다 작으면 대체된다.
            # 리스트의 끝까지 가기전에는 가장 최소값은 의미가 없다. 리스트 끝에서 계산되는 레벨합 중에 가장 최소값(최종해)을 구하면 된다.
        optimize_sub[i] = level



if __name__ == '__main__':
    tc = int(raw_input())

    for c in xrange(tc):
        print(calculate(tc))