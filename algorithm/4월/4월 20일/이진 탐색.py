import sys
sys.stdin = open('input (43).txt', 'r')

def search(s, e, num):
    global flag

    while True:

        if s > e:
            return 0

        m = (s + e) // 2

        if arr1[m] <= num:

            if arr1[m] == num:
                return 1

            if flag != 1:
                flag = 1
                s = m + 1
            else:
                return 0

        else:
            if flag != -1:
                flag = -1
                e = m - 1
            else:
                return 0


T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    n, g = map(int, input().split())

    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr1.sort()

    result = 0


    for i in range(g):
        if arr2[i] > arr1[(0 + n - 1) // 2]:
            flag = 1
        else:
            flag = 0

        result += search(0, n-1, arr2[i])

    print(result)
