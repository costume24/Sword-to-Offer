from exeTime import exeTime
'''题目描述：
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
@exeTime
def Find(target,array):
    if not array:return False
    n,m=len(array),len(array[0])
    i,j=0,m-1
    while i<n and j>=0:
        if array[i][j]==target:
            print("Target found at (%d,%d)"%(i,j))
            return True
        elif array[i][j]>target:j-=1
        else:i+=1
    return False

@exeTime
def Find2(target,array):
    if not array:return False
    n=len(array)
    for i in range(n):
        if target in array[i]:
            return True
    return False



if __name__ == "__main__":
    array=[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    target=5
    print(Find2(target,array))