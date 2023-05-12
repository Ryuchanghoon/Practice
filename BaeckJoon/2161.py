import sys

input = sys.stdin.readline

n = int(input())
card = list(range(1, n+1))  

while len(card) > 1:  # 1장까지 반복.
    print(card.pop(0), end = ' ')  # 위에 카드 삭제 출력.
    card.append(card.pop(0))  # 삭제 카드를 아래로

print(card[0])  # 남은 카드.

