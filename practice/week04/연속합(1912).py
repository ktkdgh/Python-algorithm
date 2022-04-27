import sys

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
hap = [s[0]]

for i in range(len(s) - 1):
    hap.append(max(hap[i] + s[i+1], s[i+1]))
print(max(hap))