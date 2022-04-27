import sys

n, k = map(int, sys.stdin.readline().split())
eletronic = list(map(int, sys.stdin.readline().split()))
stack = []
cnt = 0

for i in range(k):
    if eletronic[i] in stack:
        continue
    if len(stack) < n:
        stack.append(eletronic[i])
        continue

    idxs = []
    falg = True
    for j in range(n):
        if stack[j] in eletronic[i:]:
            idx = eletronic[i:].index(stack[j])
        else:
            idx = 101
            falg = False
        idxs.append(idx)
        if not falg:
            break

    idx_out = idxs.index(max(idxs))
    del stack[idx_out]
    stack.append(eletronic[i])
    cnt += 1

print(cnt)