import sys
sys.stdin = open('C:\\CodeTest_py\\input.txt', "r")


n , k = map(int, input().split())
hp = list(input().rstrip())

cnt = 0

for i in range(n):
    if hp[i] == 'P':
        for j in range(i-k, i+k+1):
            if -1<j<n:
                if hp[j] == 'H':
                    hp[j] = '-'
                    cnt +=1
                    break
print(cnt)

