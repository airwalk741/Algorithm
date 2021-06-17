import sys
sys.stdin = open('input (43).txt', 'r')


box = [list(input()) for _ in range(5)]

maxLine = 0
# 최대 길이의 행 구하기
for line in box:
    maxLine = max(maxLine, len(line))

for i in range(maxLine):
    for j in range(5):
        # 열을 벗어나지 않으면 값 출력
        try:
            print(box[j][i], end='')
        # 벗어나면 다음 것
        except:
            print(end='')