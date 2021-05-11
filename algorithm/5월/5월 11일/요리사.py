import sys
sys.stdin = open('input (43).txt', 'r')


def selectA(_sumA, idx, a):

    if idx < n:
        if len(A_visited) == n // 2:
            pass
        else:
            if idx not in A_visited:
                if a != idx:
                    _sumA += arr[a][idx] + arr[idx][a]
                    A_visited.append(a)
                    A_visited.append(idx)
                    selectA(_sumA, idx+1, a+1)
                    A_visited.pop()
                    A_visited.pop()
                    _sumA = _sumA - arr[a][idx] - arr[idx][a]
                    selectA(_sumA, idx+1, a)
                else:
                    selectA(_sumA, idx + 1, a)
    if len(A_visited) > n // 2:
        return

    if len(A_visited) == n // 2:
        selectB(0, 0, 0, _sumA)


def selectB(_sumB, idx, b, _sumA):
    global result

    if idx < n:
        if b in A_visited:
            selectB(_sumB, idx, b+1, _sumA)
        else:
            if idx not in B_visited and idx not in A_visited:
                if idx != b:
                    B_visited.append(b)
                    B_visited.append(idx)
                    _sumB = _sumB + arr[b][idx] + arr[idx][b]
                    selectB(_sumB, idx+1, b+1, _sumA)
                    B_visited.pop()
                    B_visited.pop()
                    _sumB = _sumB - arr[b][idx] - arr[idx][b]
                else:
                    selectB(_sumB, idx + 1, b, _sumA)
            else:
                selectB(_sumB, idx + 1, b, _sumA)

    if len(B_visited) == n // 2:
        result = min(result, abs(_sumB-_sumA))


T = int(input())

for tc in range(1, T+1):

    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]

    result = 987654321

    A_visited = []
    B_visited = []
    selectA(0, 0, 0)

    print(result)
