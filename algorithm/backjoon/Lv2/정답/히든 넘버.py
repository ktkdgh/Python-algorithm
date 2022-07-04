# https://www.acmicpc.net/problem/8595

# 정답
import sys

n = int(sys.stdin.readline())
hidden_word = list(sys.stdin.readline().strip())

num = '0123456789'
hidden_num = ''

for i in hidden_word:
    hidden_num += i if i in num else ' '

print(sum(list(map(int, hidden_num.split()))))
