from exeTime import exeTime


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def go(self, s):
        node = []
        for item in s:
            node.append(ListNode(item))
        for i in range(len(node) - 1):
            node[i].next = node[i + 1]
        return node


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        '''
        3个指针，每次将中间指针的next重新赋值
        考虑到链表为空，只有一个节点和两个节点的情况
        开始时将头节点的next置为None，结束时将尾节点的next置为前一个节点
        '''
        if not pHead: return None
        if not pHead.next: return pHead
        rear, now = pHead, pHead.next
        if not now.next:
            now.next = rear
            rear.next = None
            return now
        front = now.next
        rear.next = None
        while front:
            now.next = rear
            rear = now
            now = front
            front = front.next
        now.next = rear
        return now


if __name__ == "__main__":
    li = ListNode(0)
    so = Solution()
    s = [1, 2, 3, 4, 5, 6]
    node = li.go(s)
    head = so.ReverseList(node[0])
    while head:
        print(head.val)
        head = head.next
