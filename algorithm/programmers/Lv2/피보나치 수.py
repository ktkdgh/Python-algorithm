# https://programmers.co.kr/learn/courses/30/lessons/12945

# 정답
import sys
sys.setrecursionlimit(10**6)

def solution(n):
    answer = [0] * (n + 1)

    def fibo(x):
        if x == 1 or x == 2:
            return 1
        if answer[x] != 0:
            return answer[x]
        
        answer[x] = fibo(x-1) + fibo(x-2)
        return answer[x]

    return fibo(n) % 1234567

n = 51212
print(solution(n))