#28278번
#스택 2
import sys
input=sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    command = input().rstrip()
    if len(command)==1: #명령어 개수가 1개일 때
        c = int(command) #명령->정수로 변환
        if c==2:
            if(len(stack)==0): #스택이 비어있다면
                print("-1")
            else:
                print(stack.pop(-1))
        elif c==3:
            print(len(stack))
        elif c==4:
            if(len(stack)==0):
                print("1")
            else:
                print("0")
        elif c==5:
            if(len(stack)==0): #스택이 비어있다면
                print("-1")
            else:
                print(stack[-1])

    else: #명령어 개수가 2개일 때
        x,y =map(int,command.split())
        if x==1:
            stack.append(y)