import sys
sys.stdin = open('input (43).txt', 'r')


n = int(input())

balls = list(input())

result = 0

if balls[0] != balls[-1]:

    front_cnt = 0
    front_check = 1
    back_cnt = 0
    back_check = 1
    front_color = balls[0]
    back_color = balls[-1]
    for i in range(n):
        if front_color == balls[i]:
            if front_check:
                front_cnt += 1
        else:
            front_check = 0

        if back_color == balls[n - 1 - i]:
            if back_check:
                back_cnt += 1
        else:
            back_check = 0

        if not front_check and not back_check:
            break

    front_color_full = balls.count(front_color)
    back_color_full = n - front_color_full

    result = min(front_color_full - front_cnt, back_color_full - back_cnt)

else:

    front_cnt = 0
    front_check = 1
    back_cnt = 0
    back_check = 1
    color = balls[0]
    for i in range(n):
        if color == balls[i]:
            if front_check:
                front_cnt += 1
        else:
            front_check = 0

        if color == balls[n - 1 - i]:
            if back_check:
                back_cnt += 1
        else:
            back_check = 0

        if not front_check and not back_check:
            break

    full_cnt = balls.count(color)

    if n == back_cnt:
        pass
    elif back_cnt == front_cnt:
        result = full_cnt - back_cnt
    elif back_cnt > front_cnt:
        result = full_cnt - back_cnt
    else:
        result = full_cnt - full_cnt



print(result)






