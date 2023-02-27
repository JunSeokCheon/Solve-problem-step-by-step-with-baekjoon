import sys
from itertools import permutations

X = int(sys.stdin.readline())

sort_permute = sorted(list(set(list(permutations(str(X))))))

for index, value in enumerate(sort_permute):
    merge_data = ''.join(value)
    if int(merge_data) == X:
        if ''.join(sort_permute[-1]) == merge_data:
            result = merge_data
            break
        else:
            result = ''.join(sort_permute[index+1])
            break

if int(result) == X:
    print(0)
else:
    print(result)

