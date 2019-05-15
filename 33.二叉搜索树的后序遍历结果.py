from exeTime import exeTime


# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        '''取出根节点（后序遍历的根节点为末尾元素）
        然后根据BST的性质（左子树所有节点小于根节点，右子树所有节点大于根节点）
        递归判断是否为BST
        '''
        if not sequence: return False
        slen = len(sequence)
        if slen == 1: return True
        root = sequence[-1]
        j = 0
        for i in range(slen):
            if sequence[i] > root:
                break
        j = i
        for _ in range(j, slen - 1):
            if sequence[j] < root:
                return False
            j += 1
        left = True
        if i > 0: left = self.VerifySquenceOfBST(sequence[:i])
        right = True
        if i < slen - 1:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right


if __name__ == "__main__":
    so = Solution()
    seq = [4, 6, 7, 5]
    print(so.VerifySquenceOfBST(seq))