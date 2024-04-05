import sys

sys.stdin = open('C:\\CodeTest_py\\input.txt', "r")

A, B = input().split()


def Count(A,B,j):
    result = 0
    for i in range(j,len(A)):
            if A[i] == B[i]:
                result+=1
    return result

if A== B:
    print(len(A) - Count(A,B,0))
else :
    min =51
    for i in range(len(B)-len(A)):
        C = B[i,i+len(A)]
        print(C)