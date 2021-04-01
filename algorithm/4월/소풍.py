



n, k, m = map(int, input().split())


num = [i for i in range(1, n+1)]

idx = -1
cnt = 0
while len(num) > 2:

    cnt += 1
    idx += k

    q = len(num)

    if idx >= q:
        idx -= q
    if num[idx] == m:
        break

    num.pop(idx)
    idx -= 1

if len(num) == 2:
    print(cnt+2)
else:
    print(cnt)