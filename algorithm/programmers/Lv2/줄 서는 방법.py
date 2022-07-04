# https://programmers.co.kr/learn/courses/30/lessons/12936

# 틀림
import math

def solution(n, k):
    arr = [i for i in range(1, n+1)]
    answer = []
    while n > 0:
        n -= 1
        fac = math.factorial(n)
        div, mod = divmod(k, fac)
        if mod == 0:
            div -= 1
        answer.append(arr.pop(div))
        k = mod
    return answer

n = 3
k = 5
print(solution(n, k))