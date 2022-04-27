import sys

n = int(sys.stdin.readline())
stone = [(0, 0, 0, 0)]

for i in range(1, n+1):
    b, h, w = map(int, sys.stdin.readline().split())
    stone.append((i, b, h, w))
stone.sort(key=lambda x:x[3])

dp = [0] * (n+1)
for i in range(1, n+1):
    for j in range(i):
        if stone[i][1] > stone[j][1]:
            dp[i] = max(dp[i], dp[j] + stone[i][2])

max_h = max(dp)
idx = dp.index(max_h)
answer = []
while idx != 0:
    if max_h == dp[idx]:
        answer.append(stone[idx][0])
        max_h -= stone[idx][2]
    idx -= 1
    
print(len(answer))
print(*answer[::-1], sep='\n') 