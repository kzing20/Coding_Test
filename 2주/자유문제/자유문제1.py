#1003번

def fibonacci(n):
    zero = [1,0]
    one  = [0,1]
    if(n==0):
        #print("0")
        num = str(zero[0]) + " "+ str(one[0])
        return num
    elif(n==1):
        #print("1")
        num = str(zero[1]) + " "+ str(one[1])
        return num
    else:
        for i in range(n-1):
            zero.append(zero[i]+zero[i+1])
            one.append(one[i]+one[i+1])
        num = str(zero[n]) + " "+ str(one[n])
        return num
T= int(input())

for _ in range(T):
    print(fibonacci(int(input())))

# zero = [1,0,1]
# one = [ 0,1,1]
# def fibonacci(num):
#     length=len(zero)
#     if num>=length:
#         for i in range(length,num+1):
#             zero.append(zero[i-1]+zero[i-2])
#             one.append(one[i-1]+one[i-2])
#     print('{} {}'.format(zero[num],one[num]))

# T=int(input())

# for _ in range(T):
#     fibonacci(int(input()))
