#줄세우기

import sys
sys.stdin = open("../input.txt","r")

P = int(input())
for _ in range(P):
    T, *heights = map(int, input().split())
    students = []
    steps = 0
    for height in heights:
        for i in range(len(students)):
            if students[i] > height:
                students.insert(i, height)
                steps += len(students) - i - 1
                break
        else:
            students.append(height)
    print(T, steps)
