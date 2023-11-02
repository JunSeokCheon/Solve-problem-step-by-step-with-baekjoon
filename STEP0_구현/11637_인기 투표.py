import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    n_list = []
    for _ in range(n):
        n_list.append(int(sys.stdin.readline()))
    half_value = sum(n_list) // 2
    max_value = max(n_list)
    
    if n_list.count(max_value) > 1:
        print("no winner")
    elif max_value > half_value:
        print(f"majority winner {n_list.index(max_value)+1}")
    elif max_value <= half_value:
        print(f"minority winner {n_list.index(max_value)+1}")

