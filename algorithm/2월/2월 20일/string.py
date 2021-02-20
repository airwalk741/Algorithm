import sys

sys.stdin = open('input (6).txt', 'r')

for tc in range(1, 11):

    t = int(input())
    search = input()
    string = input()

    count = 0
    i = 0 # 문장 인덱스
    j = 0 # 찾는 단어의 인덱스

    while i < len(string):
        # 글자 확인
        if string[i] == search[j]:
            i += 1
            j += 1
            # j가 search 길이만큼 된다면 찾는 단어 길이이므로 count + 1
            # 하나 찾았으니까 다시 j = 0
            if j == len(search):
                j = 0
                count += 1
        else:
            # 예를들어 tti 문장이고 찾는 단어가 ti 이면
            # 처음 tt에서 ti가 아니므로 다시 찾아야하는데
            # 그때 i 인덱스가 'i'로 가는 것을 방지
            # 밑에 else 부분만 쓰면 'i'부분으로 바로 간다.
            if j != 0 and string[i] == search[0]:
                j = 0
            else:
                i += 1
                j = 0

    print('#{}'.format(t), end=' ')
    print(count)



