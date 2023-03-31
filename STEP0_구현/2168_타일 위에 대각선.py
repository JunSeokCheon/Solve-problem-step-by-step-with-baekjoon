import sys

x, y = map(int, sys.stdin.readline().split())

def gcd(x,y):
    if y > x:
        x, y = y, x
    
    while True:
        if y == 0:
            break
        x, y = y, x%y
    return x

print(x + y - gcd(x,y))
