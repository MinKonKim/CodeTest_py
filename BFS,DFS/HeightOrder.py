# 키 순서

import sys
sys.stdin = open("../input.txt", "r")


"""
    a번의 학생의 키가 b번 학생의 키보다 작다면, a->b
"""

def dfs(heights ,root):

    n = len(heights)
    smaller = [0]*  n

    stack = []
    stack.append(root)
    while stack:
        i = stack.pop()
        if heights[i]:
            for j in heights[i]:
                stack.append(j)
                smaller[j] +=1
    return smaller


N, M = map(int, input().split())

heights = [[]for _ in range(N+1)]
for _ in range(M):
    a , b = map(int, input().split())
    heights[a].append(b)

smaller = [0] * (N+1)
visited =[False for _ in range(N+1)]
stack= []

while stack:
    for i in range(N+1):
        if heights[i]:
            stack.append()



for row in heights:
    print(row)


