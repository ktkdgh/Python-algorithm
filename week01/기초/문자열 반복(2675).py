n = int(input())

x = [input().split() for _ in range(n)]

for i in range(n):
    for y in x[i][1]:
        print(y*int(x[i][0]), end='')
    print()  