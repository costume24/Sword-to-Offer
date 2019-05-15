from exeTime import exeTime


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def go(self, l):
        tmp = []
        for i in range(len(l)):
            tmp.append(ListNode(l[i]))
        for i in range(len(tmp) - 1):
            tmp[i].next = tmp[i + 1]
        return tmp


class Solution:
    @exeTime
    def deleteDuplication(self, pHead):
        if pHead == None or pHead.next == None: return pHead
        pNow = pHead
        pPre = pNow
        while pNow.next is not None:  # 下一个节点不为空
            pNext = pNow.next
            if pNow.val == pNext.val and pPre != pNow:  # 若不是刚开始
                while pNext.next != None:  # 一直寻找重复的节点
                    if pNext.val == pNext.next.val:
                        pNext = pNext.next
                        continue
                    break
                if pNext.next == None:  # 若从pNow开始到链表末尾都是重复的节点
                    pPre.next = None  # 则程序结束
                    return pHead
                else:  # 若后面还有节点，则继续
                    pNow = pNext.next
                    pPre.next = pNow
            elif pNow.val == pNext.val and pPre == pNow:  # 若是刚开始
                while pNext.next != None:  # 其余步骤相同
                    if pNext.val == pNext.next.val:
                        pNext = pNext.next
                        continue
                    break
                if pNext.next == None:  # 直接设置头指针
                    return None
                else:  # 此时需要移动头指针
                    pNow = pNext.next
                    pPre = pNow
                    pHead = pNow
            else:
                pPre = pNow
                pNow = pNext

        return pHead

    @exeTime
    def del2(self, pHead):
        if not pHead:
            return None
        preNode = ListNode(None)
        preNode.next = pHead
        head = preNode
        flg = False
        while pHead and pHead.next:
            pNext = pHead.next
            if pHead.val == pNext.val:
                flg = True
                pHead.next = pNext.next
                pNext.next = None
            elif flg == True:
                preNode.next = pHead.next
                pHead = pHead.next
                flg = False
            else:
                preNode = pHead
                pHead = pHead.next
        if flg:
            preNode.next = None
        return head.next


if __name__ == "__main__":
    so = Solution()
    node = ListNode(0)
    s = [1, 3, 3, 3, 4, 4, 5, 6, 6, 7, 7, 8, 9, 12, 13, 14, 14, 14, 15]
    l = node.go(s)
    head = so.deleteDuplication(l[0])
    head = so.del2(l[0])
    while head is not None:
        print(head.val)
        head = head.next
