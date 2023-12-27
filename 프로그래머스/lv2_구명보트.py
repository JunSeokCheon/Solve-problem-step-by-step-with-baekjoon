def solution(people, limit):
    answer = 0
    people.sort()

    left = 0
    right = len(people) - 1
    
    while left <= right:
        if people[left] + people[right] > limit:
            answer += 1
            right -= 1
        else:
            answer += 1
            right -= 1
            left += 1
            
    return answer

# print(solution([70, 50, 80, 50], 100))
# print(solution([70, 80, 50], 100))
# print(solution([10, 15, 20, 90], 100))
# print(solution([50, 50, 100], 100))
# print(solution([10, 20, 30, 40], 50))

