# 정답
from bisect import bisect_left

nums1, nums2 = [1,2,2,1], [2,2]
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = set()
        nums2.sort()

        for n1 in nums1:
            i2 = bisect_left(nums2, n1)
            if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
                result.add(n1)

        return result 

print(Solution.intersection(0, nums1, nums2))