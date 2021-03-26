
from sys import stdin

for _ in range(3):

    n = int(input())

    result = 0

    for i in range(n):
        result += int(stdin.readline())


    if result == 0:
        print('0')
    elif result > 0:
        print('+')
    else:
        print('-')