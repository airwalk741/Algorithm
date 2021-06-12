import sys
sys.stdin = open('input (43).txt', 'r')

n = int(input())

nums = [int(input()) for _ in range(n)]

numMax = max(nums) // 2 + max(nums) + 1

isPrime = [1] * numMax

isPrime[1], isPrime[0] = 0, 0

for i in range(2, numMax):
    if isPrime[i]:
        k = 2
        while i * k < numMax:
            isPrime[i * k] = 0

            k += 1




for num in nums:
    res = []
    cnt = 987654321
    for i in range(num, -1, -1):
        if isPrime[i]:
            if num - i <= cnt:
                cnt = num - i
                res.append(i)
                break

    for i in range(num + 1, numMax):
        if isPrime[i]:
            if i - num <= cnt:
                if i -num == cnt:
                    res.append(i)
                else:
                    res = [i]
                break

        if i - num > cnt:
            break

    print(*res)



