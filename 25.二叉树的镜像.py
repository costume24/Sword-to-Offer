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
        t2 = TreeNode(10)
        t3 = TreeNode(5)
        t4 = TreeNode(7)
        t5 = TreeNode(9)
        t6 = TreeNode(11)

        t0.left = t1
        t0.right = t2
        t1.left = t3
        t1.right = t4
        t2.left = t5
        t2.right = t6
        return t0


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root: return None
        self.switch(root, root.left, root.right)
        return root

    def switch(self, root, left, right):
        if not root: return
        if not left and not right: return
        root.left = right
        root.right = left
        left = root.left
        right = root.right
        if left:
            self.switch(left, left.left, left.right)
        if right:
            self.switch(right, right.left, right.right)


if __name__ == "__main__":
    tree = TreeNode(0)
    root = tree.initTree()
    so = Solution()
    print(so.Mirror(root))
