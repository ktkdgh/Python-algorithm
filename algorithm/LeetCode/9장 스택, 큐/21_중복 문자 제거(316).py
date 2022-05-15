# 실패
import collections

s = "cbacdcbc"

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack, counter = [], collections.Counter(s)
        
        for word in s:
            counter[word] -= 1
            if word in stack:
                continue
            while stack and stack[-1] > word and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(word)
        
        return ''.join(stack)
print(Solution.removeDuplicateLetters(0, s))