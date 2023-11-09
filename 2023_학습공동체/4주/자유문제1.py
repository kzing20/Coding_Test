#8393번
def cal_sum(n):
    sum =0
    for i in range(n+1):
        sum+=i
    return sum
n = int(input())
print(cal_sum(n))