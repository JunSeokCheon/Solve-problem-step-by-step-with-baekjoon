import sys

N = int(sys.stdin.readline())
count = 0
new = N

while(True):
    if new < 10:
        new = "0" + str(new)
    else:
        new = str(new)

    two_sum = str(int(new[0]) + int(new[-1]))
    new = str(new)[-1] + two_sum[-1]
    count += 1
    new = int(new)
    
    if N == new:
        print(count)
        break