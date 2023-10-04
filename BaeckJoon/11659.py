import sys

input = sys.stdin.readline


a, b = map(int,input().split())

num = list(map(int,input().split()))

sum_n = [0]
tem = 0

for i in num:
    tem = tem + i
    sum_n.append(tem)

for i in range(b):
    x, y = map(int,input().split())

    print(sum_n[y] - sum_n[x - 1])