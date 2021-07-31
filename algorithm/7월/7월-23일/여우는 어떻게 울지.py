import sys
sys.stdin = open('input.txt', 'r')

for _ in range(int(input())):


    total = list(input().split())

    # 탐색은 dict가 빠르다
    sori = set()

    while 1:

        animal = input()

        # 소리가 여우는 무슨소리라고 물어보면 while문 나가기
        if animal == 'what does the fox say?':
            break

        a, b, c = animal.split()

        sori.add(c)


    # sori에 없으면 여우 소리인 것이다
    for i in total:

        if i not in sori:
            print(i, end=' ')

    print()





