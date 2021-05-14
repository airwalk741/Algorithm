import sys
sys.stdin = open('input (43).txt', 'r')

parent_twice = 0
tc = 1
break_check = 0
real_break = 0

tree = {}
cnt = 0

while True:


    nodes = input().rstrip().split('  ')

    if nodes != ['']:
        for node in nodes:

            if len(node) > 3:
                start, end = int(node[0] + node[1]), int(node[3] + node[4])
            else:
                start, end = int(node[0]), int(node[2])

            cnt += 1

            if not start and not end and not break_check:
                break_check = 1
                cnt -= 1
                if cnt == 0:
                    print('Case {} is a tree.'.format(tc))
                elif 0 not in tree.values():
                    print('Case {} is not a tree.'.format(tc))
                elif parent_twice:
                    print('Case {} is not a tree.'.format(tc))
                else:
                    print('Case {} is a tree.'.format(tc))

                # 트리 배열
                tc += 1
                cnt = 0
                tree = {}
                parent_twice = 0


            else:
                if break_check:
                    if start == -1 and end == -1:
                        real_break = 1

                break_check = 0

            if start and end:
                start, end = str(start), str(end)

                if end not in tree.keys():
                    tree[end] = 1
                else:
                    tree[end] += 1

                if start not in tree.keys():
                    tree[start] = 0

    if real_break:
        break



