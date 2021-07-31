import sys
sys.stdin = open('input.txt', 'r')


import sys


for _ in range(int(input())):


    string = input()

    frequency = {}

    max_num = 1

    for i in range(len(string)):

        if string[i] != ' ':
            if string[i] in frequency:
                frequency[string[i]] += 1
                max_num = max(max_num, frequency[string[i]])
            else:
                frequency[string[i]] = 1

    check = 0

    for k, v in frequency.items():

        if v == max_num:

            if check:
                result = '?'
                break

            check = 1
            result = k


    print(result)











