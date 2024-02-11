import sys
sys.stdin = open('C:\\CodeTest_py\\input.txt', "r")

array =[]
def removeNumber(onecnt, zerocnt, s):
    if onecnt == 0 and zerocnt == 0:
        return
    
S = input()

oneCnt , zeroCnt = 0,0





for i in range(len(S)):
    if S[i] == '1':
        oneCnt +=1
    else:
        zeroCnt += 1

