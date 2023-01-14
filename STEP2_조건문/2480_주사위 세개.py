import sys

num1, num2, num3 = map(int, sys.stdin.readline().split())

if num1 == num2 == num3:
    print(10000 + num1 * 1000)
elif num1 == num2 or num1 == num3 or num2 == num3:
    if num1 == num2:
        print(1000+num1*100)
    if num1 == num3:
        print(1000+num1*100)
    if num2 == num3:
        print(1000+num2*100)
else:
    print(100*max(num1, num2, num3))