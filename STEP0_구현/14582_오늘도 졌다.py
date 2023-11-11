import sys

first_line = list(map(int, sys.stdin.readline().split()))
second_line = list(map(int, sys.stdin.readline().split()))

first_sum = 0
second_sum = 0
flag = "No"

for i in range(9):
    first_sum += first_line[i]
    if second_sum < first_sum:
        flag = "Yes"
        break
    second_sum += second_line[i]

print(flag)