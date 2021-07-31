import sys
sys.stdin = open('input.txt', 'r')


for _ in range(500):


    secure = input()

    if secure == 'END':
        break


    secure = list(secure)

    secure.reverse()

    print(''.join(secure))


