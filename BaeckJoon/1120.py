import sys

input = sys.stdin.readline

list_x, list_y = input().split() #문자열 입력받아온거 따로따로 분리.

list_y_min = len(list_y) #두번째 입력값 기준으로.

for i in range(len(list_y) - len(list_x) + 1): #두개의 차이만큼
    diff_input = 0
    for j in range(len(list_x)): #첫번째 입력값 개수만큼 반복
        if list_x[j] != list_y[i+j]: # 두개의 입력값이 다르다면,
            diff_input += 1 # 위에 1씩 추가.

    list_y_min = min(list_y_min, diff_input) #두번째 입력값과, 위에 다른 문자만큼 추가해준거 중에서 최솟값.

print(list_y_min) #출력.