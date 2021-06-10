import sys
sys.stdin = open('input (43).txt', 'r')


first = int(input())
second = int(input())

result = first * second

while second:

    print(first * (second % 10))

    second = second // 10

print(result)