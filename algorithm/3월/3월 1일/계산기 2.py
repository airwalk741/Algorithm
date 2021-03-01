import sys

sys.stdin = open('input (43).txt', 'r')

def operation(a, b, value):

    if value == '+':
        return a + b
    elif value == '-':
        return a - b
    elif value == '*':
        return a * b
    elif value == '/':
        return a / b


T = 10
for tc in range(1, T+1):


    n = int(input())

    cal = list(input())

    operater = {
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }
    st = []
    result = []

    while len(cal) > 0:

        value = cal.pop(0)

        if value not in operater:
            result.append(value)
        else:
            if value == '(' or len(st) == 0:
                st.append(value)
            elif operater[value] > operater[st[-1]]:
                st.append(value)
            elif operater[value] <= operater[st[-1]]:
                while len(st) != 0 and operater[value] <= operater[st[-1]]:
                  result.append(st.pop())
                st.append(value)
            elif operater[value] == ')':
                while st[-1] != '(':
                    result.append(st.pop())
                st.pop()


    while len(st) > 0:
        result.append(st.pop())



    while len(result) > 0:
        value = result.pop(0)
        if value not in operater:
            st.append(value)
        else:
            b = int(st.pop())
            a = int(st.pop())
            st.append(operation(a, b, value))

    print('#{} {}'.format(tc, *st))
























