import sys
sys.stdin = open('input (43).txt', 'r')

T = int(input())

for tc in range(1, T+1):

    print('#{}'.format(tc), end=' ')

    n = int(input())

    container = []

    for _ in range(n):

        s, e = map(int, input().split())

        container.append((s, e))


    container.sort(key= lambda x : x[1])

    result = 0

    e = 0

    for nextStart, nextEnd in container:

        if e <= nextStart:
            e = nextEnd
            result += 1

        if e == 24:
            break

    print(result)



