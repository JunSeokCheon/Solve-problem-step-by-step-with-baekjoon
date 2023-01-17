import sys

n = int(sys.stdin.readline())
for _ in range(n):
  h, w, n = map(int, sys.stdin.readline().split())
  if n%h==0:
    print(int(h*100+n/h))
  else:
    print(int(n%h*100+n/h+1))