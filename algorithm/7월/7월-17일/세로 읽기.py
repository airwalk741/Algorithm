import sys
sys.stdin = open('input.txt', 'r')


strings = []
max_length = 0
for _ in range(5):

    string = input()
    strings.append(string)

    max_length = max(max_length, len(string))


# 없다면 pass
for i in range(max_length):
    for j in range(5):

        try:
            print(strings[j][i], end='')
        except:
            pass