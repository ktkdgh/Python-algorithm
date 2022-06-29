# https://programmers.co.kr/learn/courses/30/lessons/42586

# 정답
import collections

def solution(progresses, speeds):
    answer = []
    for progresses, speeds in zip(progresses, speeds):
        div, mod = divmod(100 - progresses, speeds)
        div = div + 1 if mod != 0 else div

        answer.append(answer[-1] if answer and answer[-1] > div else div)
    result = sorted(collections.Counter(answer).most_common(len(answer)), key=lambda x:x[0])

    return [i for _, i in result]
    
progresses = [95, 90, 99, 99, 80, 99]	
speeds = [1, 1, 1, 1, 1, 1]	
print(solution(progresses, speeds))