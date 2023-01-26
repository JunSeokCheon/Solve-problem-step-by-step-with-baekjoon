import sys

N = int(sys.stdin.readline())

def pick_star(n):
    if n == 3:
        return ['***', '* *', '***']
    
    result= []
    arr = pick_star(n//3)
    
    for i in arr:
        result.append(i*3)
    for i in arr:
        result.append(i+' '*(n//3)+i)
    for i in arr:
        result.append(i*3)
    
    return result


result = pick_star(N)
print('\n'.join(result))