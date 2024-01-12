import sys
sys.stdin = open("../input.txt","r")

"""
    말은 순서와 각자의 진행 방향이 정해져 있다.

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

class Horse :


    def __init__(self, col, row, dir,stackNumber):
        self.stackNumber = stackNumber
        self.row = row
        self.col = col
        self.dir = dir

    def move(self, n, index ):
        if index != int(self.stackNumber[0]):
            return
        if self.dir == 1 and self.row+1 <n: # Right
            self.row+=1
        elif self.dir == 2 and self.row-1 >-1: # Left
            self.row -=1
        elif self.dir == 3 and self.col-1 >-1: # Up
            self.col -=1
        elif self.dir == 4 and self.col+1< n: # Down
            self.col +=1
    def upper(self, horse): # 움직이는 말, 밑에 있는 말
        self.stackNumber = horse.stackNumber+ self.stackNumber
        self.dir = horse.dir

    def update(self, color):
        if color == 1:
            sn_list = list(self.stackNumber)
            sn_list.reverse()
            self.stackNumber = ''.join(sn_list)
        elif color == 2:
            if self.dir == 1:
                self.dir = 2
            elif self.dir == 2:
                self.dir = 1
            elif self.dir == 3:
                self.dir = 4
            elif self.dir ==4:
                self.dir = 3


N, K = map(int, input().split())

chessboard = [list(map(int,input().split())) for _ in range(N)]
horses = []
for i in K:
    C,R,D = map(int, input().split())
    horse = Horse(C,R,D,str(i+1))
    horses.append(horse)

turn = 0
while turn <1000:
    for i in range(K):
        horses[i].move(N)





print(chessboard)
