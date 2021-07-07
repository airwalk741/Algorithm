import sys
sys.stdin = open('input (43).txt', 'r')


def search(res, cnt):

    if cnt == m:
        # 한번도 출력하지 않았다면 출력하고 출력했다고 result에 담아두기
        if res not in result:
            print(res)
            result.add(res)

    else:
        for i in range(n):

            search(res + arr[i] + ' ', cnt + 1)



n, m = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

arr = list(map(str, arr))

result = set()

search('', 0)


