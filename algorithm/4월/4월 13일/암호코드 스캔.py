import sys

sys.stdin = open('input (43).txt', 'r')

change = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

num_dic = {
    '112': 0,
    '122': 1,
    '221': 2,
    '114': 3,
    '231': 4,
    '132': 5,
    '411': 6,
    '213': 7,
    '312': 8,
    '211': 9,
}

T = int(input())

for tc in range(1, 1+T):
    print('#{}'.format(tc), end=' ')
    n, m = map(int, input().split())

    arr = [list(input()) for _ in range(n)]

    secure = []

    for i in range(n):
        code = ''
        for j in range(m):
            code += change[arr[i][j]]
        secure.append(code)

    n1, n2, n3 = 0, 0, 0 # 맨 마지막 1, 마지막에서 두번째 0, 두번째 1
    result = []
    res = []
    ans = 0

    for i in range(n):
        if '1' in secure[i]:
            if i > 0:
                if secure[i] == secure[i-1]:
                    continue
            for j in range(m*4-1, -1, -1):
                if n2 == 0 and n3 == 0 and secure[i][j] == '1':
                    n1 += 1
                elif n1 != 0 and n3 == 0 and secure[i][j] == '0':
                    n2 += 1
                elif n1 != 0 and n2 != 0 and secure[i][j] == '1':
                    n3 += 1
                elif n3 != 0 and secure[i][j] == '0':
                    _min = min(n1, n2, n3)
                    num = num_dic[str(n1//_min) + str(n2//_min) + str(n3//_min)]
                    res.append(num)
                    n1, n2, n3 = 0, 0, 0
                    if len(res) == 8:
                        if res not in result:
                            numver = 0
                            for k in range(8):
                                if k % 2:
                                    numver += res[k] * 3
                                else:
                                    numver += res[k]

                            if numver % 10 == 0:
                                ans += sum(res)
                            result.append(res)
                        res = []

    print(ans)






# print(bin(int('a',16))[2:].zfill(4))
