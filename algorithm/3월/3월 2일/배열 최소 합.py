import sys

sys.stdin = open('input (43).txt', 'r')

def perm(idx):

    if idx == n:
        if lst not in result:
            result.append(list(lst))
    else:
        for i in range(idx, n):

            lst[i], lst[idx] = lst[idx], lst[i]
            perm(idx+1)
            lst[i], lst[idx] = lst[idx], lst[i]

    return result

T = int(input())

for tc in range(1, T+1):

    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]
    lst = [i for i in range(n)]
    result = []
    perm(0)


    _min = 987654321

    for i in range(len(result)):
        total = 0
        for j in range(n):
            total += arr[j][result[i][j]]

            if total >= _min:
                break
        if total < _min:
            _min =total

    print(_min)

