# 키 순서

import sys
sys.stdin = open("../input.txt", "r")


"""
    a번의 학생의 키가 b번 학생의 키보다 작다면, a->b
"""

def dfs(graph, start):
    visited = [False]*(N+1)
    stack =[start]

    while stack:
        v = stack.pop()
        for i in graph[v]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True

    return visited.count(True)


# 학생들의 수 N과 비교 횟수 M을 입력 받습니다.
N, M = map(int, sys.stdin.readline().split())

# 각 학생이 다른 학생보다 작은지 큰지를 저장할 두 개의 그래프를 준비합니다.
smaller = [[] for _ in range(N+1)]
bigger = [[] for _ in range(N+1)]

# 비교 결과를 입력 받아 그래프를 구성합니다.
for _ in range(M):
    a, b = map(int, input().split())
    smaller[b].append(a)
    bigger[a].append(b)

answer =0
for student in range(1, N+1):
    if dfs(smaller, student) + dfs(bigger, student) == N - 1:
        answer += 1


print(answer)

