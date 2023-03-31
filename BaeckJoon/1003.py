import sys

input = sys.stdin.readline

times = int(input()) #for문 몇번 돌릴지.


# 몇번 호출되나 보면 된다.
'''
def fibo(num_th):
    if num_th == 0:
        return (1, 0)
    
    elif num_th == 1:
        return (0, 1)
    
    else:
        a, b = fibo(num_th-1) 
        c, d = fibo(num_th-2) 
        return (a+c, b+d)
'''

# 0 1 몇번.
for i in range(times):
    num_0 = [1,0]
    num_1 = [0,1]

    num_th = int(input())

    if num_th > 1:
        for j in range(num_th -1):
            num_0.append(num_1[-1])
            num_1.append(num_0[-2] + num_1[-1])

    print(num_0[num_th], num_1[num_th])


# 점화식.
# 위에 풀이는 시간초과. 리스트에 넣는 방식으로 다시.