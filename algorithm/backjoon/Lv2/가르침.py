# https://www.acmicpc.net/problem/1062

# 틀림
from itertools import combinations
import sys

n, k = map(int, sys.stdin.readline().split())
data = [sys.stdin.readline().strip()[4:-4] for _ in range(n)]
first_word = {'a', 'n', 't', 'i', 'c'}
remain_alphabet = set(chr(i) for i in range(97, 123)) - first_word

def checkWords(data, learned):
    cnt = 0
    for word in data:
        canRead = 1
        for w in word:
            if learned[ord(w)] == 0:
                canRead = 0
                break
        if canRead == 1:
            cnt += 1
    return cnt

answer = 0
if k >= 5:
    learned = [0] * 123
    for x in first_word:
        learned[ord(x)] = 1

    for teach in list(combinations(remain_alphabet, k-5)):
        for t in teach:
            learned[ord(t)] = 1
        cnt = checkWords(data, learned)
        if cnt > answer:
            answer = cnt
        for t in teach:
            learned[ord(t)] = 0
    print(answer)
else:
    print(0)