# # 시간초과
# def d(n):
#     for num in range(1,n):
#         num_sum = num
#         num = str(num)
#         for separate_num in num:
#             num_sum += int(separate_num)
        
#         if num_sum == n:
#             return "no"
        
#     return "yes"

# if __name__ == '__main__':
#     for i in range(1, 10000):
#         if d(i) == "yes":
#             print(i)
#         else:
#             continue

total_num = list(range(1,10001))
generated_num = []

for num in total_num:
    num_sum = num
    num = str(num)
    for mini_num in num:
        num_sum += int(mini_num)
        
    if num_sum <= 10000:
        generated_num.append(num_sum)

generated_num = set(generated_num)
for num in generated_num:
    total_num.remove(int(num))

for num in total_num:
    print(num)