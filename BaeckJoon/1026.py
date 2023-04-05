import sys

input = sys.stdin.readline


n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

#가장 작게 만들기 위해서, 하나는 오름차순, 하나는 내림차순.

x.sort(reverse = False) 
y.sort(reverse = True) 

sum = 0

for i in range(n):
    sum += x[i] * y[i]

print(sum)
