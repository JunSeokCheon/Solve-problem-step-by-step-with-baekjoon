import sys

T = int(sys.stdin.readline())

for _ in range(T):
    oxstr = sys.stdin.readline()
    total_score = 0
    semi_score = 0
    
    for symbol in oxstr:
        if symbol == 'O':
            semi_score += 1
            total_score += semi_score   
        else:
            semi_score = 0
            total_score += semi_score
    
    print(total_score)