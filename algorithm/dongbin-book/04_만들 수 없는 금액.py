# url x

# 틀림
def solution(coin):
    answer = 1
    coin.sort()

    for c in coin:
        if answer < c:
            break
        answer += c

    return answer

coin = [3, 2, 1, 1, 9]
print(solution(coin))