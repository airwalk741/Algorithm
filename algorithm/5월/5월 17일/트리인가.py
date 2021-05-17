import sys
sys.stdin = open('input (43).txt', 'r')


def find(x): # 대표 찾기

    if x == group[x]:
        return x
    else:
        return find(group[x])

def union(x, y): # 대표 입력

    group[find(y)] = find(x)


tree = {}
is_tree = True
tree_parent = []

zero_check = 0
negative_check = 0
tc = 1


while True:

    nodes = list(input().split('  '))

    if zero_check:
        cnt = 0

        for parent in tree_parent:
            if parent not in tree.keys():
                cnt += 1

        if cnt != 1:
            is_tree = False

        if not len(tree):
            is_tree = True

        # 조건 3 (루트노드는 모든 노드 지나야함 => 무리 구하는 로직)
        if is_tree:
            node_max = 0

            group = [i for i in range(1000)]

            for child, parent in tree.items():
                child, parent = int(child), int(parent)

                union(child, parent)

                if node_max < child:
                    node_max = child

            for i in range(node_max + 1):

                group[i] = find(group[i])

            tree = []

            for i in range(node_max + 1):

                tree.append(group[i])

            for i in range(len(tree)):
                tree[i] = find(tree[i])

            for i in range(len(tree)):
                if i == tree[i]:
                    tree[i] = 0



            if len(set(tree)) != 2:
                is_tree = False


        if is_tree:
            print('Case {} is a tree.'.format(tc))
        else:
            print('Case {} is not a tree.'.format(tc))

        tree = {}
        is_tree = True
        tree_parent = []
        tc += 1
        zero_check = 0

    for node in nodes:

        length = len(node)

        if length == 0:
            continue

        elif length == 3:

            parent, child = node[0], node[2]


            if parent == '0' and child == '0':
                zero_check = 1
                break

            # 자식이 키, 부모가 value
            if child not in tree.keys():
                tree[child] = parent

                # 나중에 루트가 몇개인지 확인 할려고 ( 조건 1 )
                if parent not in tree_parent:
                    tree_parent.append(parent)

            # 자식은 부모 하나만 가질 수 있음 ( 조건2 )
            else:
                is_tree = False

        elif length == 5:
            negative_check = 1

    if negative_check:
        break


