import sys
sys.stdin = open('input.txt', 'r')


a = input()
b = input()

n = 0

while n < 10:

    try:
        a = a.replace(str(n), '')
    except:
        pass

    n += 1


if b in a:
    print(1)
else:
    print(0)