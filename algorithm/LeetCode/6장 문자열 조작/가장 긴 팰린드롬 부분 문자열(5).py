# 시간초과 실패
s = "babad"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # answer = []
        # for i in range(len(s)):
        #     for j in range(1+i, len(s) + 1):
        #         temp = s[i:j]
        #         if temp == temp[::-1]:
        #             answer.append(temp)
        # return max(answer, key=len)

        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        for i in range(len(s) -1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
        return result
print(Solution.longestPalindrome(0, s))