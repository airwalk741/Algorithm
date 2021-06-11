import sys
sys.stdin = open('input (43).txt', 'r')


def first():

    k = 1

    for i in range(1, n + 1):
        if i % 2:
            for _ in range(i):
                print(k, end=' ')
                k += 1
            print()
        else:
            fake = k
            fake += i - 1

            while k-1 != fake:

                print(fake, end=' ')
                fake -= 1

            k += i

            print()




def second():

    arr = [[-1] * (n * 2) for _ in range(n * 2)]

    for i in range(n * 2):
        for j in range(i, n * 2 - i - 1):
            arr[i][j] = i

    for i in range(n * 2):
        if sum(arr[i]) == -100:
            break
        for j in range(n * 2):
            if arr[i][j] != -1:
                print(arr[i][j], end=' ')
            else:
                print(end='  ')
        print()



def third():

    arr = [[0] * 100 for _ in range(100)]
    k = 1
    for i in range(n):
        for j in range(k - 1, n - k + 1):
            arr[j][i] = k

        k += 1

    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                print(arr[i][j], end=' ')
        print()



n, m = map(int, input().split())

if 0 < n < 101 and 0 < m < 4:
    if n % 2:
        if m == 1:
            first()
        elif m == 2:
            second()
        else:
            third()
    else:
        print("INPUT ERROR!")

else:
    print("INPUT ERROR!")