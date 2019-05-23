from exeTime import exeTime


# -*- coding:utf-8 -*-
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
        t7 = TreeNode(20)
        t8 = TreeNode(22)

        t0.left = t1
        t0.right = t2
        t1.left = t3
        t1.right = t4
        t2.left = t5
        t2.right = t6
        t6.left = t7
        t7.right = t8
        return t0


class Solution:
    @exeTime
    def TreeDepth(self, pRoot):
        '''前序遍历，得到每个叶子节点到根的距离
        '''
        if not pRoot: return 0
        res = []
        dist = []
        self.fore_traversal(pRoot, res, dist)
        return max(dist)

    def fore_traversal(self, root, res, dist):
        if root is None: return
        res.append(root.val)
        if root.left:
            self.fore_traversal(root.left, res, dist)
        if root.right:
            self.fore_traversal(root.right, res, dist)
        if not root.left and not root.right:
            dist.append(len(res))
        res.pop()
        return

    @exeTime
    def TreeDepth2(self, pRoot):
        return self.do(pRoot)

    def do(self, pRoot):
        if pRoot is None: return 0
        nleft = self.do(pRoot.left)
        nright = self.do(pRoot.right)
        return nleft + 1 if nleft > nright else nright + 1


if __name__ == "__main__":
    so = Solution()
    node = TreeNode(0)
    root = node.initTree()
    print(so.TreeDepth(root))
    print(so.TreeDepth2(root))
