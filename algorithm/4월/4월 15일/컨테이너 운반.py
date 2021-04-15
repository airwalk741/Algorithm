import sys
sys.stdin = open('input (43).txt', 'r')


T = int(input())

for tc in range(1, 1+T):
    print('#{}'.format(tc), end=' ')
    n, m = map(int, input().split())

    container = list(map(int, input().split()))

    truck = list(map(int, input().split()))

    result = 0
    # 화물과 트럭 내림차순
    container.sort(reverse=True)
    truck.sort(reverse=True)

    for i in range(n):
        for j in range(len(truck)):
            if container[i] <= truck[j]: # 트럭이 화물보다 크면
                result += container[i] # 화물을 더해주고
                truck.pop(0) # 그 트럭은 사용했기때문에 pop
                break

    print(result)