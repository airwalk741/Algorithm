import sys
sys.stdin = open('input.txt', 'r')

moum = {'a', 'e', 'i', 'o', 'u'}

while 1:

    string = input()

    if string == 'end':
        break

    moum_cnt = 0 ## 모음 개수 체크
    m_cnt = 0 ## 연속 3개 모음 체크
    j_cnt = 0 ## 연속 3개 자음 체크

    success = True ## 적절한 암호문인지

    for i in range(len(string)):


        if i < len(string) - 1:
            if string[i] == string[i + 1]:
                if string[i] not in {'e', 'o'}: # 2번 연속이 e, o  아니면 false
                    success = False
                    break


        if string[i] not in moum:  ## 모음 자음 3개 연속인지 체크하는 것
            if m_cnt:
                j_cnt = 1
                m_cnt = 0
            else:
                j_cnt += 1
        else:
            if j_cnt:
                m_cnt = 1
                j_cnt = 0
            else:
                m_cnt += 1

            moum_cnt += 1

        if j_cnt > 2 or m_cnt > 2:
            success = False
            break


    else:
        # 모음 없으면 false
        if not moum_cnt:
            success = False

    if success:
        print('<' + string + '>'+' is acceptable.')
    else:
        print('<' + string + '>'+' is not acceptable.')