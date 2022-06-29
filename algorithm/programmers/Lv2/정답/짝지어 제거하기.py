# https://programmers.co.kr/learn/courses/30/lessons/12973

# 정답
def solution(s):
    stack = []
    for i in range(len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else :
            stack.append(s[i])
    answer = 1
    if stack:
        return 0
    return answer

s = 'baabaa'
print(solution(s))
