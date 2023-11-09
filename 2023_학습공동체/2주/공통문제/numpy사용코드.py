import numpy as np
### 0. N*N matrix 만들기
def make_matrix(input_list,N):
    a=[[0]*N for i in range(N)] #파이썬 2차원 배열, 모든 원소가 0인 NxN리스트 생성
    a[-1] = input_list
    return a

### 1. 물고기의 수가 가장 적은 어항에 물고기를 한 마리 넣는다.
def add_one_to_min(input_matrix):
    result_matrix = np.copy(input_matrix)
    copy_list = input_matrix[-1].copy()
    for i,value in enumerate(input_matrix[-1]):
        if value== min(input_matrix[-1]):
            copy_list[i] = value+1
    result_matrix[-1] = copy_list
    return result_matrix

### 2. 어항을 쌓는다
def stack_fish_tank(input_matrix,N):
    result_matrix = np.copy(input_matrix)
    pivot,w,h = 1,1,1
    idx = 0
    while True:
        if (pivot-1+w+h>N): #종료 조건
            break
        for c in range(pivot-1, pivot-1 + w):
            for r in range(-1, -h - 1, -1):
                nextR = - w + c - pivot
                nextC = pivot-1 +w -(r+1)
                result_matrix[nextR][nextC] = result_matrix[r][c]
                result_matrix[r][c] = 0
        pivot += (idx // 2 + 1)
        if idx % 2 == 1:
            w += 1
        else:
            h += 1
        idx += 1
    return result_matrix

### 3. 어항에 있는 물고기 수 조절
def control_fish_num(input_matrix,N):
    result_matrix = np.copy(input_matrix)
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    for x in range(0,N):
        for y in range(0,N):
            for i in range(0,4):
                nextX = x + dx[i]
                nextY = y + dy[i]
                if (nextX<0) or (nextX>N-1) or (nextY<0) or (nextY>N-1):
                    continue
                if (input_matrix[nextX][nextY] ==0):
                    continue
                if (input_matrix[x][y]> input_matrix[nextX][nextY]):
                    diff = (input_matrix[x][y] - input_matrix[nextX][nextY]) //5
                    result_matrix[x][y] -= diff
                    result_matrix[nextX][nextY] += diff
    return result_matrix

### 4. 어항을 바닥에 일렬로 놓기
def spread_fish(input_matrix,N):
    result_matrix = [[0]*N for i in range(N)]
    compare_list = [0]*N
    result_array = []
    for c in range(0,N):
        if np.array_equal(input_matrix[:,c],compare_list):
            continue
        for i in range(0,N):
            num = np.flip(input_matrix[:,c])[i]
            if num == 0:
                continue
            result_array.append(num)
    result_matrix[-1] = result_array
    return result_matrix


### 5. 공중 부양
# 180 도 회전
def rotate_180_clockwise(input_list):
    new_list = np.copy(input_list)
    new_list = np.flip(np.append(new_list,[0]*(N-len(input_list))))
    return new_list
def fly_fish_bowls(input_matrix, N):
      result_matrix = np.copy(input_matrix)
      compare_list = [0]*N
      while True:
            zero_row = 0 
            reversed_lists = []
            if np.count_nonzero(result_matrix[-1])== int(N/4):
                  break
            for i,row in enumerate(result_matrix):       
                  if np.array_equal(row, compare_list):
                        zero_row += 1
                  if not(np.array_equal(row,compare_list)):
                        nonzero_len = np.count_nonzero(row)
                        start = N - nonzero_len
                        copy_row = np.copy(row) #deep copy
                        list = copy_row[start:start + int(nonzero_len/2)]
                        result_matrix[i][start:start + int(nonzero_len/2)] =0
                        reversed_list = rotate_180_clockwise(list)
                        reversed_lists.append(reversed_list)
                        
                        nonzero_row = N-zero_row

            for i,list in enumerate(reversed_lists):
                  result_matrix[(-1)*(i+nonzero_row+1)][:] = list
      return result_matrix

def get_result(input_matrix):
    input_list = input_matrix[-1]
    result_diff = max(input_list)-min(input_list)
    return result_diff

answer = 0

N, K = input().split()
N, K = int(N), int(K)
input_list = list(map(int, input().split()))

result_matrix = make_matrix(input_list,N)

while True:
    result = get_result(result_matrix)

    if result <= K:
        print(answer)
        break

    test_matrix_2 = add_one_to_min(result_matrix)
    stack_matrix = stack_fish_tank(test_matrix_2,N)
    control_matrix = control_fish_num(stack_matrix,N)
    spread_matrix = spread_fish(control_matrix,N)
    fly_matrix = fly_fish_bowls(spread_matrix,N)
    control_matrix_2 = control_fish_num(fly_matrix,N)
    result_matrix = spread_fish(control_matrix_2,N)

    answer += 1