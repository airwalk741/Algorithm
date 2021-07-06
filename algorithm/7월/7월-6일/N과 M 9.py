import sys
sys.stdin = open('input (43).txt', 'r')


def search(res, cnt):
    global result

    if cnt == m:
        # 중복인지 체크
        if res not in result:
            print(res)
            result.add(res)
    else:
        for i in range(n):

           if visited[i]:
                visited[i] = 0 # 방문체크
                search(res + arr[i] + ' ', cnt + 1)
                visited[i] = 1 # 방문체크 해제

n, m = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort() # 사전순으로 출력하기 위해 정렬

arr = list(map(str, arr))

result = set() # 중복으로 출력되는지 체크하기 위한 변수

visited = [1] * n

search('', 0)


