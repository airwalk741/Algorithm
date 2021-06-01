import sys
sys.stdin = open('input (43).txt', 'r')


def eratos():

    for i in range(1, _max+1):
        if number[i]:
            k = 2
            while i * k < _max+1:
                number[i * k] = 0
                k += 1


n = int(input())
arr = list(map(int, input().split()))

_max = max(arr)

number = [1] * (_max+1)
number[0], number[1] = 0, 0
eratos()

result = 0

for i in arr:
    if number[i]:
        result += 1

print(result)





















