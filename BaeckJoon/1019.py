import sys

input = sys.stdin.readline

n = int(input())

cnt = [0] * 10
multi = 1

def nine(num): #9로 맞추기.
    while num % 10 != 9:
        
        for digit in str(num):
            cnt[int(digit)] += multi
        num -= 1
    return num

while n > 0:
    n = nine(n) #

    if n < 10: #1자리면,
        for i in range(n + 1): # 그게 최고 자리수면, 그냥 계속 더해주고
            cnt[i] += multi

    else:
        for j in range(10): # 그게 아니면 0~9까지. 계산한 식. +
            cnt[j] += (n // 10 + 1) * multi

    cnt[0] -= multi
    multi *= 10
    n //= 10

print(*cnt)