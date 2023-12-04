import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    result = 0
    t = 0

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            t += j

        result += i * t
        t = 0

    print(result)