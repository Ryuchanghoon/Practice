n = input() 
count = 0 
while len(n) > 1: # 한자리수 까지 반복
    temp = 0
    
    for sum_ in n:
        temp += int(sum_) # temp에 넣어주고
    n = str(temp)
    count += 1 
print(count) 

if int(n) % 3 == 0:
    print('YES')

else:
    print('NO')