from exeTime import exeTime

class Solution:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def push(self, node):
        # write code here
        self.s1.insert(0,node)
    def pop(self):
        # return xx
        if len(self.s2)==0:
            while self.s1:
                self.s2.insert(0,self.s1.pop())
        return self.s2.pop()
if __name__ == "__main__":
    so=Solution()
    
    so.push(1)
    so.push(2)
    so.push(3)
    so.pop()
    so.pop()
    so.push(4)
    so.push(5)
    print(so.s1)
    print(so.s2)