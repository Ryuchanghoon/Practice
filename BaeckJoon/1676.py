import sys
input = sys.stdin.readline

n = int(input())
count = 0

# 5 배수마다 0 한개씩
while n >= 5:
    count += n // 5
    n //= 5

print(count)