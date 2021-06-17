import sys
sys.stdin = open('input (43).txt', 'r')

def select(idx, cnt, arr):
    global day

    if len(arr) == cnt:
        _sum = 1

        for k in arr:
            _sum *= group[k]

        day += _sum

    else:

        for i in range(idx, len(clothGroup)):

            if clothGroup[i] not in arr:
                arr.append(clothGroup[i])
                select(idx + 1, cnt, arr)
                arr.pop()





for _ in range(int(input())):

    n = int(input())

    group = {}
    clothGroup = []

    for _ in range(n):

        cloth, clothType = input().split()

        if clothType not in group:
            group[clothType] = 1
            clothGroup.append(clothType)
        else:
            group[clothType] += 1


    day = 0

    for i in range(1, len(clothGroup) + 1):

        select(0, i, [])

    print(day)

