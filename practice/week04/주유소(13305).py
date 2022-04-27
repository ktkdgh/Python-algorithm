import sys

n = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
city = list(map(int, sys.stdin.readline().split()))

cost = 0
temp = city[0]
for i in range(n-1):
    if city[i] < temp:
        temp = city[i]
    cost += temp * distance[i]
print(cost)