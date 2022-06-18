# https://programmers.co.kr/learn/courses/30/lessons/42586

# 정답
import collections

def solution(progresses, speeds):
    ans, result = [], []
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            if result and result[-1] > ((100 - progresses[i]) // speeds[i]):
                result.append(result[-1])
            else:    
                result.append((100 - progresses[i]) // speeds[i])
        else:
            if result and result[-1] > (((100 - progresses[i]) // speeds[i]) + 1):
                result.append(result[-1])
            else:    
                result.append(((100 - progresses[i]) // speeds[i]) + 1)
    
    answer = sorted(collections.Counter(result).most_common(len(result)), key=lambda x:x[0])
    for _, i in answer:
        ans.append(i)
    return ans
    
    # 다른 풀이
    # def solution(progresses, speeds):
    # answer = []
    # div, mod = divmod(100 - progresses[0], speeds[0])
    # cmp = div + 1 if mod != 0 else div
    # cnt = 0
    # for progress, speed in zip(progresses[1:], speeds[1:]):
    #     div, mod = divmod(100 - progress, speed)
    #     div = div + 1 if mod != 0 else div
    #     cnt += 1
    #     if cmp < div:
    #         answer.append(cnt)
    #         cmp = div
    #         cnt = 0
    # else: answer.append(cnt+1)    
    # return answer
        
progresses = [95, 90, 99, 99, 80, 99]	
speeds = [1, 1, 1, 1, 1, 1]	
print(solution(progresses, speeds))