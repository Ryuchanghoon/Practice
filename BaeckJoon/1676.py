#소인수 분해 계산. 2 & 5로 나누어 떨어지는 거 계산.

import sys

input = sys.stdin.readline


n = int(input())

count_a = 0
count_b = 0


for i in range(1, n+1):
    
    while i % 2 == 0: #2로 나누어 떨어지는 경우.
        count_a += 1 # 나누어 떨어질 때 마다, 1 증가 시키고,
        i = i // 2 # i값 2로 나누고

    while i % 5 == 0: # 5로 나누어 떨어지는 경우.
        count_b += 1 # 동일하게 5 나누어 떨어지는 경우, 1 증가.
        i = i // 2 # i값 끝날때까지 계속 2 나누기.


print(min(count_a, count_b))