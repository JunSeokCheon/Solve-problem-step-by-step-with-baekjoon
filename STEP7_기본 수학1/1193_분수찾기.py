import sys

X = int(sys.stdin.readline())
line = 1

while X > line:
    X -= line
    line += 1

if line % 2 == 0 :
    num1 = X
    num2 = line - X + 1
elif line % 2 == 1 :
    num1 = line - X + 1
    num2 = X

print(num1,'/',num2,sep = "")
    