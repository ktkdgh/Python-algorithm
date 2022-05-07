# 실패
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]

class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letter, digit = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)

        letter.sort(key=lambda x:(x.split()[1:], x.split()[0]))
        return letter + digit

print(Solution.reorderLogFiles(0, logs))