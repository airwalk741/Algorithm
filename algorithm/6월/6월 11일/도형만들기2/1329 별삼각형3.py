import sys
sys.stdin = open('input (43).txt', 'r')


n = int(input())

if 0 < n < 101:
    if n % 2:

        k = 1
        j = 0
        for i in range(n):

            print(end=' ' * (k - 1 - j))

            print('*' * k)


            if i >= n // 2:
                k -= 2
                j -= 1
            else:
                k += 2
                j += 1



    else:
        print("INPUT ERROR!")
else:
    print("INPUT ERROR!")

#
# *
#  ***
#   *****
#    *******
#   *****
#  ***
# *
#

# *
#   ***
#     *****
#       *******
#     *****
#   ***
# *















