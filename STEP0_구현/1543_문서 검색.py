import sys

docu = sys.stdin.readline().strip()
word = sys.stdin.readline().strip()
count = 0
i = 0

if len(docu) < len(word):
    print(0)
else:
    # while docu.find(word) != -1:
    #     docu = docu[:docu.find(word)] + docu[docu.find(word)+len(word):]
    #     count += 1
    while i <= len(docu):
        if docu[i:len(word)+i] == word:
            count += 1
            i += len(word)
        else:
            i += 1
        
    
    print(count)
    
