import sys

input = sys.stdin.readline

# 2차원 배열 만들어주고
ppan = [[0] * 101 for _ in range(101)]

for _ in range(4):
    x_1, y_1, x_2, y_2 = map(int, input().split()) #직사각형 좌표들
    
    for i in range(x_1, x_2):
        
        for j in range(y_1, y_2):
            ppan[i][j] = 1

# 면적
ppan_sum = 0
for i in range(101):
    for j in range(101):
        if ppan[i][j] == 1:
            ppan_sum += 1

print(ppan_sum)