import sys

n = int(sys.stdin.readline())
serial_number = []

for _ in range(n):
    number = sys.stdin.readline().strip()
    cnt = 0
    for char in number:
        if char.isdigit():
            cnt += int(char)
        
    serial_number.append((number, cnt))

answer = sorted(serial_number, key = lambda x : (len(x[0]), x[1], x[0]))

for result in answer:
    print(result[0])
