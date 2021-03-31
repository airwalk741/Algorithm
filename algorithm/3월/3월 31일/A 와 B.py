import sys

sys.stdin = open('input (43).txt', 'r')



s = list(input())

t = list(input())

# A는 뒤에 추가하는 거기 때문에 t에서 A를 빼고 s와 같은지 비교
# B는 뒤집고 B는 추가하는 거기 때문에 t에서 B를 빼고 뒤집은 다음에 s와 같은지 비교

while len(s) != len(t):

    if t[-1] == 'A':
        t.pop()
        if s == t:
            print('1')
            break
    elif t[-1] =='B':
        t.pop()
        t.reverse()
        if s == t:
            print('1')
            break

if s != t:
    print('0')
