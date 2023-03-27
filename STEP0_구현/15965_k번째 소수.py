import sys

def isprime(n):
    board = [True] * n

    m = int(n**0.5)
    for i in range(2, m+1):
        if board[i] == True:
            for j in range(i+i, n, i):
                board[j] = False
    return [i for i in range(2, n) if board[i] == True]

n = int(sys.stdin.readline())
answer = isprime(10**7)
print(answer[n-1])