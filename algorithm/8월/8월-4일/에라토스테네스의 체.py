import sys
sys.stdin = open('input.txt', 'r')


n, k = map(int, input().split())

arr = [1] * (n + 1)

cnt = 0

result = 0

for i in range(2, n + 1):

    if arr[i]:

        for j in range(1, n + 1):

            if i * j > n:
                break
            ## 변경 안됐으면 횟수 추가 후 변경
            if arr[i * j]:
                cnt += 1

                arr[i * j] = 0

            ## 변경 횟수가 같으면 나오기
            if cnt == k:
                result = i * j
                break

    if result:
        break


print(result)