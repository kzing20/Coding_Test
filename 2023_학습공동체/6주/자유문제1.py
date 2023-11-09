#10871번
N,X = map(int, input().split())
num_list = list(map(int,input().split()))
string = ""
for num in num_list:
    if num<X:
        string+=str(num)
        string+=" "
        
print(string)

# 다른 풀이
# for num in num_list:
#     if num<X:
#         print(num, end=" ")
        
