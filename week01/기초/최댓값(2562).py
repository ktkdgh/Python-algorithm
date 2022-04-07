a = []

for i in range(1, 10):
    a.append(int(input()))

b = sorted(a)

for i in range(0,9):
    if b[8] == a[i]:
        print(b[8])
        print(i+1)


