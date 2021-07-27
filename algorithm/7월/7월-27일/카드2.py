import sys
sys.stdin = open('input.txt', 'r')
from collections import deque


n = int(input())

arr = deque(i for i in range(1, n + 1))

while len(arr) != 1:

    arr.popleft() # 맨 앞에 뽑고

    arr.append(arr.popleft()) # 맨 뒤에 추가하기



print(arr[0])