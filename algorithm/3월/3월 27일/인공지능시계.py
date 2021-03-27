

h, m, s = map(int, input().split())

cou = int(input())

cou_h = cou // 3600
cou %= 3600
cou_m = cou // 60
cou_s = cou % 60

s += cou_s
m += cou_m
h += cou_h

if s >= 60:
    m += 1
    s %= 60

if m >= 60:
    h += 1
    m %= 60

h %= 24

print('{} {} {}'.format(h, m, s))
