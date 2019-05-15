from exeTime import exeTime
@exeTime
def rectCover(number):
    '''仍然是斐波那契数列的变种
    '''
    if number==0:return 0
    if number==1:return 1
    if number==2:return 2
    num1=1
    num2=2
    res=3
    for _ in range(3,number+1):
        res=num1+num2
        num1=num2
        num2=res
    return res

@exeTime
def re2(number):
    if number < 1:
        return 0
    p = q = r =0
    for i in range(1,number+1):
        if i == 1:
            p = q = r =1
        elif i == 2:
            q = r = 2
        else:
            r = q + p
            p = q
            q = r
    return r
if __name__ == "__main__":
    n=50
    print(rectCover(n))
    print(re2(n))