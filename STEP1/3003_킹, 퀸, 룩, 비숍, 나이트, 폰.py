import sys
king, queen, rooks, bishops, knights, pawns = map(int, sys.stdin.readline().split())
print(1-king, 1-queen, 2-rooks, 2-bishops, 2-knights, 8-pawns)