# https://programmers.co.kr/learn/courses/30/lessons/12909

# 정답
def solution(s):
    result = []
    
    for i in s:
        if i == '(':
            result.append(i)
        else:
            if result and result[-1] == '(':
                result.pop()
            else:
                return False
    answer = False if result else True 
    return answer

s = "(()("
print(solution(s))