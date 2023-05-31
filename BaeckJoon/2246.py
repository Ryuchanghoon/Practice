import sys

input = sys.stdin.readline

condo = []

sum = 0

x = int(input())

for i in range(x):
    d, c = map(int, input().split()) # d = 바닷가 거리, c = 숙박비
    condo.append([d, c])

condo.sort()

cost = 10001 #콘도개수 10000까지라 해서 그냥 최대치.


for i in condo:
    temp = i[1]

    if temp < cost:
        cost = temp
        sum += 1


print(sum)