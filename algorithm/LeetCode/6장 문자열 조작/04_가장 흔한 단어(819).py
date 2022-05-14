# 실패
import collections
import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit." 
banned = ["hit"]

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        answer = []
        for word in re.sub(r'[^\w]', ' ', paragraph).lower().split():
            if not word in banned:
                answer.append(word)

        cnt = collections.Counter(answer)
        return cnt.most_common(1)[0][0]


print(Solution.mostCommonWord(0, paragraph, banned))