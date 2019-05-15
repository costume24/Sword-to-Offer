from exeTime import exeTime


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def initTree(self):
        t0 = TreeNode(8)
        t1 = TreeNode(8)
        t2 = TreeNode(9)
        t3 = TreeNode(2)
        t4 = TreeNode(5)
        # t5 = TreeNode(4)
        # t6 = TreeNode(7)

        t0.right = t1
        t1.right = t2
        t2.right = t3
        t3.right = t4
        # t4.left = t5
        # t4.right = t6

        a0 = TreeNode(8)
        a1 = TreeNode(9)
        a2 = TreeNode(3)
        a3 = TreeNode(2)
        a0.right = a1
        a1.left = a2
        a1.right = a3
        return t0, a0


class Solution:
    @exeTime
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2: return None
        root1 = pRoot1
        root2 = pRoot2
        return self.findRoot(root1, root2)

    def doTree(self, root1, root2):
        '''
        判断两棵树是否相等
        '''
        if not root2: return True  # B到达叶节点，返回True
        if not root1 or root1.val != root2.val:
            return False  # A到达叶节点或两个节点不相等，返回False
        return self.doTree(root1.left, root2.left) and \
            self.doTree(root1.right, root2.right)

    def findRoot(self, root1, root2):
        '''
        若找到相同的根节点，则判断是否相等
        否则继续寻找，直至
        '''
        if not root1: return False
        flag = False

        if root1.val == root2.val:
            flag = self.doTree(root1, root2)
        if not flag:
            flag = self.findRoot(root1.left, root2)
        if not flag:
            flag = self.findRoot(root1.right, root2)
        return flag


if __name__ == "__main__":
    node = TreeNode(0)
    so = Solution()
    pRoot1, pRoot2 = node.initTree()
    print(so.HasSubtree(pRoot1, pRoot2))
