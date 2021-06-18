
X = 10
Y = 85
D = 30

if Y % D:
    num = Y // D
else:
    num = Y // D - 1

if X + (D * num) < Y:
    num += 1
    return num
else:
    return num



