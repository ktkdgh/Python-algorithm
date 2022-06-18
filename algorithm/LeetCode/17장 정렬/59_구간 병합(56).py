# 정답
intervals = [[1,3],[2,6],[8,10],[15,18]]
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        merged = []
        for i in sorted(intervals, key = lambda x: x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += i,
        
        return merged
print(Solution.merge(0, intervals))