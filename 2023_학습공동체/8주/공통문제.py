#14499번
#주사위 굴리기
import sys
input = sys.stdin.readline
n,m,x,y,k = map(int,input().split())
map_info =[]
for _ in range(n):
    row = list(map(int,input().split()))
    map_info.append(row)
command_list =list(map(int,input().split()))
dice = [0] *6 #초기 주사위(오른쪽, 왼쪽, 앞, 뒤, 위, 아래)
def turn(command,dice):
    right, left, front, back, up, down =dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]
    if command ==1: #동
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = down, up,front,back,right,left
    elif command==2: #서
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = up,down,front,back,left,right
    elif command==3: #북
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = right,left, up,down,back,front
    elif command ==4:#남
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = right, left, down, up, front, back
    return dice
dx =[0,0,-1,1] #동,서,북,남
dy=[1,-1,0,0]
nx,ny = x,y
for command in command_list:
    nx +=dx[command-1]
    ny +=dy[command-1]
    if nx<0 or nx>=n or ny<0 or ny>=m:
        nx -=dx[command-1]
        ny -= dy[command-1]
        continue 
    dice = turn(command,dice)
    if map_info[nx][ny] ==0:
        map_info[nx][ny] = dice[5] #주사위 바닥면의 숫자가 map에 복사
    else:
        dice[5] = map_info[nx][ny] #칸의 숫자가 주사위 바닥면으로 복사
        map_info[nx][ny] =0
    print(dice[4])

