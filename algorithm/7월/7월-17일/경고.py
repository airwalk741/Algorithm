import sys
sys.stdin = open('input.txt', 'r')


first = list(map(int, input().split(':'))) # 현재 시간
second = list(map(int, input().split(':'))) # 나중 시간

# 초 단위는 60초이므로 + 60
if first[2] > second[2]:
    s = second[2] - first[2] + 60
    second[1] -= 1

else:
    s = second[2] - first[2]

s = str(s)

if len(s) == 1:
    s = '0' + s

# 분 단위는 60초이므로 + 60
if first[1] > second[1]:
    m = second[1] - first[1] + 60
    second[0] -= 1
else:
    m = second[1] - first[1]


m = str(m)

if len(m) == 1:
    m = '0' + m

# 시 단위는 24초이므로 + 24
if first[0] > second[0]:
    h = second[0] - first[0] + 24
else:
    h = second[0] - first[0]


h = str(h)

if len(h) == 1:
    h = '0' + h

# 시간이 같다면 문제에서 최소 1초 기다려야한다고 했으므로 24시간을 출력
if not int(s) and not int(m) and not int(h):
    print('24:00:00')

else:
    print(':'.join([h, m, s]))

