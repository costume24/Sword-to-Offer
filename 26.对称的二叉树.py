from exeTime import exeTime


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def initTree(self):
        t0 = TreeNode(8)
        t1 = TreeNode(6)
        t2 = TreeNode(6)
        t3 = TreeNode(5)
        t4 = TreeNode(7)
        t5 = TreeNode(7)
        t6 = TreeNode(5)

        t0.left = t1
        t0.right = t2
        t1.left = t3
        t1.right = t4
        t2.left = t5
        t2.right = t6
        return t0


class Solution:
    @exeTime
    def isSymmetrical(self, pRoot):
        """通过比较二叉树的前序遍历序列和对称前序遍历序列判断
        """
        if not pRoot: return True
        foreRes = []
        symForeRes = []
        self.foreTraverse(pRoot, foreRes)
        self.symForeTraverse(pRoot, symForeRes)
        return True if foreRes == symForeRes else False

    def foreTraverse(self, root, res):
        """前序遍历二叉树：根，左，右
        """
        if not root:
            res.append(None)
            return
        res.append(root.val)
        self.foreTraverse(root.left, res)
        self.foreTraverse(root.right, res)
        return res

    def symForeTraverse(self, root, res):
        """对称前序遍历二叉树：根，右，左
        """
        if not root:
            res.append(None)
            return
        res.append(root.val)
        self.symForeTraverse(root.right, res)
        self.symForeTraverse(root.left, res)
        return res


if __name__ == "__main__":
    node = TreeNode(0)
    root = node.initTree()
    so = Solution()
    print(so.isSymmetrical(root))