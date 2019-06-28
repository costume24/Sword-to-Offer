from exeTime import exeTime
from multitimes import multitimes

class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        '''两个指针small和big，分别初始化为1和2.
        重复以下步骤：
            1.计算small+big，若小于tsum，则增大big（序列末尾加上一个新数），
            若大于tsum，则增大small（去掉序列的第一个数）
        '''
        res=[]
        if tsum<3:return []
        if tsum==3:return [1,2]
        small=1
        big=2
        while big<=tsum/2+1:
            if self.do_sum(small,big)<tsum:
                big+=1
            elif self.do_sum(small,big)>tsum:
                small+=1
            else:
                res.append(range(small,big+1))
                small+=1
        return res
    
    def do_sum(self,start,end):
        return (start+end)*(end-start+1)/2

if __name__ == "__main__":
    so=Solution()
    tsum=9
    print(so.FindContinuousSequence(tsum))
    