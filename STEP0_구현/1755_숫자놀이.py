import sys

m, n = map(int, input().split())

num_dic = {"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}

result = []
for num in range(m, n+1):
  new_str = ' '.join([num_dic[i] for i in str(num)])
  result.append([num, new_str])

result = sorted(result, key = lambda x : x[1])

for i in range(len(result)):
  if i%10 == 0 and i != 0:
    print()
  print(result[i][0], end=" ")
