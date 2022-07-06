# url x

# 정답
def solution(nums):
    answer = int(nums[0])
    
    for i in range(1, len(nums)):
        num = int(nums[i])
        if answer <= 1 or num <= 1:
            answer += num
        else:
            answer *= num

    return answer

nums = "567"
print(solution(nums))