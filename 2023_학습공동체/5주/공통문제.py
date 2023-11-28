#청소년 상어
import copy

array = [[None]*4 for _ in range(4)]

for i in range(4):
    data= list(map(int,input().split()))
    for j in range(4):
        #각 위치에 [물고기 번호, 방향] 저장
        array[i][j] = [data[j*2],data[j*2+1]-1]

#순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

def turn_left(direction):
    return (direction+1)%8

#현재 배열에서 특정 번호의 물고기 위치 찾는 함수
def find_fish(array,index):#공간 정보가 들어있는 배열, 물고기 번호
    for i in range(4):
        for j in range(4):
            if array[i][j][0] ==index:
                return (i,j)
    #해당 물고기가 없으면 None return
    return None

#모든 물고기를 회전 및 이동시키는 함수
def move_fishes(array, now_x, now_y): #상어의 현재 위치를 인자로 넣어준다
    #1부터 16번까지 물고기를 차례대로 확인
    for i in range(1,17):
        #해당 물고기의 위치 찾기
            position =find_fish(array,i)
            if position!=None:
                x,y = position[0],position[1]
                direction=array[x][y][1]
                #현재 direction부터 반시계 방향으로 검사
                for _ in range(8):
                    nx = x+dx[direction]
                    ny = y+dy[direction]
                    #벽이 아닐 조건
                    if 0<=nx and nx<4 and 0<=ny and ny<4:
                        #상어 위치가 아닐 조건
                        if not(nx==now_x and ny==now_y):
                            array[x][y][1] = direction
                            array[x][y],array[nx][ny] = array[nx][ny],array[x][y]
                            break
                    direction = turn_left(direction)
#상어가 현재 위치에서 먹을 수 있는 모든 물고기의 위치 반환
def get_possible_positions(array,now_x,now_y):
    positions =[]
    direction = array[now_x][now_y][1]
    for _ in range(3):
        now_x+=dx[direction]
        now_y+=dy[direction]
        if 0<=now_x and now_x<4 and 0<=now_y and now_y<4:
            if array[now_x][now_y][0]!=-1:
                positions.append((now_x,now_y))
    return positions

#모든 경우 탐색(dfs)
result=0
def dfs(array,now_x,now_y,total):
    global result
    array = copy.deepcopy(array)

    total+=array[now_x][now_y][0] #현재 위치의 물고기 먹기
    array[now_x][now_y][0] = -1

    move_fishes(array,now_x,now_y) 

    positions= get_possible_positions(array,now_x,now_y)

    if len(positions)==0:
        result = max(result,total)
        return
    for next_x,next_y in positions:
        dfs(array,next_x,next_y,total)

dfs(array,0,0,0)
print(result)