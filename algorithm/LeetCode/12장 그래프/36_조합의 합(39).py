# 실패
candidates = [2,3,6,7,9,10,11]
target = 7

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def dfs(sum, index, temp):
            if sum == 0:
                result.append(temp)
                return
            if sum < 0:
                return
            for i in range(index, len(candidates)):
                dfs(sum - candidates[i], i, temp + [candidates[i]])
        
        dfs(target, 0, [])
        return result

print(Solution.combinationSum(0, candidates, target))