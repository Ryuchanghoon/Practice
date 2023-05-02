import sys

a,b = map(int,input().split())

while b:
    a,b = b, a % b

print('1' * a )

#유클리드 호제법 사용.
#a를 b로 나눈 나머지 R, (a,b) = (b,R)