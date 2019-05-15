from exeTime import exeTime
class Solution:
    @exeTime
    def hasPath(self,matrix,rows,cols,path):
        '''回溯法
        '''
        if not matrix or rows<1 or cols<1 or not path:
            return False
        index=0
        # 是否已i案例过
        used=[[0 for i in range(cols)] for j in range(rows)]            # 不能使用numpy，系统不通过
        mat=[[0 for i in range(cols)] for j in range(rows)]
        count=0
        # 此处可优化，不需要转换为二维矩阵
        for i in range(rows):
            for j in range(cols):
                mat[i][j]=matrix[count]
                count+=1
        # 可视化，用于调试
        for i in range(rows):
            for j in range(cols):
                if j==cols-1:
                    print(mat[i][j])
                else:
                    print(mat[i][j],end=' ')
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==path[index]:                              # 找到path的第一个元素
                    if self.findPath(i,j,path,index,mat,used,rows,cols):
                        return True
        return False

    def findPath(self,i,j,path,index,mat,used,rows,cols):
        if index==len(path)-1:return True                               # 递归的结束条件：到达path末尾
        used[i][j]=1
        if i+1<rows and used[i+1][j]==0 and mat[i+1][j]==path[index+1]: # 判断四个方向是否有path的字符
            print(mat[i+1][j])
            print(path[index+1])
            index+=1                        
            if self.findPath(i+1,j,path,index,mat,used,rows,cols):return True
            index-=1                                                    # 回溯到上一个状态
        if i-1>=0 and used[i-1][j]==0 and mat[i-1][j]==path[index+1]:
            print(mat[i-1][j])
            print(path[index+1])            
            index+=1
            if self.findPath(i-1,j,path,index,mat,used,rows,cols): return True
            index-=1
        if j+1<cols and used[i][j+1]==0 and mat[i][j+1]==path[index+1]:
            print(mat[i][j+1])
            print(path[index+1])
            index+=1
            if self.findPath(i,j+1,path,index,mat,used,rows,cols):return True
            index-=1
        if j-1>=0 and used[i][j-1]==0 and mat[i][j-1]==path[index+1]:
            print(mat[i][j-1])
            print(path[index+1])
            index+=1
            if self.findPath(i,j-1,path,index,mat,used,rows,cols):return True
            index-=1
        used[i][j]=0                                                       # used也需要回溯到上一个状态
        return False

if __name__ == "__main__":
    # matrix=[
    #     ['a','b','c','e'],
    #     ['s','f','c','s'],
    #     ['a','d','e','e']
    # ]
    # rows=len(matrix)
    # cols=len(matrix[0])
    so=Solution()
    matrix='ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS'
    path='SGGFIECVAASABCEHJIGQEM'
    rows,cols=5,8
    print(so.hasPath(matrix,rows,cols,path))



