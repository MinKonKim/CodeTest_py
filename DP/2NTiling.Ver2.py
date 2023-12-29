import sys
sys.stdin = open("../input.txt","r")


MOD = 10007

def solution(n):
    dp = [0] * (N + 1)
    dp[1] = 1
    dp[2] = 3
    if n<3 :return dp[n]
    for i in range(3,n+1):
        dp[i] = (dp[i-1]+dp[i-2]*2)%MOD

    return(dp[n])


N = int(input())
print(solution(n))

# 이게 정답
# def solution(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 3
#
#     dp = [0] * (n + 1)
#     dp[1], dp[2] = 1, 3
#     for i in range(3,n+1):
#         dp[i] = (dp[i-1]+dp[i-2]*2)%10007
#
#     return(dp[n])
#
#
# N = int(input())
# print(solution(N))
