import sys

input = sys.stdin.readline

n = int(input())
ans = list(map(int,input().split()))

accuracy = 0
count = 0

for i in ans:
    if i == 1:
        count += 1
        accuracy += count

    else:
        count = 0


print(accuracy)