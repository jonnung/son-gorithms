# -*- coding: utf8 -*-
import sys


def find_friend(students, friends, case=0, prev=0):
    for i, current in enumerate(students):
        next_students = students[:]
        for another in next_students:
            if another <= current or current < prev:
                continue
            if (current, another,) in friends:
                bind_students = next_students[:]
                bind_students.remove(current)
                bind_students.remove(another)
                if bind_students:
                    case = find_friend(bind_students, friends, case, current)
                else:
                    return case+1
    return case

if __name__ == '__main__':
    std_input = lambda: sys.stdin.readline()
    tc = int(std_input())

    for x in xrange(tc):
        students_count, _ = std_input().split()
        friends_list = [int(f) for f in std_input().split()]
        couple_list = [tuple(sorted(d)) for d in zip(friends_list[::2], friends_list[1::2])]
        print(find_friend(range(int(students_count)), couple_list))
