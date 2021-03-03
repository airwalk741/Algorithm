# 6,2
# 10,3

x, y, w, h = map(int, input().split())

print(min(abs(x - w), abs(y - h), x, y))
