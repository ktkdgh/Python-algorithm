# 실패
s = "pwwkew"

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        word = {}
        max_length = start = 0

        for idx, char in enumerate(s):
            if char in word and start <= word[char]:
                start = word[char] + 1
            else:
                max_length = max(max_length, idx - start + 1)
            word[char] = idx
        return max_length

print(Solution.lengthOfLongestSubstring(0, s))