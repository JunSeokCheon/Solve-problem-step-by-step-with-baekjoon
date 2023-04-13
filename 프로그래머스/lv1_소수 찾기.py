def isprime(n):
    board = [True] * (n+1)
    
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if board[i] == True:
            for j in range(i+i, n+1, i):
                board[j] = False
    
    return [i for i in range(2, n+1) if board[i] == True]

def solution(n):
    return len(isprime(n))