
arr = []

Y = 0
M = 0

n = int(input())

arr = list(map(int, input().split()))

# 통화 수 하나씩 받아오면서
# Y는 30초에 10원
# M은 60초에 15원
# Y는 1~29 -> 10원, 30~59 -> 20원
# M은 1~59 - > 15원, 60~119 -> 30원
for i in arr:

    if i < 30:
        Y += 10
    else:
        Y += (i // 30) * 10

        Y += 10
    if i < 60:
        M += 15
    else:
        M += (i // 60) * 15
        M += 15


if Y == M:
    print('Y M {}'.format(Y))
elif Y < M:
    print('Y {}'.format(Y))
else:
    print('M {}'.format(M))