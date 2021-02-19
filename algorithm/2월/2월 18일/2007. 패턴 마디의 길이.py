import sys

sys.stdin = open('input (6).txt', 'r')

T = int(input())

for tc in range(1, T+1):


    string = input()
    a = '' # 반복 되는 단어 담을 변수

    # 문자열의 반만 탐색 -> 반 이상가면 어쩌피 반복 없음
    for i in range(len(string)//2):
        # a에 입력받은 글자 하나씩 추가하면서 a 뒤에부터 반복이 되는지 확인할 것이다.
        a += string[i]
        k = 0
        # 반복이 되는지 확인하는 구문
        for j in range(i+1, i+len(a)):

            if a[k] != string[j]:
                break
            k += 1
        # break를 만나지 않았으면 반복이 됐다는 뜻
        else:
            result = a
            if len(result) != 1:
                # 문자가 하나가 아니면 반복문을 나와서 최종 결과가 나온다.
                break

    print('#{}'.format(tc), end=' ')
    print(len(result))

