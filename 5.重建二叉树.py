from exeTime import exeTime


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


@exeTime
def reConstructBinaryTree(pre, tin):
    if len(pre) == 0:
        return None
    elif len(pre) == 1:
        return TreeNode(pre[0])
    root = TreeNode(pre[0])
    i = tin.index(root.val)
    left_pre = pre[1 : i + 1]
    right_pre = pre[i + 1 :]
    left_tin = tin[:i]
    right_tin = tin[i + 1 :]
    root.left = reConstructBinaryTree(left_pre, left_tin)
    root.right = reConstructBinaryTree(right_pre, right_tin)
    return root


if __name__ == "__main__":
    root = TreeNode(1)
    root1 = TreeNode(2)
    root2 = TreeNode(3)
    root3 = TreeNode(4)
    root4 = TreeNode(5)
    root5 = TreeNode(6)
    root6 = TreeNode(7)
    root7 = TreeNode(8)
    root.left = root1
    root.right = root2
    root1.left = root3
    root3.right = root6
    root2.left = root4
    root2.right = root5
    root5.left = root7
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    print(reConstructBinaryTree(pre, tin).val)

