<<<<<<< HEAD
import sys

b, s, d = map(int, sys.stdin.readline().split())
b_list = list(map(int, sys.stdin.readline().split()))
s_list = list(map(int, sys.stdin.readline().split()))
d_list = list(map(int, sys.stdin.readline().split()))
sale_price = 0
origin_price = sum(b_list) + sum(s_list) + sum(d_list)

b_list.sort(reverse=True)
s_list.sort(reverse=True)
d_list.sort(reverse=True)

min_value = min(b, s, d)

for i in range(min_value):
    sale_price += (b_list[i] + s_list[i] + d_list[i]) * 0.9

sale_price += sum(b_list[min_value:])
sale_price += sum(s_list[min_value:])
sale_price += sum(d_list[min_value:])

print(origin_price)
=======
import sys

b, s, d = map(int, sys.stdin.readline().split())
b_list = list(map(int, sys.stdin.readline().split()))
s_list = list(map(int, sys.stdin.readline().split()))
d_list = list(map(int, sys.stdin.readline().split()))
sale_price = 0
origin_price = sum(b_list) + sum(s_list) + sum(d_list)

b_list.sort(reverse=True)
s_list.sort(reverse=True)
d_list.sort(reverse=True)

min_value = min(b, s, d)

for i in range(min_value):
    sale_price += (b_list[i] + s_list[i] + d_list[i]) * 0.9

sale_price += sum(b_list[min_value:])
sale_price += sum(s_list[min_value:])
sale_price += sum(d_list[min_value:])

print(origin_price)
>>>>>>> ed80e6f384bbb3a2416d12cf980d93d10f1cbabb
print(int(sale_price))