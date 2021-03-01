import sys

sys.stdin = open('input (43).txt', 'r')

def dfs(value):

    result = []
    st = []
    st.append(value)

    while len(st) > 0:

        n = st.pop()
        if visited[n] == 0:
            visited[n] = 1
            result.append(n)
            for i in range(len(arr_list)):
                if arr_list[n][i] == 1:
                    st.append(i)
    return  result

for tc in range(1, 11):

    t, length = map(int, input().split())


    arr = list(map(int, input().split()))

    arr_list = [ [0] * 100 for _ in range(100)]

    for i in range(0, len(arr), 2):
        arr_list[arr[i]][arr[i+1]] = 1



    visited = [0] * 100

    result1 = dfs(arr[0])

    if 99 in result1:
        print('1')
    else:
        print('0')







