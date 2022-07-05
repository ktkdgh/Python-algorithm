# url x

# 틀림
def solution(adventurer):
    answer = 0
    count = 0
    adventurer.sort()

    for i in adventurer:
        count += 1
        if count >= i:
            answer += 1
            count = 0

    return answer

adventurer = [2, 3, 1, 2, 2]
print(solution(adventurer))