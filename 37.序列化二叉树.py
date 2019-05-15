# -*- coding:utf-8 -*-
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
    def Serialize(self, root):
        # write code here
        if not root: return None
        res = ''
        res = self.fore(root, res)
        return res

    def fore(self, root, res):
        if not root: return
        res += str(root.val)
        if root.left:
            res += ','
            res = self.fore(root.left, res)
        else:
            res += ',#'
        if root.right:
            res += ','
            res = self.fore(root.right, res)
        else:
            res += ',#'
        return res

    @exeTime
    def Deserialize(self, s):
        # write code here
        if not s or s == '#' or s == '##': return None
        l = s.split(',')
        node = self.deFore(l)
        return node

    def deFore(self, l):
        if not l or l[0] == '#': return None
        node = TreeNode(int(l[0]))
        l.pop(0)
        node.left = self.deFore(l)
        if l:
            l.pop(0)
            node.right = self.deFore(l)
        return node

    @exeTime
    def Deserialize2(self, s):
        # write code here
        if not s or s == '#' or s == '##': return None
        res = []
        l = s.split(',')
        self.deFore2(l, res)
        return res

    def deFore2(self, l, res):
        if not l or l[0] == '#': return None
        node = TreeNode(int(l[0]))
        res.append(node)
        l.pop(0)
        node.left = self.deFore2(l, res)
        if l:
            l.pop(0)
        node.right = self.deFore2(l, res)
        return node

    @exeTime
    def Deserialize3(self, s):
        # write code here
        list = s.split(',')
        return self.deserializeTree(list)

    def deserializeTree(self, list):
        if len(list) <= 0:
            return None
        val = list.pop(0)
        root = None
        if val != "#":
            root = TreeNode(int(val))
            root.left = self.deserializeTree(list)
            root.right = self.deserializeTree(list)
        return root


if __name__ == "__main__":
    node = TreeNode(0)
    root = node.initTree()
    so = Solution()
    s = so.Serialize(root)
    res = so.Deserialize(s)
    root = node.initTree()
    s = so.Serialize(root)
    res = so.Deserialize2(s)
    root = node.initTree()
    s = so.Serialize(root)
    res = so.Deserialize3(s)