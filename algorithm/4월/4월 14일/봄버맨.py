import sys
sys.stdin = open('input (43).txt', 'r')


def pr(arr):

    for i in range(r):
        for j in range(c):
            print('{}'.format(arr[i][j]), end='')
        print()

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

r, c, n = map(int, input().split())

# 처음 폭탄의 위치
arr = [list(input()) for _ in range(r)]

# 폭탄 가득 찬 것
boom = [['O'] * c for _ in range(r)]

# 처음 폭탄 터지기
fake_arr = [['O'] * c for _ in range(r)]

# 또 터지기
fake_arr2 = [['O'] * c for _ in range(r)]

# 처음 폭탄 터지기
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'O': # 처음 폭탄의 위치만 터져야함
            fake_arr[i][j] = '.'
            for k in range(4): # 상우하좌
                x = i + dr[k]
                y = j + dc[k]
                if -1 < x < r and -1 < y < c:
                    fake_arr[x][y] = '.' # 터진걸로 체크

for i in range(r):
    for j in range(c):
        if fake_arr[i][j] == 'O':
            fake_arr2[i][j] = '.'
            for k in range(4):
                x = i + dr[k]
                y = j + dc[k]
                if -1 < x < r and -1 < y < c:
                    fake_arr2[x][y] = '.'


# n %= 4 # 4개의 장면으로 바뀜

if n == 1:
    pr(arr) # 처음 폭탄 들어온것
elif n % 2 == 0:
    pr(boom) # 폭탄 가득한것
else:
    n = n // 2
    if n % 2:
        pr(fake_arr) # 폭탄 터진 것
    else:
        pr(fake_arr2)







