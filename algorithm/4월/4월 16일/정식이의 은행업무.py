import sys
sys.stdin = open('input (43).txt', 'r')

T = int(input())


for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    b = list(input())
    t = list(input())

    b_change = []


    for i in range(len(b)):
        if b[i] == '0':
            b[i] = '1'
            b_change.append(int(''.join(b), 2))
            b[i] = '0'
        else:
            b[i] = '0'
            b_change.append(int(''.join(b), 2))
            b[i] = '1'

    for i in range(len(t)):
        if t[i] == '0':
            t[i] = '1'
            if int(''.join(t), 3) in b_change:
                print(int(''.join(t), 3))
                break
            t[i] = '2'
            if int(''.join(t), 3) in b_change:
                print(int(''.join(t), 3))
                break
            t[i] = '0'
        elif t[i] == '1':
            t[i] = '0'
            if int(''.join(t), 3) in b_change:
                print(int(''.join(t), 3))
                break
            t[i] = '2'
            if int(''.join(t), 3) in b_change:
                print(int(''.join(t), 3))
                break
            t[i] = '1'

        elif t[i] == '2':
            t[i] = '0'
            if int(''.join(t), 3) in b_change:
                print(int(''.join(t), 3))
                break
            t[i] = '1'
            if int(''.join(t), 3) in b_change:
                print(int(''.join(t), 3))
                break
            t[i] = '2'

