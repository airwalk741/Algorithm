import sys

sys.stdin = open('input (6).txt', 'r')

# 선택 정렬
def selection(arr):

    for i in range(len(arr)-1):
        arr_min = i
        for j in range(i, len(arr)):
            if arr[arr_min] > arr[j]:
                arr_min = j

        arr[i], arr[arr_min] = arr[arr_min], arr[i]
    return arr

for tc in range(1, 10+1):

    dump = int(input())

    arr = list(map(int, input().split()))
    # 정렬을 해서 가장 큰 숫자를 하나빼고
    # 가장 작은 숫자를 하나 더하면서 상자를 이동시킨다
    while dump > 0:

        selection(arr)
        arr[len(arr)-1] -= 1
        arr[0] += 1
        dump -= 1

    selection(arr)
    print('#{}'.format(tc), end=' ')
    print(arr[len(arr)-1]-arr[0])














