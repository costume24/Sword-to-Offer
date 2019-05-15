from exeTime import exeTime


# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

    def initListNode(self):
        n0 = RandomListNode(1)
        n1 = RandomListNode(2)
        n2 = RandomListNode(3)
        n3 = RandomListNode(4)
        n4 = RandomListNode(5)

        n0.next = n1
        n1.next = n2
        n2.next = n3
        n3.next = n4

        n0.random = n2
        n1.random = n4
        n3.random = n1
        return n0


class Solution:
    # 返回 RandomListNode
    @exeTime
    def Clone(self, pHead):
        # write code here
        if not pHead: return None
        head = pHead
        res = []
        old = []
        randomDic = {}

        while head:
            tmp = RandomListNode(head.label)
            res.append(tmp)
            old.append(head)
            randomDic[head] = tmp  # 用字典存储新旧节点的对应关系
            if head.next:
                head = head.next
            else:
                break
        for i in range(len(res) - 1):
            res[i].next = res[i + 1]
            if old[i].random:
                res[i].random = randomDic[old[i].random]
        return res[0]

    @exeTime
    def Clone2(self, pHead):
        '''新节点直接嵌入旧链表中，形如1-1-2-2-3-3-4-4-5-5
        新节点的random就等于旧节点的random的next
        然后再将链表拆分为两部分即可
        '''
        if not pHead: return None
        head = pHead
        res = []
        old = []
        while head:
            tmp = RandomListNode(head.label)
            res.append(tmp)
            old.append(head)
            tmp.next = head.next
            head.next = tmp
            if tmp.next:
                head = tmp.next
            else:
                break
        for i in range(len(res) - 1):
            if old[i].random:
                res[i].random = old[i].random.next
        pOld = pHead
        while pOld.next.next:
            pNew = pOld.next
            pOld.next = pNew.next
            pNew.next = pOld.next.next
            pOld = pOld.next
        return res[1]


if __name__ == "__main__":
    node = RandomListNode(0)
    pHead = node.initListNode()
    t = pHead
    while t:
        print(id(t))
        t = t.next
    so = Solution()
    res = so.Clone2(pHead)
    p = res
    while p:
        print(id(p))
        p = p.next
    pHead = node.initListNode()
    res = so.Clone(pHead)
    while res:
        print(res.label)
        if res.random:
            print('random ', res.random.label)
        if res.next:
            res = res.next
        else:
            break
