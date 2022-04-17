import sys
sys.setrecursionlimit(10 ** 6)

pre_order = []
while True:
    try:
        pre_order.append(int(sys.stdin.readline()))
    except:
        break

def post_order(start, end):
    if start > end:
        return
    root = pre_order[start]
    # 루트 왼쪽에만 자식이 있을 때
    if pre_order[end] <= root:
        post_order(start + 1, end)
        print(root)
        return
    # 오른쪽 자식이 시작되는 위치를 찾음
    for i in range(start + 1, end + 1):
        if pre_order[i] > root:
            idx = i
            break
    post_order(start + 1, idx -1)
    post_order(idx, end)
    print(root)

post_order(0, len(pre_order) - 1)