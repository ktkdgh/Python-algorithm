# 두 포인터 풀이방식
# import sys

# n = int(sys.stdin.readline())
# x = list(map(int, sys.stdin.readline().split()))
# x.sort()

# start = 0
# end = len(x) -1
# answer = x[start] + x[end]
# pl = pr = 0
# while start <= end:
#     temp = x[start] + x[end]

#     if abs(temp) == abs(answer):
#         answer = temp        
#         pl = start
#         pr = end
#         if answer == 0:
#             break
#     if abs(temp) < 0:
#         start += 1
#     else:
#         end -= 1
        
# print(x[pl], x[pr])

# 이분 탐색
import sys

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
x.sort()
min = 2000000000

for i in range(n - 1):
    start = i + 1
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        temp = x[i] + x[mid]
        if abs(temp) < min:
            min = abs(temp)
            a, b = i, mid
        if temp < 0:
            start = mid + 1
        else:
            end = mid - 1
print(x[a], x[b])