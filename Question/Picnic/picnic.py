# -*- coding: utf8 -*-
import sys

rl = lambda: sys.stdin.readline()

# 테스트 케이스의 수 C (C <= 50) « 입력 1
stdin_tc = int(rl())  # 3


# 학생의 수 n (2 <= n <= 10) 친구 쌍의 수 m (0 <= m <= n*(n-1)/2) « 입력2
stdin_sc = rl()  # 4 6
students_count, couples_count = stdin_sc.split(' ', 1)


# 친구쌍의 수(m)로 서로 친구인 두 학생의 번호가 주어짐 « 입력3
# (학생 번호는 0 ~ n-1, 중복쌍 없음, 학생수 모두 짝수)

friend_list = []
stdin_friends = rl()  # « 0 1 1 2 2 3 3 0 0 2 1 3
for i, f in enumerate(stdin_friends.split(' ')):
    couple = ()
    if i % 2 == 0:
        first = f.strip()
        continue
    else:
        second = f.strip()
        if not first:
            raise Exception(u"First friend is nothing..")
        if first > second:
            couple = (int(second), int(first),)  # [(0, 1), (0, 2), (1, 2), (3, 1), (2, 3)]
        elif first < second:
            couple = (int(first), int(second),)
        else:
            raise Exception(u"Same people doesn't couple")
        friend_list.append(couple)

########################################################################################
# 한 줄에 모든 학생을 친구끼리만!!! 짝지어줄 수 있는 방법의 수를 출력 » 출력1
# 3

student_list = range(int(students_count))

# 0, 1, 2, 3
# [(0 1) (1 2) (2 3)]


def number_of_case_couple(peoples, friends, case=0):
    couples = []
    temp_friends = []
    for f_index, fr in enumerate(friends):
        if fr[0] not in couples and fr[1] not in couples:
            couples.append(fr[0])
            couples.append(fr[1])
        else:
            if fr not in temp_friends:
                temp_friends.append(fr)

    if sorted(couples) == sorted(peoples):
        case += 1

    # print("PEOPLES: ", peoples)
    # print("COUPLES: ", couples)
    # print("TEMP_FR: ", temp_friends)
    # print("---------------------------------------")
    if temp_friends:
        case += number_of_case_couple(peoples, temp_friends)

    return case

print(student_list)
print(friend_list)
print(number_of_case_couple(student_list, friend_list))