# https://programmers.co.kr/learn/courses/30/lessons/43165

# 틀림
def solution(numbers, target):
    answer = 0

    def dfs(idx, result):
        if idx == len(numbers):
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
    
    dfs(0, 0)
    return answer

numbers	= [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))