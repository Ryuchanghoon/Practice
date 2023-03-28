import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
books = [input() for _ in range(n)]

count_books = Counter(books) #위에 받아준  books 빈도수

max_count = max(count_books.values()) #빈도수 가장 큰 것, 받아와서 딕셔너리 값만.

# 출판횟수 가장 많은 책들. 리스트로
best_sellers = []
for book, count in count_books.items():
    if count == max_count:
        best_sellers.append(book)

# 사전순으로 가장 앞에 나오는 제목.
best_seller = sorted(best_sellers)[0]

print(best_seller)

## 사전순으로 앞서는 것을 고려 안했다.