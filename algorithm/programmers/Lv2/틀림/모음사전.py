# https://programmers.co.kr/learn/courses/30/lessons/84512

# 틀림
from itertools import product

def solution(word):
    answer = []
    for i in range(1, 6):
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            answer.append(''.join(list(c)))
    
    answer.sort()
    return answer.index(word) + 1

word = "AAAAE"
print(solution(word))