import sys, heapq

n, k = map(int, sys.stdin.readline().split())
queue = []
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline()))
coin = list(set(coin))  # 중복제거
coin.sort(reverse=True) # 내림차순 정렬
visited = [0 for _ in range(k+1)]
heapq.heappush(queue, (0, 0)) # 코인갯수, 합 0으로 초기화

def bfs():
    while queue:
        cnt, sum = heapq.heappop(queue)
        for i in coin:
            hap = sum + i
            if hap == k:
                return cnt + 1
            if hap < k and visited[hap] == 0: # 합이 k 보다 작고 방문하지 않았으면
                visited[hap] = 1
                heapq.heappush(queue, (cnt + 1, hap))

count = bfs()
if count:
    print(count)
else:
    print(-1)