#2738번
#행렬 덧셈
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
a=[]
b=[]
for _ in range(n):
    row = list(map(int,input().split()))
    a.append(row)
for _ in range(n):
    row = list(map(int,input().split()))
    b.append(row)

for row in range(n):
    for col in range(m):
        print(a[row][col] + b[row][col], end=' ')
    print()
