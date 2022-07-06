# https://www.acmicpc.net/problem/1439

# 정답
import sys

nums = sys.stdin.readline().strip()
count1 = 0
count0 = 0

if nums[0] == '1':
    count1 += 1
else:
    count0 += 1

for i in range(len(nums)-1):
    if nums[i] != nums[i+1]:
        if nums[i+1] == '1':
            count1 += 1
        else:
            count0 += 1

print(min(count1, count0))