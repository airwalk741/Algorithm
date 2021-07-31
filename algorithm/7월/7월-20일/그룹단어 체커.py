import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

n = int(input())

result = 0

for _ in range(n):

    string = input()

    repeat = set()

    repeat.add(string[0]) # 첫번째 알파벳 넣기

    for i in range(1, len(string)):

        # 알파벳이 존재 하지 않으면 담아두기
        if string[i] not in repeat:
            repeat.add(string[i])
        # 한번 나온 알파벳이였다면
        else:
            # 연속하면 괜찮지만 그게 아니라면 break
            if string[i] != string[i - 1]:
                break
    # 한번도 break 안되면 한 단어
    else:
        result += 1

print(result)



