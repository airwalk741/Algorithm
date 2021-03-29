
s = input()
t = input()

if len(s) > len(t):
    s, t = t, s

t = t + t * len(s) # s: abab t: ababa


i = 0
k = 0
# t 길이까지
while i < len(t):
    # 다르면 나감
    if t[i] != s[k]:
        print('0')
        break
    else:
        k += 1
        i += 1
        # s길이 다 했으면 다시 0으로
        if k == len(s):
            k = 0

# break 안되고 나왔으면 같은 것
if i == len(t):
    print('1')