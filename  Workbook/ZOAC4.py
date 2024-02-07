import sys
sys.stdin = open("../input.txt","r")

H, W, N, M = map(int, input().split())

col = H//(N+1) if H%(N+1) == 0 else H//(N+1)+1
row = W//(N+1) if W%(M+1) == 0 else W//(M+1)+1
print(col*row)


