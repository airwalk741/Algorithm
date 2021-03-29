



num = int(input())

f = 1
r = num

while True:

    mid = int((f + r) / 2)

    if mid * mid == num:
        print(mid)
        break

    if mid * mid > num:
        r = mid
    elif mid * mid < num:
        f = mid




