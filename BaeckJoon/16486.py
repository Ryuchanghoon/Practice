import sys
import math


input = sys.stdin.readline

a = int(input())
b = int(input())

dul = 2 * (a + math.pi * b)

print(f'{dul:.6f}')