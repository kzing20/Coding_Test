#어른상어
N = 5 # 격자 크기
M= 4 # 상어 개수
k = 4 #냄새 횟수
grid = [[0, 0, 0, 0, 3], #상어의 위치 격자
        [0, 2, 0, 0, 0],
        [1, 0, 0, 0, 4],
        [0, 0, 0, 0, 0],
        [0, 0 ,0, 0 ,0]]
smell = [[0, 0, 0, 0, 4], #상어의 냄새 격자
        [0, 4, 0, 0, 0],
        [4, 0, 0, 0, 4],
        [0, 0, 0, 0, 0],
        [0, 0 ,0, 0 ,0]]
dir = [4,4,3,1] #처음 방향
priority = [[[2, 3, 1, 4],
             [4, 1, 2, 3],
             [3, 4, 2, 1],
             [4, 3, 1, 2]],

             [[2, 4, 3 ,1],
             [2, 1, 3, 4],
             [3 ,4, 1, 2],
             [4, 1, 2, 3]],

             [[4, 3, 2, 1],
             [1, 4, 3, 2],
             [1, 3 ,2, 4],
             [3, 2, 1, 4]],

             [[3, 4 ,1, 2],
             [3 ,2, 4, 1],
             [1 ,4, 2, 3],
             [1 ,4, 2, 3]]]
# (4,4,4) 상어 번호, 방향, 우선순위 

