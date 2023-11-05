#25314번
def Nbyte(n):
    num = int(n/4)
    str = ""
    for _ in range(num):
        str+="long "
    str+="int"
    print(str)

N = int(input())
Nbyte(N)