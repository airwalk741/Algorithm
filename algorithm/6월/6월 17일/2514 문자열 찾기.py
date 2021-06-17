import sys
sys.stdin = open('input (43).txt', 'r')


koi = 0
ioi = 0


ch = input()

for i in range(len(ch)-2):
    if ch[i:i+3] == 'KOI':
        koi += 1
        continue

    if ch[i:i+3] == 'IOI':
        ioi += 1

print(koi)
print(ioi)