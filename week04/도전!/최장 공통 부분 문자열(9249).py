import sys

str_a = [0] + list(sys.stdin.readline().strip())
str_b = [0] + list(sys.stdin.readline().strip())

dp = [[0 for _ in range(len(str_a))] for _ in range(len(str_b))]

for i in range(len(str_b)):
    for j in range(len(str_a)):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif str_b[i] == str_a[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = 0

max_length = 0

for i in dp:
    max_length = max(max_length, max(i))
    print(i)

print(max_length)