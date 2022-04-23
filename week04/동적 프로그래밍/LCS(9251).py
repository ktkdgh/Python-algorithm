import sys

string_a = [0] + list(sys.stdin.readline().strip())
string_b = [0] + list(sys.stdin.readline().strip())

dp = [[0] * len(string_b) for _ in range(len(string_a))]
for i in range(len(string_a)):
    for j in range(len(string_b)):
        if i == 0 or j == 0:
            dp[i][j] == 0
        elif string_a[i] == string_b[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])