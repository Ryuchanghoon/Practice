import sys

input = sys.stdin.readline

n = int(input())

count = [0] * 10

x = 1

while n >= x:
    a, b = divmod(n, x * 10)
    count[0] += max(0, (a - 1) * x + min(x, max(b - x + 1, 0)))

    for i in range(1, 10):
        count[i] += a * x + min(x, max(b - i * x + 1, 0))

    x *= 10

print(*count)