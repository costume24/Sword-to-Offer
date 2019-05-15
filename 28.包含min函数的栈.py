from exeTime import exeTime


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.mini = None

    def push(self, node):
        # write code here
        if len(self.stack) == 0: self.mini = node
        if node < self.mini: self.mini = node
        self.stack.append(node)

    def pop(self):
        # write code here
        res = self.stack.pop(-1)
        if res == self.mini:
            self.mini = min(self.stack)
        return res

    def top(self):
        # write code here
        return self.stack[0]

    def min(self):
        # write code here
        return self.mini


if __name__ == "__main__":
    so = Solution()
    so.push(3)
    print(so.min())

    so.push(4)
    print(so.min())

    so.push(2)
    print(so.min())

    so.push(3)
    print(so.min())

    so.pop()
    print(so.min())
    so.pop()
    print(so.min())
    so.pop()
    print(so.min())
    so.push(0)
    print(so.min())