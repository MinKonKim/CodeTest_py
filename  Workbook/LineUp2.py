# 줄세우기 문제번호 : 2631  알고리즘 : DP
import sys
sys.stdin = open('C:\\CodeTest_py\\input.txt', "r")


N = int(input())

children =[int(input()) for _ in range(N)]

dp= [1]*N

for i in range(N):
    for j in range(i):
        if children[i] > children[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(dp)
print(N-max(dp))