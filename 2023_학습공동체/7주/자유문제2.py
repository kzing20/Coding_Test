#2750번
#수 정렬하기
N= int(input())
my_list =[]
for _ in range(N):
    my_list.append(int(input()))
my_list = sorted(my_list)
for i in range(N):
    print(my_list[i])