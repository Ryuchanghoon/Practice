import sys

input = sys.stdin.readline


num = int(input())

count = [0] * (num + 1) #첫 값 0으로 설정.

for i in range(2, num + 1):
    count[i] = count[i-1] + 1 #반복문 돌면서 하나씩 올리고.
    
    if i % 2 == 0:
        count[i] = min(count[i], count[i//2] + 1) #2로 나눈값과 위에 그냥 반복문 돈 값 중에서 작은것.
    
    if i % 3 == 0:
        count[i] = min(count[i], count[i//3] + 1) #3로 나눈값과 위에 그냥 반복문 돈 값 중에서 작은것.

print(count[num])