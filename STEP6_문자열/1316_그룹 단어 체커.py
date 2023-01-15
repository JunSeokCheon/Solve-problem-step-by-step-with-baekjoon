import sys

N = int(sys.stdin.readline().strip())
result = N
for _ in range(N):
    word = sys.stdin.readline().strip()
    
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            continue
        
        if word[i] in word[i+1:]:
            result -= 1
            break
print(result)