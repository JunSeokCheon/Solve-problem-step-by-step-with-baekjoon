# 정확도는 100점, 효율성 0점
# 이유는 로직은 맞으나 모든 경우를 다 순회해서 석유 개수를 다 구해서여서 시간이 오래 걸린다.
# 해결책 ? : 각 석유의 그룹을 구하고, 그룹의 석유 개수를 먼저 저장한다. 그리고, 열에 따라 시추선을 누르며 거쳐간 석유 그룹을 파악 후 개수를 더해서 최대 값 갱신을 한다?
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(cross_land, n, m, i, idx, visited):
    que = deque()
    que.append((i, idx))
    visited[i][idx] = 1
    count = 1
    
    while que:
        x, y = que.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if cross_land[nx][ny] != 0 and visited[nx][ny] == 0:
                que.append((nx,ny))
                visited[nx][ny] = 1
                count += 1
        
    return count
     

def solution(land):
    answer = []
    cross_land = [[0] * len(land) for _ in range(len(land[0]))]
    
    for i in range(len(land)):
        for j in range(len(land[0])):
            cross_land[j][i] = land[i][j]
    # print(cross_land)
    for i in range(len(cross_land)):
        visited = [[0] * len(cross_land[0]) for _ in range(len(cross_land))]
        mini_count = 0
        for idx, num in enumerate(cross_land[i]):
            # print(i, idx, answer, visited)
            if num == 1 and visited[i][idx] == 0: 
                mini_count += bfs(cross_land, len(cross_land), len(cross_land[0]), i, idx, visited)
        answer.append(mini_count)
    
    return max(answer)


# 수정안
# 정확성 100점, 효율성 100점
from collections import deque

# 그룹, 방문 여부, 그룹 넘버 변수
group, visited = {}, {}
group_count = 0
n, m = 0, 0
DIR = [(0, -1), (0, 1), (1, 0), (-1, 0)]  # 이동 방향 정의

def bfs(sx, sy, visited, group, land):

    #너비 우선 탐색을 통해 그룹을 찾아내고 그룹의 크기를 계산

    global group_count, n, m
    count = 1
    q = deque([(sx, sy)])
    visited[(sx, sy)] = group_count

    while q:
        x, y = q.popleft()

        for dx, dy in DIR:
            nx, ny = x + dx, y + dy

            # 유효한 범위 내에 있고, 석유가 들었고 방문하지 않았다면 추가
            if 0 <= nx < n and 0 <= ny < m and land[nx][ny] != 0 and (nx, ny) not in visited:
                visited[(nx, ny)] = group_count
                q.append((nx, ny))
                count += 1

    group[group_count] = count
    group_count += 1


def solution(land):
    global n, m
    n, m = len(land), len(land[0])

    # 모든 지점을 탐색하면서 그룹을 찾음
    for row in range(n):
        for col in range(m):
            if (row, col) not in visited and land[row][col] != 0:
                bfs(row, col, visited, group, land)

    maximum = 0

    # 각 열에 대해 최대 그룹 크기를 계산
    for col in range(m):
        already_gone = {}
        ret = 0

        for row in range(n):
            if land[row][col] != 0:
                cur_group = visited[(row, col)]

                # 이미 계산한 그룹이면 skip
                if cur_group in already_gone:
                    continue

                cur_count = group[cur_group]
                ret += cur_count
                already_gone[cur_group] = True

        maximum = max(maximum, ret)

    return maximum