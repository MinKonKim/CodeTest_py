import sys
sys.stdin = open('C:\\CodeTest_py\\input.txt', "r")

N = int(input())

G = list(map(int,input().split()))

S =[]

G = sorted(G)

for i in range(N):
    S.append(G[i]+G[-1-i])

print(min(S))