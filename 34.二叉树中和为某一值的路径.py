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
        t6 = TreeNode(3)

        t0.left = t1
        t0.right = t2
        t1.left = t3
        t1.right = t4
        t2.left = t5
        t2.right = t6
        return t0


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    @exeTime
    def FindPath(self, root, expectNumber):
        '''回溯法
        '''
        if not root: return []
        if root and not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        res = []
        path = [root.val]
        result = root.val
        self.back(root, path, result, expectNumber, res)
        return res

    def back(self, root, path, result, aim, res):
        '''回溯法采用递归形式
        注意细节，每次返回父节点的时候需要回溯到上一状态

        Args:
            root:当前节点
            path:路径列表
            result:当前路径的和
            aim:目标值
            res:存储所有路径的二维列表

        Returns:
            更新后的当前路径和
        '''
        le = root.left
        if le:
            result += le.val
            path.append(le.val)
            if not le.left and not le.right:  #到达叶节点
                if result == aim:
                    res.append(path[:])
                result -= le.val
                path.pop()
            else:
                result = self.back(le, path, result, aim, res)
        ri = root.right
        if ri:
            result += ri.val
            path.append(ri.val)
            if not ri.left and not ri.right:
                if result == aim:
                    res.append(path[:])
                result -= ri.val
                path.pop()
            else:
                result = self.back(ri, path, result, aim, res)
        result -= root.val  # 返回父节点时，回溯到上一状态
        path.pop()
        return result  # 需要返回result值，否则上一次调用无法获得更新后的result值


if __name__ == "__main__":
    node = TreeNode(0)
    so = Solution()
    root = node.initTree()
    aim = 21
    res = so.FindPath(root, aim)
    count = 0
    for li in res:
        count += 1
        print('=' * 3, count, '=' * 3)
        for item in li:
            print(item)
