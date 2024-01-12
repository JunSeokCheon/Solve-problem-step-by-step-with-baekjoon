import math

def lcm(a,b):
    return (a * b) // math.gcd(a,b)

def solution(n, m):
    return [math.gcd(n, m), lcm(n, m)]

print(solution(2, 5))