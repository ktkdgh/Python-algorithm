# 실패
import sys

def postorder(istart, iend, pstart, pend):
    if (istart > iend) or (pstart > pend):
        return
    
    parent = position[pend]
    position.append(parent)
    left = position[parent] - istart
    right = iend - position[parent]

    postorder(istart, iend - left, pstart, pend - left)   
    postorder(istart, right - iend, pstart, right - pend) 


for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    preorder = list(map(int, sys.stdin.readline().split()))
    inorder = list(map(int, sys.stdin.readline().split()))

    position = [0] * (n+1)
    for i in range(n):
        position[inorder[i]] = i

    postorder(0, n-1, 0, n-1)
    print(*position)