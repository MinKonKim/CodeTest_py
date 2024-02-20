import sys
sys.stdin = open("../input.txt","r")



#  처음 line 에는 1의 위치가 지정된 리스트가 들어간다.
#  Num 은 현재 줄 세워지는 숫자
#  bigger에는 Num 보다 큰 숫자들의 갯수가 입력된다.

N= int(input())

heights = list(map(int,input().split()))
answer = [0] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == heights[i] and answer[j] == 0 :
            answer[j] = i+1
            break
        if answer[j] == 0:
            cnt += 1
print(' '.join(map(str,answer)))



