# https://programmers.co.kr/learn/courses/30/lessons/42587

# 정답
from collections import deque

def solution(priorities, location):
    q = deque((idx, pri) for idx, pri in enumerate(priorities))
    max_pri, value = max(priorities), priorities[location]

    answer = []
    while q:
        idx, pri = q.popleft()
        if pri < max_pri:
            q.append((idx, pri))
            continue
        max_pri = 0
        for p in q:
            max_pri = max(max_pri, p[1])
        answer.append((idx, pri))
    
    return answer.index((location, value)) + 1    

priorities = [1, 1, 9, 1, 1, 1]	
location = 0
print(solution(priorities, location))
