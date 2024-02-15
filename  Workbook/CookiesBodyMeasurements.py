#쿠키의 신체 측정
# 출력
# 심장 좌표
# 왼팔, 오른팔 ,허리 ,왼다리, 오른다리 길이 순서
import sys
sys.stdin = open('C:\\CodeTest_py\\input.txt', "r")

def countBody(y,x,dirY,dirX):
    cnt = 0
    while x+dirX <N and y+dirY <N and x+dirX > -1 and y+dirY > -1 :
        x +=dirX
        y +=dirY
        if pan[y][x] == '*':
            cnt+=1
        else:
            break
    return cnt
        
def findHeart():
    for y in range(N):
        for x in range(N): 
            if pan[y][x] == '*':
                y+=1
                return (y,x)

N= int(input())

pan=[input()for _ in range(N)]

heartY, heartX  =findHeart()
print(heartY+1,heartX+1 )
print(countBody(heartY,heartX,0,-1),end=" ")#왼팔
print(countBody(heartY,heartX,0,1),end=" ")#오른팔

waist = countBody(heartY,heartX,1,0)
print(waist,end=" ")#허리

# 왼다리 
leftLegX = heartX-1
leftLegY = heartY+waist
print(countBody(leftLegY,leftLegX,1,0),end=' ')
# 오른다리1
rightLegX = heartX+1
rightLegY = leftLegY
print(countBody(rightLegY,rightLegX,1,0))


