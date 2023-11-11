#바이러스 
#백준 2606번

# 1. 입력 및 초기화
n = int(input())
c = int(input())
info =[]
for _ in range(c):
    c1,c2 = map(int,input().split())
    info.append((c1-1,c2-1))

# 2. graph에 연결 정보 채우기
graph =[[0 for _ in range(n)] for _ in range(n)]
for list in info:
    c1,c2 = list
    graph[c1][c2] =1
    graph[c2][c1] =1

# 3. dfs
visited = [0 for _ in range(n)]
def dfs(idx):
    visited[idx] =1
    for i in range(n):
        if visited[i]==0 and graph[idx][i]==1:
            dfs(i)
dfs(0)
print(visited.count(1)-1)