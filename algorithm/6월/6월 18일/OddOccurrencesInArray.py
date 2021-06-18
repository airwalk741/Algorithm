

A = [9, 3, 9, 3, 9, 7, 9]

nums = {}

for num in A:

    if num not in nums:
        nums[num] = 1
    else:
        nums[num] += 1

for k, v in nums.items():

    if v % 2:
        return k
