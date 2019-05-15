from exeTime import exeTime
'''本题有一个扩展，求链表的中间结点。若结点数为偶数，返回中间两个的任意一个
若为奇数，返回中间结点。
同样可以采用两个指针，但是一个指针一次走一步，另一个一次走两步。
第二个指针到达末尾后，第一个指针指向的就是要找的结点。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def makeList(self, s):
        nodeList = []
        for i in s:
            nodeList.append(ListNode(i))
        for i in range(len(nodeList) - 1):
            nodeList[i].next = nodeList[i + 1]
        return nodeList


class Solution:
    @exeTime
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k < 0: return
        p = head
        q = p
        while k > 0:
            q = q.next
            k -= 1
        while q:
            p = p.next
            q = q.next
        return p

    @exeTime
    def FindKthToTail2(self, head, k):
        if head == None or k < 0: return
        res = []
        while head:
            res.append(head)
            head = head.next
        return res[-k]


if __name__ == "__main__":
    listNode = ListNode(0)
    so = Solution()
    s = list(range(50))
    nodeList = listNode.makeList(s)
    k = 9
    kth = so.FindKthToTail(nodeList[0], k)
    print(kth.val)
    kth = so.FindKthToTail2(nodeList[0], k)
    print(kth.val)
