import sys
sys.stdin = open('input.txt', 'r')


## 입력이 몇개 들어오는 지 모른다.
try:
    while 1:
        s, t = input().split()


        result = 'Yes'

        j = 0
        s_length = len(s)
        t_length = len(t)

        for i in range(len(s)):

            # 앞부분 부터 순서대로 찾기
            while j < t_length:

                if s[i] == t[j]:
                    j += 1
                    break

                j += 1

            # t길이까지 갔다면 끝난건지 아닌지 체크하기
            if j == t_length and i <= s_length - 1:
                if s[i] != t[j - 1]:
                    result = 'No'
                break

        print(result)
except:
    pass








