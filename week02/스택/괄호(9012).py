import sys

n = int(sys.stdin.readline())
x = [sys.stdin.readline().strip() for _ in range(n)]

for i in x:
    flag = True
    stack = []
    for j in range(len(i)):
        if i[j] == '(':
            stack.append(i[j])
        else:
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
    if len(stack) == 0 and flag:
        print("YES")
    else:
        print("NO")
        

