import sys
sys.stdin = open('input (9).txt', 'r')


T = int(input())

for tc in range(1, T + 1):

    n = int(input())

    arr = list(map(int, input().split()))

    result = []

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            num = str(arr[i] * arr[j])
            if len(num) == 1:
                result += [int(num)]
                continue
            check = True
            k = 1
            num_min = num[0]
            while k < len(num):

                if int(num_min) <= int(num[k]):
                    num_min = num[k]
                    k += 1
                else:
                    check = False
                    break
            if check:
                result += [int(num)]


    print('#{}'.format(tc), end=' ')
    if len(result):
        print(max(result))
    else:
        print('-1')




