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
    def traversal_mid_recur(self, pRootOfTree):
        '''二叉树中序遍历递归版本
        '''
        if not pRootOfTree: return None
        res = []
        return self.mid(pRootOfTree, res)

    def mid(self, root, res):
        if not root: return
        if root.left:
            self.mid(root.left, res)
        res.append(root.val)
        if root.right:
            self.mid(root.right, res)
        return res


if __name__ == "__main__":
    so = Solution()
    node = TreeNode(0)
    root = node.initTree()
    print(so.traversal_mid_recur(root))