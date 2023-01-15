import sys

cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = sys.stdin.readline().strip()

for i in cro:
    if i in word:
        word = word.replace(i, '+')

print(len(word))