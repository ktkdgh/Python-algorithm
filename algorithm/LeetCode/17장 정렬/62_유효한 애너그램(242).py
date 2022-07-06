# 정답
s = "anagram"
t = "nagaram"
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

print(Solution.isAnagram(0, s, t))