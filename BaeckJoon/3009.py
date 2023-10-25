import sys

input = sys.stdin.readline



x_what = []
y_what = []

for _ in range(3):
    x, y = map(int, input().split())
    x_what.append(x)
    y_what.append(y)

x_result = 0
y_result = 0

for x in x_what:
    x_result ^= x

for y in y_what:
    y_result ^= y


print(x_result, y_result)