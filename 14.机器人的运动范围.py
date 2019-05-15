from exeTime import exeTime
class Solution:
    @exeTime
    def movingCount(self,threshold,rows,cols):
        '''回溯法
        '''
        if rows<1 or cols<1:return 0
        used=[[0 for i in range(cols)] for j in range(rows)]
        i,j=0,0
        count=[0]
        self.find(used,i,j,rows,cols,threshold,count)
        return count[0]

    def find(self,used,i,j,rows,cols,threshold,count):
        if i>=rows or j>=cols or used[i][j]==1 or not self.check(threshold,i,j):return 0
        used[i][j]=1
        count[0]+=1
        if i+1<rows and self.check(threshold,i+1,j) and used[i+1][j]==0:
            self.find(used,i+1,j,rows,cols,threshold,count)

        if i-1>=0 and self.check(threshold,i-1,j) and used[i-1][j]==0:
            self.find(used,i-1,j,rows,cols,threshold,count)

        if j+1<cols and self.check(threshold,i,j+1) and used[i][j+1]==0:
            self.find(used,i,j+1,rows,cols,threshold,count)

        if j-1>=0 and self.check(threshold,i,j-1) and used[i][j-1]==0:
            self.find(used,i,j-1,rows,cols,threshold,count)
        return 0

    def check(self,k,i,j):
        if k>=sum(list(map(int,str(i)+str(j)))):return True
        else:return False

if __name__ == "__main__":
    so=Solution()
    threshold,rows,cols=-10,10,10
    print(so.movingCount(threshold,rows,cols))