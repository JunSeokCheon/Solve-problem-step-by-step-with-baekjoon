import sys

n, k, a, b = map(int, sys.stdin.readline().split())
day = 0

plant_list = [k for _ in range(n)]

while min(plant_list) != 0:
    day += 1
    plant_list.sort()
    for idx, num in enumerate(plant_list):
        if idx < a:
            plant_list[idx] = plant_list[idx] + b - 1
        else:  
            plant_list[idx] -= 1

print(day)