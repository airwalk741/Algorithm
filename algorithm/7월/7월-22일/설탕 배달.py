import sys
sys.stdin = open('input.txt', 'r')


n = int(input())

result = -1

five = n // 5

while five != -1:

    num = n

    # 최소 개수를 구하는 것이기 때문에 5부터 나눠서 나머지를 구한다.
    num -= five * 5

    # 나머지가 0이면 break
    if not num:
        result = five
        break

    # 나머지를 3으로 나눴는데 0이라면 설탕의 무게와 같은 것
    if not num % 3:
        result = num // 3 + five
        break

    five -= 1

print(result)