def solution(n):
    answer = list(map(int, str(n)))
    answer.reverse()
    return answer

print(solution(12345))