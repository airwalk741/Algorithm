

h, m = map(int, input().split())

cous = int(input())

cous_h = int(cous // 60)
cous_m = int(cous % 60)

m = (m + cous_m)

if m >= 60:
    m %= 60
    h += 1
h = (h + cous_h) % 24


print('{} {}'.format(h, m))

