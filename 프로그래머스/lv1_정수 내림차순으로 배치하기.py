def solution(n):
    n = list(map(str, str(n)))
    n.sort(reverse=True)
    n = int(''.join(n))
    return n

solution(118372)

    