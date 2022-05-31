# 실패
import collections
import heapq

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        distance = collections.defaultdict(int)

        for i in range(len(times)):
            a, b, c = times[i]
            graph[a].append((b, c))

        def dijkstra(start):
            q = []
            heapq.heappush(q, (0, start))
            while q:
                dist, now = heapq.heappop(q)
                if now not in distance:
                    distance[now] = dist
                    for i, j in graph[now]:
                        cost = dist + j
                        heapq.heappush(q, (cost, i))
        dijkstra(k)

        if len(distance) == n:
            return max(distance.values())
        return -1

print(Solution.networkDelayTime(0, times, n, k))