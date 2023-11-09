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
# def make_grid(N):
#     arr = [[0 for j in range(N)] for i in range(N)]
#     return arr
# n = int(input())
# grid = make_grid(n)
# print(grid)

# #사과가 존재하는 위치를 1로 바꾸기
# def make_apple(input_mat):
#     k=int(input())
#     for _ in range(k):
#         a,b = map(int, input().split())
#         input_mat[a][b] = 1
#     return input_mat
# grid = make_apple(grid)
# print(grid)
    
info =[]
#방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    #시간과 방향을 튜플 형태로 append
    info.append((int(x),c))

print(info)

