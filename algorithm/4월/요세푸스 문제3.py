


n, k = map(int, input().split())


num = [i for i in range(1, n+1)]

idx = -1

while len(num) > 2:

    idx += k
    q = len(num)
    if idx >= q:
        idx -= q

    num.pop(idx)
    idx -= 1


print(num[1])
