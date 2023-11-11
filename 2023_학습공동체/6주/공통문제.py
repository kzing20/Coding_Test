#17142번
#연구소3
import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

INF = 100000
n,m= map(int,input().rstrip().split())
state = [list(map(int,input().rstrip().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(q, blanks): # q:바이러스 위치정보가 저장된 deque, blanks: 빈칸 개수
    visited= [[-1]*n for _ in range(n)]
    time =0
    while True:
        length = len(q) #큐의 길이(=1초 동안 새롭게 추가된 바이러스의 수)
        if blanks ==0 or length ==0: #종료 조건 2가지
            if blanks==0: #모든 빈칸에 바이러스를 퍼뜨리면 종료
                return time
            else: #바이러스를 어떻게 놓아도 전체에 퍼뜨릴 수 없는 경우
                return INF
        time+=1 #1초동안 큐에 새로 추가된 바이러스 수 만큼 탐색-> 완료시 time 1초 추가
        for _ in range(length): #큐 길이만큼 반복
            x, y = q.popleft()
            if visited[x][y] ==-1:
                visited[x][y] =1

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if (0<=nx<n) and (0<=ny<n):
                        if visited[nx][ny] ==-1: #아직 방문하지 않은 칸에 대해
                                if state[nx][ny] ==0: #case 1: 빈 칸
                                     q.append((nx,ny))
                                     visited[nx][ny] =1
                                     blanks-=1
                                elif state[nx][ny] ==2: #case 2: 비활성된 바이러스
                                     q.append((nx,ny))
                                     visited[nx][ny] =1

virus_xy = [] #바이러스의 위치정보
blank_cnt =0 #빈칸 개수

for i in range(n):
    for j in range(n):
        if state[i][j]==0:
            blank_cnt += 1
        if state[i][j] ==2:
            virus_xy.append((i,j))

#활성화 바이러스 m개 선택하는 모든 조합 구하기
virus_comb = combinations(virus_xy, m)

answer = INF
for virus_list in virus_comb:
    q= deque()
    for virus in virus_list:
        q.append(virus)
        #bfs 함수 호출
    tmp = bfs(q,blank_cnt)
    answer = min(answer,tmp)
if answer ==INF:
    print(-1)
else:
     print(answer)