import sys

n = int(sys.stdin.readline())
n_list = [sys.stdin.readline().strip() for _ in range(n)]

asd_nList = sorted(n_list)
des_nList = sorted(n_list, reverse= True)

if n_list == asd_nList:
    print("INCREASING")
elif n_list == des_nList:
    print("DECREASING")
else:
    print("NEITHER")