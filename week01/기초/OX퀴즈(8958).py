a = int(input())

b = [input() for _ in range(1, a+1)]

for i in range(0,a):
    cnt = 0
    total = 0
    c = list(b[i])
    for j in range(len(b[i])):
        if c[j] == 'O':
            cnt = cnt +1
            total = total + cnt
        else:
            cnt = 0;
    print(total)    