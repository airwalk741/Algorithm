import sys
sys.stdin = open('input (43).txt', 'r')

def search(idx_arr, res, cnt):

    if cnt == m:
        print(res)
    else:
        for i in range(n):

            if i not in idx_arr:
                idx_arr.append(i)
                search(idx_arr, res + arr[i] + ' ', cnt + 1)
                idx_arr.pop()



n, m = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

for i in range(n):
    arr[i] = str(arr[i])

search([], '', 0)