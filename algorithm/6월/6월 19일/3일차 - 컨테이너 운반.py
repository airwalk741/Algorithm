import sys
sys.stdin = open('input (43).txt', 'r')

T = int(input())

for tc in range(1, T+1):

    print('#{}'.format(tc), end=' ')

    n, m = map(int, input().split())

    weight = list(map(int, input().split()))

    truck = list(map(int, input().split()))

    result = 0

    # 최댓값 찾는 것이기때문에 내림차순으로 정렬
    weight.sort(reverse=True)
    truck.sort(reverse=True)

    k = 0

    for i in range(len(truck)):

        while True:

            if k == n:
                break

            # i 트럭에 맞는 가장 큰 화물을 찾고 나간다.
            if weight[k] <= truck[i]:
                result += weight[k]
                k += 1
                break

            k += 1

        if k == n:
            break

    print(result)

