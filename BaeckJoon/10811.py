import sys

input = sys.stdin.readline

a,b = map(int,input().split())

a_b = list(range(1, a + 1))

for _ in range(b):
    i, j = map(int,input().split())
    a_b[i - 1 : j] = reversed(a_b[i-1 : j])

print(" ".join(map(str, a_b)))