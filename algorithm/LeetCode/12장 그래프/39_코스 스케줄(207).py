# 실패
import collections

numCourses = 2
prerequisites = [[1,0],[0,1]]

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        visited = set()
        traced = set()

        def dfs(i):
            if i in visited:
                return True
            if i in traced:
                return False
            
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            
            traced.remove(i)
            visited.add(i)
            return True
        
        for x in list(graph):
            if not dfs(x):
                return False
        
        return True

print(Solution.canFinish(0, numCourses, prerequisites))