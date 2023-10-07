import sys

#input = sys.stdin.readline

a = input()

a_re = a[::-1]

if a == a_re:
    print(1)

elif a != a_re:
    print(0)