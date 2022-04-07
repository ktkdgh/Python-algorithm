a = []
b = [0 for _ in range(10)]
n = [int(input()) for _ in range(3)]

total = n[0] * n[1] * n[2]

for i in str(total):
    a.append(i)

for i in a:
    for j in range(10):
        if int(i) == j:
            b[j] += 1

for i in b:
    print(i)