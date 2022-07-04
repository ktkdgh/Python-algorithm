# https://www.acmicpc.net/problem/11816

# 정답
import sys

num = sys.stdin.readline()

if '0x' in num:
    print(int(num, 16))
elif num[0] == '0':
    print(int(num, 8))
else:
    print(int(num))
