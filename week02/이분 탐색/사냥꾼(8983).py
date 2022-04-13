import sys

m, n, l = map(int, sys.stdin.readline().split())
m_location = list(map(int, sys.stdin.readline().split()))
animal = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
m_location.sort()

cnt = 0
for i in animal:
    start = 0
    end = m - 1
    while start <= end:
        mid = (start + end) // 2
        if abs(m_location[mid] - i[0]) + i[1] <= l:
            cnt += 1
            break
        if i[0] > m_location[mid]:
            start = mid +1
        else:
            end = mid -1
print(cnt)