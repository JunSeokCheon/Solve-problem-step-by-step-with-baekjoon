import sys

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

num = int(sys.stdin.readline())
print(fibo(num))