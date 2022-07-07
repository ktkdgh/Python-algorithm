# https://www.acmicpc.net/problem/10815

# 정답
import sys

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
check_card = list(map(int, sys.stdin.readline().split()))

card.sort()
answer = []

for i in check_card:
    start = 0 
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        if card[mid] == i:
            answer.append(1)
            break
        elif card[mid] > i:
            end = mid - 1
        else:
            start = mid + 1
    else:
        answer.append(0)

print(*answer)