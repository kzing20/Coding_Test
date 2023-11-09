#뱀 10875번
#L값 입력했을 때 격자 만드는 함수(배열의 요소가 모두 0) -> 뱀이 지나가면 1로 바꾸기
def make_grid(L):
    n = 2*L +1
    arr = [[0 for j in range(n)] for i in range(n)]
    return arr
print(make_grid(3))

#뱀이 숨을 거두는 조건 검사하는 함수

#방향과 시간을 입력받아 뱀이 움직이는 함수

#뱀이 몇 초 후에 숨을 거두는지 계산하는 함수
