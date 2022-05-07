# 정답
s = ["h","e","l","l","o"]

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        return s

print(Solution.reverseString(0, s))