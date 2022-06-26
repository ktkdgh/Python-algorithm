# https://programmers.co.kr/learn/courses/30/lessons/42577

# 틀림
def solution(phone_book):
    answer = True
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            answer = False
    return answer

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))