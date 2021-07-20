import sys
sys.stdin = open('input.txt', 'r')


alpa = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]


string = input()

friend = [0] * len(string)

for i in range(len(string)):

    friend[i] = alpa[ord(string[i]) - 65]


if (sum(friend) % 10) % 2:
    print("I'm a winner!")
else:
    print("You're the winner?")