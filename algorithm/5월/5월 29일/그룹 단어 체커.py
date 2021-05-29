import sys
sys.stdin = open('input (43).txt', 'r')


T = int(input())

result = 0

for _ in range(T):

    word = input()

    check = [word[0]]

    for i in range(1, len(word)):
        if word[i] == check[-1]:
            continue
        else:
            if word[i] in check:
                break
            else:
                check.append(word[i])
    else:
        result += 1


print(result)