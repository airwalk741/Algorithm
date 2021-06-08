import sys
sys.stdin = open('input (43).txt', 'r')

arr = list(map(int, input().split()))

func = [[], []]

for i in range(len(arr)):
    if i < 3:
        func[0].append(arr[i])
    else:
        func[1].append(arr[i])

y = (func[0][2] * func[1][0] - func[1][2] * func[0][0]) / (func[0][1] * func[1][0] - func[1][1] * func[0][0])
if func[0][0]:
    x = (func[0][2] - func[0][1] * y) / func[0][0]
else:
    x = (func[1][2] - func[1][1] * y) / func[1][0]

print(int(x), int(y))












