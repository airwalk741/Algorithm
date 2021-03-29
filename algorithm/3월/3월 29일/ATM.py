
n = int(input())

number = list(map(int, input().split()))

number.sort()

result = 0

for i in range(len(number)):
    result += number[i] * (len(number)-i)

print(result)