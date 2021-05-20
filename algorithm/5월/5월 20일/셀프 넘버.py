

numbers = set(range(1, 10000))

result = set()

for num in numbers:
    for i in str(num):
        num += int(i)
    if num < 10000:
        result.add(num)


result = numbers - result
result = list(result)
result.sort()
for num in result:
    print(num)



