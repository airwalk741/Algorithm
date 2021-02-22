import sys
sys.stdin = open('input (3).txt', 'r')


T = int(input())

for tc in range(1, T+1):

    s = [0] * 14
    d = [0] * 14
    h = [0] * 14
    c = [0] * 14

    arr = input()

    for i in range(0, len(arr), 3):

        if arr[i] == 'S':
            s[int(arr[i+1:i+3])] += 1
        elif arr[i] == 'D':
            d[int(arr[i+1:i+3])] += 1
        elif arr[i] == 'H':
            h[int(arr[i+1:i+3])] += 1
        elif arr[i] == 'C':
            c[int(arr[i+1:i+3])] += 1


    if 2 in s or 2 in d or 2 in h or 2 in c:
        print('#{} ERROR'.format(tc))
        continue

    print('#{} {} {} {} {}'.format(tc, s.count(0)-1, d.count(0)-1, h.count(0)-1, c.count(0)-1))



