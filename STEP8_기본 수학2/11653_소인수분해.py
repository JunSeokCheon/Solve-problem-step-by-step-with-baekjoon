import sys

def solve(num):
    for i in range(2, num+1):
        if num % i == 0:
            return i, num//i
    return False

num = int(sys.stdin.readline())
num_list = []

if num == 1:
    print("")
else:
    while(True):
        if solve(num) == False:
            num_list.sort()
            for i in num_list:
                print(i)
            break
        else:
            result, num = solve(num)
            num_list.append(result)