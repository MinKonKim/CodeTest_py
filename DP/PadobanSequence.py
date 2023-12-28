import sys
sys.stdin = open("../input.txt","r")

def solution(N):
    dp =[1,1,1,2,2]
    if N < 5:
        return dp[N]
    for i in range(5,N):
        dp.append(dp[i-1]+dp[i-4])
    print(dp[-1])

T = int(input())

for _ in range(T):
    N = int(input())
    solution(N)
