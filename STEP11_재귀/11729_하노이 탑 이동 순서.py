# 하노이 탑 알고리즘 정리 링크 : https://shoark7.github.io/programming/algorithm/tower-of-hanoi
import sys

N = int(sys.stdin.readline())

def move(start, to):
    print(start, to, sep=' ')

def hanoi(N, start, to, via):
    if N == 1:
        move(start, to)
    else:
        hanoi(N-1, start, via, to)
        move(start, to)
        hanoi(N-1, via, to, start)

print((2**N)-1)
hanoi(N, 1, 3, 2)