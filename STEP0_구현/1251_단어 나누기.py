import sys

word = sys.stdin.readline().strip()
answer = []

for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        word_first = word[:i]
        word_second = word[i:j]
        word_third = word[j:]

        word_first = word_first[::-1]
        word_second = word_second[::-1]
        word_third = word_third[::-1]

        result = word_first + word_second + word_third
        answer.append(result)

answer.sort()

print(answer[0])

