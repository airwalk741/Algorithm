import sys
sys.stdin = open('input (43).txt', 'r')

check = 1

while check:

    s, e = map(int, input().split())

    if 1 < s < 10 and 1 < e < 10:
        check = 0


    if check:
        print('INPUT ERROR!')
        continue
    else:

        if s > e:

            for i in range(1, 10):
                for j in range(s, e-1, -1):
                    if len(str(i*j)) == 1:
                        print('{} * {} =  {}'.format(j, i, i*j), end='   ')
                    else:
                        print('{} * {} = {}'.format(j, i, i*j), end='   ')
                print()

        if s <= e:

            for i in range(1, 10):
                for j in range(s, e+1):
                    if len(str(i*j)) == 1:
                        print('{} * {} =  {}'.format(j, i, i*j), end='   ')
                    else:
                        print('{} * {} = {}'.format(j, i, i*j), end='   ')
                print()

