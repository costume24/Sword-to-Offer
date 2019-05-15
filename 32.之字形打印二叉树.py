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
    def Print(self, pRoot):
        if not pRoot: return []
        res = []
        tmp = []
        queue = [pRoot]
        toBePrint = 1  #表示当前层剩余的节点数，每pop一个节点就减一，当为0时，置为next
        next = 0  #表示下一层的节点数，每入队一个节点就加一
        flag = 1  # 与上一题的区别就在于增加了一个控制方向的标志位
        while queue:
            last = queue.pop(0)
            if last.left:
                queue.append(last.left)
                next += 1
            if last.right:
                queue.append(last.right)
                next += 1
            tmp.append(last.val)
            toBePrint -= 1
            if toBePrint == 0:
                res.append(tmp[::flag])  #利用Python的切片性质，为1则正序，为0则逆序
                flag = -flag  #每一行过后反向
                tmp = []
                toBePrint = next
                next = 0
        return res


if __name__ == "__main__":
    node = TreeNode(0)
    so = Solution()
    root = node.initTree()
    print(so.Print(root))