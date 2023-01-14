import sys

N = int(sys.stdin.readline())
count = 99

if N < 100:
    print(N)
elif N >= 100 and N <= 1000:
    for num in range(100, N+1):
        num = str(num)
        
        if (int(num[0]) - int(num[1])) == (int(num[1]) - int(num[2])):
            count += 1

    print(count)
            