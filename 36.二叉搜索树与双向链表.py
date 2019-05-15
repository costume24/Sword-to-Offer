from exeTime import exeTime


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def initTree(self):
        t0 = TreeNode(10)
        t1 = TreeNode(6)
        t2 = TreeNode(14)
        t3 = TreeNode(4)
        t4 = TreeNode(8)
        t5 = TreeNode(12)
        t6 = TreeNode(16)

        t0.left = t1
        t0.right = t2
        t1.left = t3
        t1.right = t4
        t2.left = t5
        t2.right = t6
        return t0


class Solution:
    def Convert(self, pRootOfTree):
        '''中序遍历以后改变指针方向
        '''
        if not pRootOfTree: return None
        res = []
        res = self.midConvert(pRootOfTree, res)
        for i in range(len(res)):
            if i > 0:
                res[i].left = res[i - 1]
            if i < len(res) - 1:
                res[i].right = res[i + 1]
        return res[0]

    def midConvert(self, root, res):
        if not root: return
        if root.left:
            self.midConvert(root.left, res)
        res.append(root)
        if root.right:
            self.midConvert(root.right, res)
        return res


if __name__ == "__main__":
    node = TreeNode(0)
    root = node.initTree()
    so = Solution()
    res = so.Convert(root)
