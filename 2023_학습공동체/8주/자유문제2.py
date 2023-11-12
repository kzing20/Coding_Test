#18258번
#큐2
from collections import deque
import sys
input= sys.stdin.readline
n=int(input())
queue = deque()
for _ in range(n):
    command = input().split()
    if command[0]=="push":
        x= int(command[1])
        queue.append(x)
    elif command[0]=="pop":
        if len(queue)==0:
            print("-1")
        else:
            print(queue.popleft())
    elif command[0]=="size":
        print(len(queue))
    elif command[0]=="empty":
        if len(queue)==0:
            print("1")
        else:
            print("0")
    elif command[0]=="front":
        if len(queue)==0:
            print("-1")
        else:
            print(queue[0])
    elif command[0]=="back":
        if len(queue)==0:
            print("-1")
        else:
            print(queue[-1])
