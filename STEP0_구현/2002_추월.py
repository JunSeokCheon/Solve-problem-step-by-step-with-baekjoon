import sys

N = int(sys.stdin.readline())
start_dic = {}
end_list = []
result = 0

for i in range(N):
    start_car = sys.stdin.readline().strip()
    start_dic[start_car] = i

for i in range(N):
    end_car = sys.stdin.readline().strip()
    end_list.append(end_car)

for i in range(N-1):
    for j in range(i+1, N):
        if start_dic[end_list[i]] > start_dic[end_list[j]]:
            result += 1
            break

print(result)
