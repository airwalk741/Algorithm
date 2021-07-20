import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

n = int(input())

strings = set()

for _ in range(n):

    string = input().rstrip()

    if string not in strings:
        strings.add(string)


strings = list(strings)

strings.sort(key=lambda x: (len(x), x))


for i in strings:
    print(i)
