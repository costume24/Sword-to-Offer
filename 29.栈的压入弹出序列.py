from exeTime import exeTime


# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        if not popV: return True
        elif not pushV: return False
        n, m = len(pushV), len(popV)
        if n != m: return False
        pushStack = []
        p, q = 0, 0
        while q < m:
            if popV[q] in pushStack:  # 若待出栈的元素已在栈中
                if pushStack.pop() != popV[q]:
                    return False  # 则出栈。若栈顶元素与待出栈元素不相等，则返回False
                q += 1
            else:
                if p == n: return False  # 若所有元素均已入栈，待出栈元素仍不在栈中，则返回False
                pushStack.append(pushV[p])  # 若待出栈元素不在栈中，则入栈一个元素
                p += 1
        return True if not pushStack else False


if __name__ == "__main__":
    so = Solution()
    pushV = [1, 2, 3, 4, 5]
    popV = [4, 3, 5, 1, 2]
    print(so.IsPopOrder(pushV, popV))
