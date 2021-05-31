import sys
sys.stdin = open('input (43).txt', 'r')

input = sys.stdin.readline

T = int(input())

for _ in range(T):

    text = list(input().rstrip())

    result = []

    for _ in range(len(text)):

        check = text.pop()

        if check == ')':
            result.append(check)
        else:
            try:
                result.pop()
            except:
                print('NO')
                break
    else:
        if result:
            print('NO')
        else:
            print('YES')





























