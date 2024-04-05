import sys
from itertools import permutations
sys.stdin = open('C:\\CodeTest_py\\input.txt', "r")

N = int(input())
A = list(map(int, input().split()))

max = 0


for arr in permutations(A,N):
    num = 0 
    for i in range(N-1):
        num += abs(arr[i]-arr[i+1])
    if num > max : max= num
print(max)


