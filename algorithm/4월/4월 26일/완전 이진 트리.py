import sys
sys.stdin = open('input (43).txt', 'r')

# 상근이가 읽은 것은 앞에서부터 읽은 중위표기법
# 다시 원래 트리로 바꿔주기 위해
# 뒤에서부터 읽기
def post(idx):

    if idx < tree_max:
        post(idx * 2 + 1) # 뒤에서 부터
        if tree[idx] == 0: # 뒤에서부터 읽었는데 값이 없으면 pop 넣는다
            tree[idx] = build.pop()
        post(idx * 2)


k = int(input())
# 인덱스는 0부터 트리의 번로는 1부터니까
# 2 ** k - 1이 아닌 2 ** k
tree_max = 2 ** (k)


tree = [0] * (tree_max)

build = list(map(int, input().split()))

# tree는 1번부터 시작
post(1)

jump = 1 # 다음줄로 넘거가는거 체크
number = 1 # 트리는 1 -> 2 -> 4 이렇게 한줄당 1부터해서 2배씩 늘어남
for i in range(1, tree_max):
    print(tree[i], end=' ')

    if number == jump:
        print()
        number *= 2
        jump = 1
    else:
        jump += 1





