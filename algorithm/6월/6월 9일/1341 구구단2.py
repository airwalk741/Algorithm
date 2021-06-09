import sys
sys.stdin = open('input (43).txt', 'r')



s, e = map(int, input().split())

if s <= e:

    for i in range(s, e+1):
        for j in range(1, 10):
            if len(str(i*j)) == 1:
                print('{} * {} =  {}'.format(i, j, i * j), end='   ')
            else:
                print('{} * {} = {}'.format(i, j, i * j), end='   ')

            if not j % 3:
                print()
        print()
else:
    for i in range(s, e-1, -1):
        for j in range(1, 10):
            if len(str(i * j)) == 1:
                print('{} * {} =  {}'.format(i, j, i * j), end='   ')
            else:
                print('{} * {} = {}'.format(i, j, i * j), end='   ')

            if not j % 3:
                print()
        print()