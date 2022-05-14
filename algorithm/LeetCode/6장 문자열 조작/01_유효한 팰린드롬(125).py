# 정답
s = "A man, a plan, a canal: Panama"

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 입력받은 문자열에 공백 제거 후 소문자로 새로운 배열에 넣는다.
        strs = []
        for word in s:
            if word.isalnum():
                strs.append(word.lower())
        
        # 문자열 슬라이싱을 이용해 비교
        if strs != strs[::-1]:
            return False
        return True

print(Solution.isPalindrome(0, s))