import sys
sys.stdin = open('input (43).txt', 'r')

def first():

    if 5 not in color.values():
        return 0

    isSame = []

    cnt = 0

    for i in range(1, 10):
        if nums[i]:
            cnt += 1
            if cnt == 5:
                break
        else:
            cnt = 0


    if cnt != 5:
        return

    return i + 900


def second():

    for i in range(10):
        if len(nums[i]) == 4:
            return i + 800

    return 0


def third():

    two = 0
    three = 0
    result = 0
    for i in range(10):

        if len(nums[i]) == 3:
            result += i * 10
            three += 1
        elif len(nums[i]) == 2:
            result += i + 700
            two += 1

    if two and three:
        return result
    else:
        return 0


def fourth():

    if 5 not in color.values():
        return 0

    cnt = 0
    for i in range(10):
        if nums[i]:
            cnt += 1
            if cnt == 5:
                return i + 600


def fifth():

    cnt = 0
    _max = 0
    for i in range(10):
        if nums[i]:
            cnt += 1
            _max = i
            if cnt == 5:
                return _max + 500
        else:
            cnt = 0

    return 0


def sixth():

    for i in range(10):
        if len(nums[i]) == 3:
            return i + 400


def seventh():

    cnt = 0
    result = 0
    for i in range(10):
        if len(nums[i]) == 2:
            cnt += 1
            if cnt == 1:
                result += i + 300
            else:
                result += (i * 10)

    if cnt == 2:
        return result
    else:
        return 0


def eighth():

    for i in range(10):
        if len(nums[i]) == 2:
            return i + 200


def ninth():

    cnt = 0
    for i in range(10):
        if nums[i]:
            cnt += 1
            if cnt == 5:
                return i + 100




color = {
    'R': 0,
    'B': 0,
    'Y': 0,
    'G': 0
}

nums = [[] for _ in range(10)]


for i in range(5):

    c, n = input().split()

    nums[int(n)].append(c)
    color[c] += 1


if first():
    print(first())
elif second():
    print(second())
elif third():
    print(third())
elif fourth():
    print(fourth())
elif fifth():
    print(fifth())
elif sixth():
    print(sixth())
elif seventh():
    print(seventh())
elif eighth():
    print(eighth())
elif ninth():
    print(ninth())

















