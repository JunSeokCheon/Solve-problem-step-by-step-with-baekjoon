import sys

a, b, v = map(int, sys.stdin.readline().split())

day = (v-b)%(a-b)
if day!=0:
  print((v-b)//(a-b)+1)
else:
  print((v-b)//(a-b))