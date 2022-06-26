# https://programmers.co.kr/learn/courses/30/lessons/42885

# 정답
from collections import deque

def solution(people, limit):
    answer = 0
    queue = deque(sorted(people))

    while queue:
        if len(queue) == 1:
            answer += 1
            break
        if queue[0] + queue[-1] <= limit:
            queue.pop()
            queue.popleft()
        else:
            queue.pop()
        answer += 1

    return answer

people = [70, 80, 50, 40]
limit = 100
print(solution(people, limit))