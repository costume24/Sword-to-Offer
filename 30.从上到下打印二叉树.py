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
        t6 = TreeNode(2)

        t0.left = t1
        t0.right = t2
        t1.left = t3
        t1.right = t4
        t2.left = t5
        t2.right = t6
        return t0


class Solution:
    @exeTime
    def PrintFromTopToBottom(self, root):
        '''基于队列实现
        出队时，将出队节点的子节点入队
        广度优先遍历都要用到队列
        '''
        if not root: return None
        res = []
        queue = []
        queue.append(root)
        while queue:
            last = queue.pop(0)
            if not last: continue
            res.append(last.val)
            queue.append(last.left)
            queue.append(last.right)
        return res

    @exeTime
    def PrintFromTopToBottom2(self, root):
        # write code here
        l = []
        if not root:
            return []
        q = [root]
        while len(q):
            t = q.pop(0)
            l.append(t.val)
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
        return l


if __name__ == "__main__":
    so = Solution()
    node = TreeNode(0)
    root = node.initTree()
    print(so.PrintFromTopToBottom(root))
    root = node.initTree()
    print(so.PrintFromTopToBottom2(root))
