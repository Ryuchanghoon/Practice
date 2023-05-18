import math


number = input()

count = [0] * 10  # 0부터 9까지 숫자 개수

for digit in number:
    count[int(digit)] += 1  # 숫자의 개수 뽑고

count[6] = math.ceil((count[6] + count[9]) / 2)  # 6 & 9 세트로
count[9] = 0

max_count = max(count)

print(max_count)