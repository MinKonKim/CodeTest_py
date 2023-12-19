MOD = 10007

def solution (n):
    if n<=2:
        return n
    dp = [0]*(n+1)
    dp[1] =  1 
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1]+dp[i-2])%MOD
    return dp[n]

n = int(input())
print(solution(n))

# n=int(input())
# a,b=1,2
# for i in range(n-2):a,b=b,(a+b)%10007
# print(b if n>1 else a)