# 정답
import collections

jewels = "z"
stones = "ZZ"

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        stone = collections.Counter(stones)

        for i in range(len(jewels)):
            if jewels[i] in stone:
                cnt += stone[jewels[i]]
        return cnt

print(Solution.numJewelsInStones(0, jewels, stones))