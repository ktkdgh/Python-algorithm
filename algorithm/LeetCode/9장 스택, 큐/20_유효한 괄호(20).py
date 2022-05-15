# 정답
s = "()[]{}"

class Solution:
    def isValid(self, s: str) -> bool:
        # 내 풀이 47ms
        stack = []

        for valid in s:
            if valid == '(' or valid == '{' or valid == '[':
                stack.append(valid)
            else:
                if stack and valid == ')' and stack[-1] == '(':
                    stack.pop()
                elif stack and valid == '}' and stack[-1] == '{':
                    stack.pop()
                elif stack and valid == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True

        # 책 풀이 53ms
        # stack = []
        # table = {')':'(', '}':'{', ']':'['}

        # for char in s:
        #     if char not in table:
        #         stack.append(char)
        #     elif not stack or table[char] != stack.pop():
        #         return False
        # return len(stack) == 0

print(Solution.isValid(0, s))