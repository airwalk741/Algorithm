import sys
sys.stdin = open('input (43).txt', 'r')



arr = list(map(int, input().split()))



for num in arr:

    check = 0
    i = 1
    if num == 1:
        print('number one')
        continue
    while i * i <= num:

        if num == 1:
            print('number one')
            break

        if num % i == 0:
            check += 1

        if check > 1:
            print('composite number')
            break

        i += 1


    if check == 1:
        print('prime number')






