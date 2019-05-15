from exeTime import exeTime
import numpy as np
@exeTime
def quickSort(lyst,start,end,name='Random'):
    '''快速排序
    选择一个主元，每一趟排序将小于主元的数移到其左边
    大于主元的数移到其右边。
    一趟排序后，主元的位置就是其排好序的最终位置
    '''
    if start<end:
        q=partion(lyst,start,end,name)
        quickSort(lyst,start,q-1,name)
        quickSort(lyst,q+1,end,name)
    return lyst

def partion(lyst,start,end,name='Random'):
    '''快排的核心方法。
    根据相对主元的大小移动位置
    '''
    pivot=selectPivot(lyst,start,end,name)   # 选择主元
    #print('Start from pivot: ',lyst[pivot])
    x=lyst[pivot]
    swap(lyst,end,pivot)                 # 将主元移到最后
    i=start-1
    for j in range(start,end):
        if lyst[j]<=x:
            i+=1						# 若要改为非递增排序，则改为大于等于
            swap(lyst,i,j)
    swap(lyst,i+1,end)
    #print(lyst)
    return i+1
    
def selectPivot(lyst,start,end,name='Random'):
    if name=='Random':						# 随机选择主元
        def randomlySelect(start,end):
            k=np.random.randint(start,end+1)
            return k
        return randomlySelect(start,end)
    elif name=='First':						# 以第一个数作为主元
        return start
    elif name=='Last':						# 以最后一个数作为主元
        return end
    elif name=='Three':						# 三者取中法获得主元
        def threeMidium(lyst,start,end):
            '''离平均值最近的就是中值
            '''
            mid=int((start+end)/2)  
            tmp=np.array([lyst[start],lyst[mid],lyst[end]])
            res=[start,mid,end]				# 返回的是在原数组中的序号
            diff=abs(tmp-np.mean(tmp))
            #print('tmp=',tmp,'mid= ',tmp[np.where(diff==min(diff))[0][0]])
            return res[np.where(diff==min(diff))[0][0]]  
        return threeMidium(lyst,start,end) 
    elif name=='Mid':						# 以中间位置处的数作为主元
        def selectMid(lyst,start,end):
            mid=int((start+end)/2)
            return mid
        return selectMid(lyst,start,end)


def swap(lyst,i,j):
    lyst[i],lyst[j]=lyst[j],lyst[i]

if __name__ == "__main__":
    lyst=np.random.randint(1,30,10)
    np.random.shuffle(lyst)
    print(lyst)
    print('三者取中法：')
    print(quickSort(lyst,0,len(lyst)-1,name='Three'))
    print('取中位数：')
    print(quickSort(lyst,0,len(lyst)-1,name='Mid'))
    print('随机取主元')
    print(quickSort(lyst,0,len(lyst)-1))
