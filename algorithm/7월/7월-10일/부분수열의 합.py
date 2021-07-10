import sys
sys.stdin = open('input (43).txt', 'r')



sys.setrecursionlimit(10 ** 6)
N, S = map(int, input().split())
D = list(map(int, input().split()))


def solve():
    A = [0]
    for i in range(N):
        length = len(A)
        for j in range(length):
            A += [D[i] + A[j]]
        # A += [D[i] + j for j in A]

    ans = A.count(S)
    if S == 0:
        ans -= 1
    print(ans)

solve()