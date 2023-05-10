import sys

input = sys.stdin.readline

n = int(input())
num_ = 0
num_digit = 1

while num_digit <= n:
    num_ += n - num_digit + 1
    num_digit *= 10

print(num_)