import sys

n = int(sys.stdin.readline())
n_list = []
country_dic = {}
cnt = 0

for _ in range(n):
    country, number, grade = map(int, sys.stdin.readline().split())
    if country not in country_dic:
        country_dic[country] = 0

    n_list.append((country, number, grade))

n_list.sort(key = lambda x : -x[2])

for co, nu, gr in n_list:
    if cnt == 3:
        break

    if country_dic[co] >= 2:
        continue
    else:
        country_dic[co] += 1
        print(co, nu, sep=" ")
        cnt += 1