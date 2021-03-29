
def mul(num):

    num = str(int(num) * 2)

    return num

def num_1(num):

    num += '1'

    return num

def dfs(num, cnt):
    global count

    if int(num) >= int(result):
        if int(num) == int(result):
            if count > cnt:
                count = cnt
        return

    dfs(mul(num), cnt+1)
    dfs(num_1(num), cnt+1)


n, result = input().split()

count = 987654321

dfs(n, 0)

if count == 987654321:
    print('-1')
else:
    print(count+1)