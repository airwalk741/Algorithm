import sys

sys.stdin = open('input (9).txt', 'r')

def select(arr):

    for i in range(len(arr)-1):
        arr_min = i
        for j in range(i, len(arr)):
            if arr[arr_min] > arr[j]:
                arr_min = j
        arr[arr_min], arr[i] = arr[i], arr[arr_min]

    return arr

T = int(input())

for tc in range(1, T + 1):
    print('#{}'.format(tc), end=' ')
    n, m, k = map(int, input().split())

    arr = list(map(int, input().split()))

    # 사람 오는 시간 정렬
    select(arr)

    cnt = 0
    j = 0
    # 시간초 ( 0초부터 마지막 오는 사람 시간까지)
    for i in range(arr[-1]+1):
        # 0초가 아니면
        if i != 0:
            # 붕어빵 만드는 시간마다 붕어빵 만드는 개수 k만큼 늘려준다.
            if i % m == 0:
                cnt += k
        # i(시간초) j(차례로 오는 손님)
        if i == arr[j]:
            cnt -= arr.count(arr[j]) # 동시에 오는 손님을 카운트해서 붕어빵 빼준다.
            if cnt < 0: # 다 뻈는데 음수면 붕어빵 부족했던 것
                print('Impossible')
                break
            else:
                j += arr.count(arr[j]) # 동시에 온 손님만큼 j인덱스 늘려서 다음시간에 오는 손님 맞이
    else: # break 안걸리면 출력
        print('Possible')

