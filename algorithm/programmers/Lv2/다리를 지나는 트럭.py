# https://programmers.co.kr/learn/courses/30/lessons/42583

# 틀림
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    running = [0 for _ in range(bridge_length)]
    
    while running:
        answer += 1
        running.pop(0)

        if truck_weights:
            if sum(running) + truck_weights[0] <= weight:
                running.append(truck_weights.pop(0))
            else:
                running.append(0)
    
    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))