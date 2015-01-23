# -*- coding: utf8 -*-
import sys


def find_friend(students, friends, case=0, prev=0):
    for i, current in enumerate(students):
        next_students = students[:]
        for another in next_students:
            if another <= current or current < prev:
                continue
            if (current, another,) in friends:
                bind_people = next_students[:]
                bind_people.remove(current)
                bind_people.remove(another)
                if bind_people:
                    case = find_friend(bind_people, friends, case, current)
                else:
                    return case+1
    return case


stdin = lambda: sys.stdin.readline()
test_case = int(stdin())

for x in range(test_case):
    students_and_couples = stdin()
    students_count, couple_count = students_and_couples.split(' ', 1)

    friend_list = []
    friends = stdin()
    for i, f in enumerate(friends.split(' ')):
        couple = ()
        if i % 2 == 0:
            first = f.strip()
            continue
        else:
            second = f.strip()
            if not first:
                raise Exception(u"First friend is nothing..")
            if first > second:
                couple = (int(second), int(first),)
            elif first < second:
                couple = (int(first), int(second),)
            else:
                raise Exception(u"Same people doesn't couple")
            friend_list.append(couple)

    student_list = range(int(students_count))
    print(find_friend(student_list, friend_list))
