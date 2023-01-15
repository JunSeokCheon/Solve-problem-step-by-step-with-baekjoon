import sys
from collections import Counter

alpha = sys.stdin.readline().upper().strip()
collection = Counter(alpha)

collections = collection.most_common(2)

try:
    if collections[0][1] == collections[1][1]:
        print("?")
    else:
        print(collections[0][0])
except:
    print(collections[0][0])