import sys
sys.stdin = open('input (43).txt', 'r')


def first():

    k = 2

    for i in range(1, n+1):
        if i <= n // 2 + 1:
            print('*' * i)
        else:
            print('*' * (i-k))
            k += 2

def second():

    k = n-1
    q = k

    for i in range(n):
        for j in range(n):

            if q <= j <= k:
                print('*', end='')
            else:
                print(end=' ')
        print()

        if i <= n//2 - 1:
            q -= 1
        else:
            q += 1


def third():

    k = 0

    for j in range(n):
        for i in range(n):

            if i < k or n - k <= i:
                print(end=' ')
                continue


            print('*', end='')


        if j < n // 2 + 1:
            k += 1
        else:
            k -= 1
        print()



def fourth():
    pass


n, m = map(int, input().split())



if 0 < n < 101 and 0 < m < 5:
    if n % 2:
        if m == 1:
            first()
        elif m == 2:
            second()
        elif m == 3:
            third()
        elif m == 4:
            fourth()
    else:
        print("INPUT ERROR!")

else:
    print("INPUT ERROR!")








