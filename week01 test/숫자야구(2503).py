import sys
import itertools

nPr = list(itertools.permutations([1,2,3,4,5,6,7,8,9], 3))
num = int(sys.stdin.readline())

for _ in range(num):
    game, s, b = map(int, sys.stdin.readline().split())
    game = list(str(game))
    remove_cnt = 0
    for i in range(len(nPr)):
        s_cnt = b_cnt = 0
        i -= remove_cnt
        for j in range(3):
            game[j] = int(game[j])
            if game[j] in nPr[i]:
                if j == nPr[i].index(game[j]):
                    s_cnt += 1
                else:
                    b_cnt += 1
        if s_cnt != s or b_cnt != b:
            nPr.remove(nPr[i])
            remove_cnt += 1
print(len(nPr))