# 정답
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m, n = len(grid[0]), len(grid)
        dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
        visited = [[0 for _ in range(m)] for _ in range(n)]

        def dfs(x, y):
            visited[x][y] = 1
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    if grid[nx][ny] == '1':
                        dfs(nx, ny)

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i, j)
                    cnt += 1
        return cnt

print(Solution.numIslands(0, grid))