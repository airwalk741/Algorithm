import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(2500)

## DFS 
def search(idx, cnt, arr):

    if cnt >= k:
        if cnt == k:
            res = ''.join(arr)
            if res not in result:
                result.add(res)
        return

    for i in range(idx, n):
        if cnt + coin[i] > k:
            break
        search(i, cnt + coin[i], arr + [str(coin[i])])


n, k = map(int, input().split())

coin = [int(input()) for _ in range(n)]
coin.sort()
result = set()

search(0, 0, [])

print(len(result))
