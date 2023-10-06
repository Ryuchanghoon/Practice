import sys
from collections import Counter


input = sys.stdin.readline

n = int(input())
num = [int(input()) for _ in range(n)]


mean = round(sum(num) / n)


sort_num = sorted(num)
mid = sort_num[n // 2]


counter = Counter(num)
many = counter.most_common()

most = many[0][0]

if len(many) > 1 and many[0][1] == many[1][1]:
    many_most = []

    for i in many:
        if i[1] == many[0][1]:
            many_most.append(i)

    many_most_sort = sorted(many_most, key = lambda x: x[0])

    most = many_most_sort[1][0]


range_num = max(num) - min(num)


print(mean)
print(mid)
print(most)
print(range_num)