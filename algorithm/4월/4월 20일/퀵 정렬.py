import sys
sys.stdin = open('input (43).txt', 'r')


def quick(arr, l, r):
    if l < r:
        s = partition(arr, l, r)
        quick(arr, l, s-1)
        quick(arr, s+1, r)

    return arr

def partition(arr, l, r):

    p = arr[l]
    i = l
    j = r
    while i <= j:
        while i < len(arr) and arr[i] <= p:

            i += 1

        while i <= j and arr[j] >= p:

            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[l], arr[j] = arr[j], arr[l]

    return j


T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    n = int(input())

    arr = list(map(int, input().split()))

    arr = quick(arr, 0, len(arr)-1)

    print(arr[n//2])