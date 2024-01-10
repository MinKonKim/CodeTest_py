import sys
sys.stdin = open("../input.txt","r")

def  calculate( num1, num2, symbol):
    num1 = int(num1)
    num2 = int(num2)
    if symbol == '+':
        return num1 + num2
    elif symbol == '-':
        return num1 - num2
    elif symbol == '*':
        return num1 * num2


def solve(idx, value):
    global answer
    if idx >= N - 2:
        answer = max(answer, value)
        return
    solve(idx + 2, calculate(value, formula[idx + 2], formula[idx + 1]))
    if idx + 4 < N:
        solve(idx + 4,calculate(value, calculate( formula[idx + 2], formula[idx + 4], formula[idx + 3]), formula[idx + 1]))


N = int(input())
formula = input()
answer = -2**31
solve(0,int(formula[0]))
print(answer)

