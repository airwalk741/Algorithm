import sys
sys.stdin = open('input (43).txt', 'r')

plate = input()

result = 10

for i in range(len(plate)-1):
    # 다음 그릇의 방향에 따라 높이가 다르게 더해진다.
    if plate[i] != plate[i+1]:
        result += 10
    else:
        result += 5

print(result)