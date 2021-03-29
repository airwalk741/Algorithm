



n, k = map(int, input().split())

arr = list(map(int, input().split()))

cnt = 0

for i in range(n-2):
    for j in range(1+i, n-1):
        for x in range(2+i, n):
            if (arr[i] * arr[j] * arr[x]) % k == 0:
                cnt += 1

print(cnt)