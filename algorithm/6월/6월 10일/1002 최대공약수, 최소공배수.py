import sys
sys.stdin = open('input (43).txt', 'r')


n = int(input())

nums = list(map(int, input().split()))

_min = min(nums)

sosu = [1] * (_min + 1)

sosu[0], sosu[1] = 0, 0

for i in range(2, _min):
    if sosu[i]:
        k = 2
        while i * k < _min + 1:
            sosu[i * k] = 0

            k += 1

i = 2
resMin = 1
resMax = 1
_max = max(nums)

while i <= _max:

    if not sosu[i]:
        i += 1
        continue

    check = 0

    for j in range(n):
        if nums[j] % i == 0:
            check += 1

    if check > 1:

        for j in range(n):
            if nums[j] % i == 0:
                nums[j] = nums[j] // i

    if check == n:
        resMin *= i


    if check > 1:
        resMax *= i

    if check == 0 or check == 1:
        i += 1

    _max = max(nums)


for num in nums:
    resMax *= num

print(resMin, resMax)










