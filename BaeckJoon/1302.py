import sys
from collections import Counter

input = sys.stdin.readline

book_list = []

for i in range(int(input())):
    book_list.append(input())

count_list = Counter(book_list)

max_count = count_list.most_common(n = 1)

print(max(count_list))

########### 실패 문제.
