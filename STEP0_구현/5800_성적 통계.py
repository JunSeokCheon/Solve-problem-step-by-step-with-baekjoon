import sys

k = int(sys.stdin.readline())
for i in range(k):
    temp_data = list(map(int, sys.stdin.readline().split()))
    num_score = temp_data[1:]
    num_score.sort()
    num_diff = []

    for j in range(temp_data[0]-1):
        num_diff.append(num_score[j+1] - num_score[j])

    print(f"Class {i+1}")
    print(f"Max {num_score[-1]}, Min {num_score[0]}, Largest gap {max(num_diff)}")