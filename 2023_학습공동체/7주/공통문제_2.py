#뱀 문제
#3190번
# 첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 
# 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)

# 다음 K개의 줄에는 사과의 위치가 주어지는데,
# 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 
# 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.

# 다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)

# 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데, 
#정수 X와 문자 C로 이루어져 있으며. 게임 시작 시간으로부터 
#X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. 
# X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

#L값 입력했을 때 격자 만드는 함수(배열의 요소가 모두 0) -> 뱀이 지나가면 2로 바꾸기
def make_grid(N):
    arr = [[0 for j in range(N)] for i in range(N)]
    arr[0][0]=2 #뱀의 시작 위치
    return arr
n = int(input())
grid = make_grid(n)

#사과가 존재하는 위치를 1로 바꾸기
def make_apple(input_mat):
    k=int(input())
    for _ in range(k):
        a,b = map(int, input().split())
        input_mat[a-1][b-1] = 1
    return input_mat
grid = make_apple(grid)
info =[]
#방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    #시간과 방향을 튜플 형태로 append
    info.append((int(x),c))

#방향 전환하는 함수
direction = 0 #동,서,남,북 index
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def turn(direction,c):
    if c=='L': #왼쪽으로 턴
        if(direction==0):#동
            direction=3 #북
        elif(direction==1): #서
            direction=2 #남
        elif(direction==2): #남
            direction=0 #동
        else: #북
            direction=1 #서
    else: #오른쪽으로 턴
        if(direction==0): #동
            direction=2 #남
        elif(direction==1): #서
            direction=3 #북
        elif(direction==2): #남
            direction=1 #서
        else: #북
            direction=0 #동
    return direction


answer =0
loc_x = 0
loc_y = 0
turn_num = 0 #방향 바꾸는 횟수
tail = [(loc_x,loc_y)] #꼬리 위치
while(True):
    
    new_loc_x = loc_x + dx[direction]
    new_loc_y = loc_y + dy[direction]
    if(new_loc_x<0 or new_loc_x>n-1 or new_loc_y<0 or new_loc_y>n-1):
        answer+=1
        break
    elif(grid[new_loc_x][new_loc_y]==2):
        answer+=1
        break
    else:
        
        if(grid[new_loc_x][new_loc_y]==0):
            tx,ty = tail.pop(0)
            grid[tx][ty] = 0 #꼬리 제거
        grid[new_loc_x][new_loc_y] = 2
        tail.append((new_loc_x, new_loc_y))
        loc_x,loc_y = new_loc_x,new_loc_y
        answer+=1
       
    if(turn_num<l and answer==info[turn_num][0]):
        direction = turn(direction,info[turn_num][1])
        turn_num+=1
print(answer)

