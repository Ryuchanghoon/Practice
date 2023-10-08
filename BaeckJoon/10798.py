import sys

input = sys.stdin.readline


list_col = [[] for _ in range(15)]

for _ in range(5):
    mun = input().strip()

    for i in range(len(mun)):
        list_col[i].append(mun[i])

mun_sum = ''

for i in range(len(list_col)):
    mun_sum += ''.join(list_col[i])


print(mun_sum)