from sys import stdin
from bisect import bisect

def solution(N, S, words):
    answer = 0
    for word in words:
        idx = min(N-1, bisect(S,word)) # word와 값이 가장 유사한 문자열 인덱스
        # 접두사인지 확인
        if S[idx].startswith(word):
            answer += 1
        # 접두사인지 확인
        elif S[idx-1].startswith(word):
            answer += 1
    return answer

# input
N, M = map(int,stdin.readline().split())
S = sorted([stdin.readline().rstrip() for _ in range(N)])
words = [stdin.readline().rstrip() for _ in range(M)]

# result
result = solution(N, S, words)
print(result)