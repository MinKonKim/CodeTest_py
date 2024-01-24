import sys
sys.stdin = open("../input.txt","r")

"""
    흰색, 빨강색, 파랑색으로 이루어진 체스판 위 말은 순서와 각자의 진행 방향이 정해져 있다.

    1턴 : 1번 말부터 K번 말까지 순서대로!! 이동. 
    
    한말이 이동할 때 , 위에 올려져 있는말도 함께 이동.
    
    가장 아래에 있는 말만 이동할 수 있다.
    
    말이 4개 이상 쌓이는 순간 게임 종료
    
    이동 룰 :
    흰색 : 그 칸으로 이동한다. , 이동하려는 칸에 말이 이미 있으면 말을 올려놓는다.
    
    빨강 : 이동 후에, 이동한 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다.
    단, 이동 칸에 이미 있는 말은 바꾸지 않는다. 움직이는 말들만!! 바꾼다.
    
    파랑 :  A번 말의 이동 방향을 반대로 하고 한 칸 이동한다. 
            방향을 반대로 한 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 방향만 반대로 바꾼다.
            체스판을 벗어나는 경우에는 파란색과 같은 경우이다.
            
    --------------------------------------------------------------------
    
    NxN 체스판 : 0 흰색 1 빨 2 파랑 
    
    말=   좌표 2개(열 , 행) , 방향 : 1 = 오른 ,  2 = 왼 , 3 = 위 , 4 =아래 
     
"""

dirX = [0,0,-1,1]
dirY = [1,-1,0,0]

def ChangeDir(horse_idx):
    dir = horses[horse_idx][2]

    if dir == 1 or dir == 3 :
        horses[horse_idx][2]=  dir+1
    else:
        horses[horse_idx][2]= dir-1

def Move(nx,ny, horse_idx): # 이동할 위치 x, y 와 이동하는 말의 인덱스 번호
    if horses_Position[ny][nx] > -1 and board[ny][nx] == 1:
        horses.pop(horse_idx)
        horses.append([nx,ny,horses_Position[ny][nx]])
    else :
        horses[horse_idx][0] = nx
        horses[horse_idx][1] = ny
def Start():
    n =0
    while n< 1000:
        if len(horses) == K-3:
            return n
        n+=1

        for idx in range(N):
            nx = horses[idx][0] + dirX[horses[idx][2]-1]
            ny = horses[idx][1] + dirY[horses[idx][2]-1]

            if board[ny][nx] == 2:
                ChangeDir(idx)
            else:
                Move(nx,ny,idx)

        return -1


N, K = map(int, input().split())

board = [list(map(int,input().split())) for _ in range(N)]
horses = [list( map(int, input().split())) for _ in range(K)]
horses_Position = [[-1 for _ in range(N)]for _ in range(N)]
horses_Value =[i for i in range(K)]
for i  in range(K):
    x= horses[i][1]-1
    y= horses[i][0]-1
    horses_Position[y][x] = i






print(chessboard)
