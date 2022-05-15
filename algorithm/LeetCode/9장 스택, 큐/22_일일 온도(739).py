# 실패
temperatures = [73,74,75,71,69,72,76,73]

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                left = stack.pop()
                answer[left] = i - left
            stack.append(i)
        return answer

print(Solution.dailyTemperatures(0, temperatures))