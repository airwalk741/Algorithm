import sys
sys.stdin = open('input (43).txt', 'r')




while True:

    ch = list(input().split())

    repeat = {}

    if ch[0] == 'END':
        break

    # 반복 횟수 체크 하기
    for i in range(len(ch)):
        if ch[i] not in repeat:
            repeat[ch[i]] = 1
        else:
            repeat[ch[i]] += 1


    result = []

    # sort 함수 사용하기 위해 리스트로 바꾸기
    for k, v in repeat.items():
        result.append((k, v))

    result.sort() # 알파벳 순 정렬

    # 출력
    for k, v in result:
        print('{} : {}'.format(k, v))

