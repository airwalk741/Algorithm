import sys
sys.stdin = open('input (43).txt', 'r')


def first():

    for i in range(1, n+1):
        print('*' * i)

def second():

    for i in range(n, 0, -1):
        print('*' * i)

def third():

    m = (n - 1) * 2 + 1

    k = n - 1

    for j in range(1, m+1, 2):
        for i in range(m+1):

            if i == 0:
                print(end='')
            elif i < k + 1:
                print(end=' ')
            else:
                if j:
                    print('*', end='')
                    j -= 1
                else:
                    break
        k -= 1

        print()


n, m = map(int, input().split())

if 0 < n < 101 and 0 < m < 4:

    if m == 1:
        first()
    elif m == 2:
        second()
    else:
        third()

else:
    print("INPUT ERROR!")
