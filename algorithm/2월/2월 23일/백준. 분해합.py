import sys
sys.stdin = open('input (9).txt', 'r')


number = int(input())

i = 1
num_min = number # 최소값을 구하기 위해 number를 넣는다


# 기본값에서 하나씩 줄이면서 생성자를 찾을 것이다.
while i < number:

    num = number - i
    # 각 자리숫자의 최대가 9이기 때문에 9 * (자릿수)를 빼줘서
    # 불필요한 계산을 줄인다.
    if num < number - 9 * (len(str(number))):
        break
    # 나중에 최소 생성자를 담기위한 변수
    result = num

    total = num
    # 각 자리 수를 더하는 while문
    while num > 0:

        total += num % 10

        num = num // 10
        # total이 number 보다 크다면 구할 더 이상 더해줄 필요가 없기때문에 나간다.
        if total > number:
            break

    # 최소값 비교하는 if문
    if total == number:
        if num_min > num:
            num_min = result
    i += 1
# 만약 num_min이 그대로면 생성자가 없는 것이기때문에 0을 넣어준다.
if num_min == number:
    num_min = 0

print(num_min)




