import sys

x, y, w, h = map(int, sys.stdin.readline().split())

min = x

if min > w-x:
    min = w-x
if min > y:
    min = y
if min > h-y:
    min = h-y

print(min)