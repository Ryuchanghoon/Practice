import sys

input = sys.stdin.readline

# A 행렬
n, m = map(int, input().split())
a = []

for _ in range(n):
    a.append(list(map(int, input().split())))

#  B 행렬
m, k = map(int, input().split())
b = []
for _ in range(m):
    b.append(list(map(int, input().split())))

# 결과 C로 척척 넣고.
c = [[0] * k for _ in range(n)]

for z in range(n):
    for y in range(k):
        for x in range(m):
            c[z][y] += a[z][x] * b[x][y]

# 결과.
for i in c:
    print(' '.join(map(str, i)))