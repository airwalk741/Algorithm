import sys
sys.stdin = open('input (43).txt', 'r')

def merge_sort(nums):

    if len(nums) == 1:
        return nums

    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    global result

    arr = []
    check = 1
    i = 0
    j = 0

    while i < len(left) or j < len(right):

        if i < len(left) and j < len(right):

            if left[i] <= right[j]:
                arr.append(left[i])
                i += 1

            else:
                arr.append(right[j])
                j += 1
        elif i < len(left):
            if check:
                check = 0
                result += 1
            arr.append(left[i])
            i += 1

        elif j < len(right):
            arr.append(right[j])
            j += 1

    return arr


T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    n = int(input())

    nums = list(map(int, input().split()))

    result = 0

    arr = merge_sort(nums)

    print(arr[n//2], result)