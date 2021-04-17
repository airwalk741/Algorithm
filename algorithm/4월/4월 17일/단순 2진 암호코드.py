import sys

sys.stdin = open('input (43).txt', 'r')


T = int(input())

for tc in range(1, 1+T):
    print('#{}'. format(tc), end=' ')
    n, m = map(int, input().split())

    arr = []

    for i in range(n):
        arr.append(input()) # str로 입력받기

    code = [0] * 8 # 암호 해독

    secure = '' # 암호

    for i in range(n):
        if '1' in arr[i]: # 열중에서 1이 있는 열 가져오기
            for j in range(m-1, -1, -1):
                if arr[i][j] == '1': # 맨뒤부터 접근해서 1인거 찾아 뒤에서부터 7 * 8개 슬라이싱
                    secure = arr[i][j-55:j+1]
                    # for k in range(55, -1, -1):
                    #     secure += arr[i][j-k]
                    break
            break

    idx = 0 # 해독 code index
    cnt = 0 # 암호 secure index

    while idx < 8:

        s = ''

        for i in range(cnt, cnt+7):
            s += secure[i]

        if s == '0001101':
            code[idx] = 0
        elif s == '0011001':
            code[idx] = 1
        elif s == '0010011':
            code[idx] = 2
        elif s == '0111101':
            code[idx] = 3
        elif s == '0100011':
            code[idx] = 4
        elif s == '0110001':
            code[idx] = 5
        elif s == '0101111':
            code[idx] = 6
        elif s == '0111011':
            code[idx] = 7
        elif s == '0110111':
            code[idx] = 8
        elif s == '0001011':
            code[idx] = 9

        cnt += 7
        idx += 1

    _sum = 0
    for i in range(len(code)):
        if i % 2:
            _sum += code[i]
        else:
            _sum += code[i] * 3

    if _sum % 10:
        print('0')
    else:
        print(sum(code))




