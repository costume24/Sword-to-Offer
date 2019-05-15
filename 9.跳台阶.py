from exeTime import exeTime
@exeTime
def jumpFloor(n):
    f1=1
    f2=2
    f3=3
    if n==1:return f1
    elif n==2:return f2
    elif n==3:return f3
    f=4
    for _ in range(4,n+1):
       f=f3+f2
       f2=f3
       f3=f
    return f

if __name__ == "__main__":
    n=4
    print(jumpFloor(n))

