import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(tree)

result = 0
while start <= end:
    total = 0
    pc = (start + end) // 2
    for i in tree:
        if i > pc:
            total += i - pc
    if total < M:
        end = pc - 1
    else:
        result = pc
        start = pc + 1

print(result)