from exeTime import exeTime


class TreeNode:
    def __init__(self, val):
        self.val = val
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


def kth_node_in_bst(root, k):
    '''对一颗二叉搜索树来说，中序遍历即可得到递增序列
    实际上是考察中序遍历
    '''
    if not root: return
    proot = root
    res = []
    res = mid_traversal(proot, res)
    return res[k - 1]


def mid_traversal(root, res):
    if not root: return res
    pleft = root.left
    pright = root.right
    if pleft:
        mid_traversal(pleft, res)
    res.append(root.val)
    if pright:
        mid_traversal(pright, res)
    return res


if __name__ == "__main__":
    node = TreeNode(0)
    root = node.initTree()
    k = 3
    print(kth_node_in_bst(root, k))
