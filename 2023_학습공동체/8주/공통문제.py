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
print(command_list)
dice = [0] *6 #초기 주사위(동,서,남,북,위,아래)