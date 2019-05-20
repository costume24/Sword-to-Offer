from exeTime import exeTime


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def get_node(self, s1, s2, common):
        node1 = []
        node2 = []
        node_common = []
        for item in s1:
            node1.append(ListNode(item))
        for item in s2:
            node2.append(ListNode(item))
        for item in common:
            node_common.append(ListNode(item))
        for i in range(len(node1) - 1):
            node1[i].next = node1[i + 1]
        for i in range(len(node2) - 1):
            node2[i].next = node2[i + 1]
        for i in range(len(node_common) - 1):
            node_common[i].next = node_common[i + 1]
        if node1:
            node1[-1].next = node_common[0]
        if node2:
            node2[-1].next = node_common[0]
        node1.extend(node_common)
        node2.extend(node_common)

        return node1[0], node2[0]


class Solution:
    @exeTime
    def FindFirstCommonNode(self, pHead1, pHead2):
        '''Python特色的解法
        '''
        if not pHead1 or not pHead2: return None
        ids = []
        p1 = pHead1
        p2 = pHead2
        while p1:
            ids.append(id(p1))
            p1 = p1.next
        while p2:
            if id(p2) in ids:
                return p2
            p2 = p2.next
        return None

    @exeTime
    def FindFirstCommonNode2(self, pHead1, pHead2):
        '''由于是单向链表，因此若存在公共节点，则两个链表的尾节点一定相同
        可以从尾节点开始比较，第一个不相同的节点的next节点就是第一个公共节点
        '''
        if not pHead1 or not pHead2: return None
        stack1 = []
        stack2 = []
        p1 = pHead1
        p2 = pHead2
        while p1:
            stack1.append(p1)
            p1 = p1.next
        while p2:
            stack2.append(p2)
            p2 = p2.next
        slen1 = len(stack1)
        slen2 = len(stack2)
        if stack1[-1] != stack2[-1]: return None
        i, j = slen1 - 1, slen2 - 1
        while i >= 0 and j >= 0:
            if stack1[i] != stack2[j]:
                return stack1[i + 1]
            else:
                i -= 1
                j -= 1
        if i == -1: return pHead1
        elif j == -1: return pHead2
        return None

    @exeTime
    def FindFirstCommonNode3(self, pHead1, pHead2):
        '''将两个链表的图画出来，可以看出像一个Y型
        两个指针最终汇聚的时候，就是第一个公共节点
        '''
        p1 = pHead1
        p2 = pHead2
        while p1 != p2:
            p1 = p1.next if p1 != None else pHead2
            p2 = p2.next if p2 != None else pHead1
        return p1


if __name__ == "__main__":
    node = ListNode(0)
    so = Solution()
    s1 = [1, 2]
    s2 = []
    common = [6, 7]
    p1, p2 = node.get_node(s1, s2, common)

    res = so.FindFirstCommonNode(p1, p2)
    print(res.val)

    res = so.FindFirstCommonNode2(p1, p2)
    print(res.val)

    res = so.FindFirstCommonNode3(p1, p2)
    print(res.val)
