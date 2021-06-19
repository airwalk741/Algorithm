

A = [1, 3, 6, 4, 1, 2]

nums = [0] * 100001
nums[0] = 1
for i in range(len(A)):

    try:
        nums[A[i]] = 1
    except:
        continue


try:
    num = nums.index(0)
    return num
except:
    return 100001