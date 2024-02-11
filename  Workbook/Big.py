#덩치
import sys
sys.stdin = open('C:\\CodeTest_py\\input.txt', "r")

N = int(input())
people = []

for _ in range(N):
    w, h = map(int, input().split())
    people.append((w, h))

for i in range(N):
    rank = 1
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    print(rank, end=' ')

