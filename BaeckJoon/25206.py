import sys

input = sys.stdin.readline

i=0
sum=0
p=0
while i<20:
    uni=list(map(str,input().split()))
    if '1' in uni[1]:
        a=1
    elif '2' in uni[1]:
        a=2
    elif '3' in uni[1]:
        a=3
    elif '4' in uni[1]:
        a=4
    if uni[2]=='A+':
        sum+=4.5*a
        p+=a
    elif uni[2]=='A0':
        sum+=4.0*a
        p+=a
    elif uni[2]=='B+':
        sum+=3.5*a
        p+=a
    elif uni[2]=='B0':
        sum+=3.0*a
        p+=a
    elif uni[2]=='C+':
        sum+=2.5*a
        p+=a
    elif uni[2]=='C0':
        sum+=2.0*a
        p+=a
    elif uni[2]=='D+':
        sum+=1.5*a
        p+=a
    elif uni[2]=='D0':
        sum+=1.0*a
        p+=a
    elif uni[2]=='F':
        p+=a
    i+=1
sum=sum/p
print(round(sum, 6))