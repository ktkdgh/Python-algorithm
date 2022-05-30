# 실패
import collections
tickets =  [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = collections.defaultdict(list)
        for left, right in sorted(tickets):
            graph[left].append(right)

        stack = []
        def dfs(str):
            while graph[str]:
                dfs(graph[str].pop(0))
            stack.append(str)
        
        dfs('JFK')
        return stack[::-1]

print(Solution.findItinerary(0, tickets))