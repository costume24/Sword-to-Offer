from exeTime import exeTime
@exeTime
def Fibonacci(n,count):
    '''最原始的递归解法，重复计算很多，效率极低
    n=3时计算5次，n=5时计算15次
    '''
    count[0]+=1
    if n==0:return 0
    if n==1:return 1
    return Fibonacci(n-1,count)+Fibonacci(n-2,count)

@exeTime
def Fibonacci2(n):
    '''复杂度为O(n)的动态规划算法
    自底向上，推导出F(n)
    '''
    res=[0,1]
    if n==0:return res[0]
    if n==1:return res[1]
    fibNMinusOne=1
    fibNMinusTwo=0
    fibN=1
    for _ in range(2,n+1):
        fibN=fibNMinusOne+fibNMinusTwo
        fibNMinusTwo=fibNMinusOne
        fibNMinusOne=fibN
    return fibN

@exeTime
def Fibonacci3(n):
    '''备忘录法
    用一个数组保存求出的斐波那契数列的每一个值。计算的时候如果发现已经计算过了，则直接调用。
    '''
    tmp=[-1]*(n+1)
    tmp[0]=0
    tmp[1]=1
    fibo3(n,tmp)
    return tmp[n]
def fibo3(n,tmp):
    if tmp[n]!=-1:return tmp[n]
    else:
        tmp[n]=fibo3(n-1,tmp)+fibo3(n-2,tmp)
        return tmp[n]



if __name__ == "__main__":
    n=20
    count=[0]
    print(Fibonacci(n,count))
    print(count[0])
    print(Fibonacci2(n))
    print(Fibonacci3(n))
