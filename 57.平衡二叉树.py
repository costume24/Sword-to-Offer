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
        t7 = TreeNode(7)
        t8 = TreeNode(2)
        t0.left = t1
        t0.right = t2
        t1.left = t3
        t1.right = t4
        #t2.left = t5
        t2.right = t6
        t4.left = t7
        t7.left = t8
        return t0


class Solution:
    def IsBalanced_Solution(self, pRoot, depth):
        '''后序遍历，遍历每个节点的时候记录它的深度
        自底向上，每个节点只需要遍历一次
        若自顶向下，则判断上层节点时，需要多次遍历下层节点
        类似动态规划的思想
        '''
        if not pRoot:
            depth = [0]
            return True
        left, right = [0], [0]
        if self.IsBalanced_Solution(pRoot.left,left) \
            and self.IsBalanced_Solution(pRoot.right,right):
            diff = left[0] - right[0]
            if diff <= 1 and diff >= -1:
                depth[0] = 1 + left[0] if left[0] > right[0] else 1 + right[0]
                return True
        return False


if __name__ == "__main__":
    so = Solution()
    node = TreeNode(0)
    root = node.initTree()
    depth = 0
    print(so.IsBalanced_Solution(root, depth))
