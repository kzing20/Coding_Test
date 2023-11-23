#13460번
#구슬 탈출 2
import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
map =[]
rx,ry,bx,by = 0,0,0,0
for i in range(n):
    row= list(input().strip())
    map.append(row)
    for j in range(m):
        if map[i][j] == "R":
            rx,ry=i,j
        if map[i][j] == "B":
            bx,by = i,j
q = deque()
q.append((rx,ry,bx,by,1))
dx =[0,0,-1,1] #동,서,북,남
dy=[1,-1,0,0]
def move(x, y, dx, dy):
    count = 0 # 이동한 칸 수 
    # 다음 이동이 벽이거나 구멍이 아닐 때까지
    while map[x+dx][y+dy] != '#' and map[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

visited = [(rx,ry,bx,by)]
def bfs():
    while q: # BFS -> queue, while
        rx, ry, bx, by, depth = q.popleft() # FIFO
        if depth > 10: # 10 이하여야 한다.
            break
        for i in range(len(dx)): # 4방향으로 시도한다.
            next_rx, next_ry, r_count = move(rx, ry, dx[i], dy[i]) # RED
            next_bx, next_by, b_count = move(bx, by, dx[i], dy[i]) # BLUE
                        
            if map[next_bx][next_by] == 'O': # 파란 구슬이 구멍에 떨어지지 않으면(실패 X)
                continue
            if map[next_rx][next_ry] == 'O': # 빨간 구슬이 구멍에 떨어진다면(성공)
                print(depth)
                return
            if next_rx == next_bx and next_ry == next_by : # 빨간 구슬과 파란 구슬이 동시에 같은 칸에 있을 수 없다.
                if r_count > b_count: # 이동 거리가 많은 구슬을 한칸 뒤로
                    next_rx -= dx[i]
                    next_ry -= dy[i]
                else:
                    next_bx -= dx[i]
                    next_by -= dy[i]
            # 방문 여부 확인 
            if (next_rx, next_ry, next_bx, next_by) not in visited:
                visited.append((next_rx,next_ry, next_bx, next_by))
                q.append((next_rx, next_ry, next_bx, next_by, depth +1))
    print(-1) # 실패 

bfs()