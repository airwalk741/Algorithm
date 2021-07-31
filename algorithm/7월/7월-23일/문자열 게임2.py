import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for i in range(T):

    _min, _max = 0, 0

    string = input()

    n = int(input())

    search = n



    length = len(string)

    while n != length:

        word = {}

        for i in range(n):

            if string[i] not in word:
                word[string[i]] = 1
            else:
                word[string[i]] += 1


        if search in word.values():

            if _min == 0:

                _min = n

            if string[0] == string[n]:
                _max = max(_max, n)


        for i in range(1, length - n + 1):

            word[string[i - 1]] -= 1

            if string[n + i - 1] not in word:
                word[string[n + i - 1]] = 1
            else:
                word[string[n + i - 1]] += 1


            if search in word.values():

                if _min == 0:
                    _min = n

                if string[i] == string[n + i - 1]:
                    _max = max(_max, n)

        n += 1

    if not _min and not _max:
        print(-1)
    else:
        print(_min, _max)

















