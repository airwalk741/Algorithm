import sys
sys.stdin = open('input (43).txt', 'r')

def dfs(idx, cnt, num):
    global result

    if idx == n:
        if result < cnt:
            result = cnt
        return

    if num <= arr[idx][0]: # 시작이 그 전 종료시점보다 크면
        dfs(idx+1, cnt, num) # 택하지 않고 다음으로 넘어가거나
        dfs(idx+1, cnt+1, arr[idx][1]) # 택해서 다음으로 넘어간다.
    else:# 시작이 그 전 종료시점보다 작으면
        dfs(idx+1, cnt, num) # 다음으로 넘어간다.

T = int(input())

for tc in range(1, 1+T):
    print('#{}'.format(tc), end=' ')
    n = int(input())

    arr = []

    for i in range(n):
        arr.append(list(map(int, input().split())))

    # 0번 index 오름차순으로 정렬하는데 같은거는 1번 index를 오름차순으로 정렬
    # arr.sort(key=lambda x: (x[0], x[1]))

    # 0번 index 오름차순으로 정렬
    arr.sort(key=lambda x: x[0])
    # print(arr)
    result = 0

    dfs(0, 0, 0)

    print(result)

