import sys
sys.stdin = open('input (43).txt', 'r')


n, m = map(int, input().split())

if m == 2:
    print(bin(n)[2:])
elif m == 8:
    print(oct(n)[2:])
else:
    num = list(hex(n)[2:])

    for i in range(len(num)):

        try:
            print(int(num[i]), end='')
        except:
            print(chr(ord(num[i]) - 32), end='')






