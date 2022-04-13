import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
num = sys.stdin.readline().rstrip()
st = []

for i in num:
    while st and st[-1] < i and K > 0:
        st.pop()
        K -= 1
    st.append(i)

ans = []

if K > 0:
    for i in range(len(st)-K):
        ans.append(st[i])
else:
    for i in st:
        ans.append(i)

print("".join(ans))