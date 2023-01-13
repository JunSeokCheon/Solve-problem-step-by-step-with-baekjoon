import sys

C = int(sys.stdin.readline().strip())

for _ in range(C):
    N_list = list(map(int, sys.stdin.readline().strip().split()))
    N_list_avg = sum(N_list[1:])/N_list[0]
    count = 0
    
    for score in N_list[1:]:
        if N_list_avg < score:
            count+=1
    
    
    print(str('{:.3f}'.format((count/N_list[0])*100))+'%')
    