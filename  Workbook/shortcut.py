#https://www.acmicpc.net/problem/1446
import heapq
import sys
sys.stdin = open('C:\\CodeTest_py\\input.txt', "r")

INF = int(1e9)
n,d = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

distance = [i for i in range(d+1)]

for i in range(d+1):
    distance[i] = min(distance[i], distance[i-1]+1)
    for start, end , dist in graph:
        if i ==  start and end <= d and distance[i] +dist <distance[end]:
            distance[end] = distance[start] + dist


print(distance[d])


