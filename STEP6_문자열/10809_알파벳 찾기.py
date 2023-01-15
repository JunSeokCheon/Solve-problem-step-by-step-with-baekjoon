import sys

word = sys.stdin.readline().strip()
alphabet = list(range(97,123))

for i in alphabet:
  print(word.find(chr(i)))