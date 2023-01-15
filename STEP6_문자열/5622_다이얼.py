import sys

dialog_dict = {2:"ABC", 3:"DEF", 4:"GHI", 5:"JKL", 6:"MNO", 7:"PQRS", 8:"TUV", 9:"WXYZ"}

word = sys.stdin.readline().strip()
time = 0

for mini_word in word:
    for key, value in dialog_dict.items():
        if mini_word in value:
            time += key+1

print(time)