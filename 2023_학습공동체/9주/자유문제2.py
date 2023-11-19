#팩토리얼 2
#27433번
import sys
input = sys.stdin.readline
n = int(input())

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(n))
