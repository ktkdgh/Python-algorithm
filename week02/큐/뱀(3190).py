from collections import deque
import sys

n = int(sys.stdin.readline())
matrix = [[0] * n for _ in range(n)] # 맵크기

# 사과 위치 저장
for _ in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x-1][y-1] = 1

# 방향 변경 저장
change = {}
for _ in range(int(sys.stdin.readline())):
    x, c = sys.stdin.readline().split()
    change[int(x)] = c

# 뱀 시작 위치
snake = deque([[0, 0]])

# 상 좌 하 우
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 초기값
d = 1
time = 0
nx = ny = 0

# 맵 범위 체크 함수
def boundary_check(x, y):
    return True if 0 <= x and x < n and 0 <= y and y < n else False

# 방향 전환 함수
def change_direction(direction):
    global d
    if direction == "D":
        d = (d+1) % 4
    else:
        d = (d-1) % 4
    return d

while True:
    time += 1
    nx += dx[d]
    ny += dy[d]

    # 방향 전환
    if time in change.keys():
        d = change_direction(change[time])
    
    if boundary_check(nx, ny):
        # 몸에 부딪히는 경우
        if [nx, ny] in snake:
            break

        # 다음 위치에 사과가 있는 경우 
        if matrix[nx][ny] == 1:
            matrix[nx][ny] == 0
            snake.append([nx, ny])

        elif matrix[nx][ny] == 0:
            snake.append([nx, ny])
            x, y = snake.popleft()
    else:
        break

print(time)