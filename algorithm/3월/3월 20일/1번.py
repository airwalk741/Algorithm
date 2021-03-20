import sys

sys.stdin = open('input (43).txt', 'r')


def deli(idx):
    global result

    if idx < len(arr):
        if arr[idx] == '1':
            if idx == len(arr) - 1:
                result += 1


    if idx + 1 < len(arr):
        if arr[idx + 1] != '0':
            deli(idx + 1)
    if idx + 2 < len(arr):
        if arr[idx + 2] != '0':
            deli(idx + 2)


T = int(input())

for tc in range(1, 1 + T):
    n = int(input())

    arr = list(input())

    result = 0

    deli(0)

    print(result)
