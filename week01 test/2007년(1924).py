import sys
x, y = map(int, sys.stdin.readline().split())
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
temp = y
for i in range(x):
    if x-1 > i:
        temp += month[i]
print(days[temp%7])