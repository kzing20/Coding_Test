from copy import deepcopy
### 0. N*N matrix 만들기
def make_matrix(input_list,N):
    a=[[0]*N for i in range(N)] #파이썬 2차원 배열, 모든 원소가 0인 NxN리스트 생성
    a[-1] = input_list
    return a

### 1. 물고기의 수가 가장 적은 어항에 물고기를 한 마리 넣는다.
def add_one_to_min(input_matrix):
    result_matrix = input_matrix.copy()
    copy_list = input_matrix[-1].copy()
    for i,value in enumerate(input_matrix[-1]):
        if value== min(input_matrix[-1]):
            copy_list[i] = value+1
    result_matrix[-1] = copy_list
    return result_matrix

### 2. 어항을 쌓는다
def stack_fish_tank(input_matrix,N):
    result_matrix = deepcopy(input_matrix)
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
    result_matrix = deepcopy(input_matrix)
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
        column_list = [row[c] for row in input_matrix]
        if column_list==compare_list:
            continue
        for i in range(0,N):
            num = list(reversed(column_list))[i]
            if num == 0:
                continue
            result_array.append(num)
    result_matrix[-1] = result_array
    return result_matrix

def count_nonzero_custom(arr):
    count = 0
    for element in arr:
        if element != 0:
            count += 1
    return count

def rotate_180_clockwise(input_list,N):
    new_list = deepcopy(input_list)
    for i in range(N-len(input_list)):
        new_list.append(0)
    new_list = list(reversed(new_list))
    return new_list

### 5. 공중 부양

def fly_fish_bowls(input_matrix, N):
      result_matrix = deepcopy(input_matrix)
      compare_list = [0]*N
      while True:
            zero_row = 0 
            reversed_lists = []
            if count_nonzero_custom(result_matrix[-1])== int(N/4):
                  break
            for i,row in enumerate(result_matrix):       
                  if row== compare_list:
                        zero_row += 1
                  if not(row==compare_list):
                        nonzero_len = count_nonzero_custom(row)
                        start = N - nonzero_len
                        copy_row = deepcopy(row) #deep copy
                        list = copy_row[start:start + int(nonzero_len/2)]
                        result_matrix[i][start:start + int(nonzero_len/2)] = [0] * (start + int(nonzero_len/2) - start)
                        reversed_list = rotate_180_clockwise(list,N)
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