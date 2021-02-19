import sys

sys.stdin = open('input (6).txt', 'r')

# T = int(input())

for tc in range(1, 10+1):

    n = int(input())

    arr = list(map(int, input().split()))
    count = 0
    for i in range(2, len(arr)-2):
        max_building = 0
        # 이 네개의 if문은 가장 양쪽 두개의 빌딩 중 가장 높은 빌딩을 찾는 것이다.
        if max_building < arr[i-2]:
            max_building = arr[i-2]
        if max_building < arr[i-1]:
            max_building = arr[i-1]
        if max_building < arr[i+2]:
            max_building = arr[i+2]
        if max_building < arr[i+1]:
            max_building = arr[i+1]
        # 기준이 되는 빌딩이 주위 빌딩 보다 높다면 조망권이 확보 되는 것이다.
        if arr[i] > max_building:
            count += arr[i] - max_building

    print('#{}'.format(tc), end=' ')
    print(count)

