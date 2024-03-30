# n = 1, 1
# n = 2, 2
# n = 3, 3
# n = 4, 5
# n = 5, 8
# ....
def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    
    return dp[n]