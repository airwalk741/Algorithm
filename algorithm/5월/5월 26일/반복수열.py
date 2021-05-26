import sys
sys.stdin = open('input (43).txt', 'r')

check = 0
num, p = input().split()
result = [int(num)]
perm = []

while True:

    number = 0

    for i in range(len(num)):
        number += int(num[i]) ** int(p)

    if number not in result:
        result.append(number)
    else:
        check = 1

    if check == 1:
        if number not in perm:
            perm.append(number)
        else:
            check += 1

    if check == 2:
        break

    num = str(number)


print(len(result) - len(perm))



