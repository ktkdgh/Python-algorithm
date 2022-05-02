# 실패
import sys

def postorder(preorder, inorder):
    if preorder:
        root = preorder[0]
    
        for i, in_num in enumerate(inorder):
            if in_num == root:
                idx = i
                break

        postorder(preorder[1:idx+1], inorder[:idx])
        postorder(preorder[idx+1:], inorder[idx+1:])
        temp.append(root)

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    preorder = list(map(int, sys.stdin.readline().split()))
    inorder = list(map(int, sys.stdin.readline().split()))
    temp = []
    postorder(preorder, inorder)
    print(*temp)