import sys

input = sys.stdin.readline

n = int(input())

top = 0

for _ in range(n):
    num = list(map(int,input().split()))
    num.sort()


    if num[0] == num[1] == num[2]:
        top_mon = 10000 + num[0] * 1000

    elif num[0] == num[1] or num[1] == num[2]:
        top_mon = 1000 + num[1] * 100

    else:
        top_mon = num[2] * 100


    if top_mon > top:
        top = top_mon


print(top)