

A = [1, 3, 1, 4, 2, 3, 5, 4]
X = 5

leaf = [0] * (X + 1)
cnt = -1

for num in A:

    cnt += 1

    try:
        if leaf[num] == 0:
            X -= 1
            leaf[num] = 1
    except:
        continue



    if X == 0:
        return cnt

return -1