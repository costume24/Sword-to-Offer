from exeTime import exeTime


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def go(self, s, entry):
        node = []
        for item in s:
            node.append(ListNode(item))
        for i in range(len(node) - 1):
            node[i].next = node[i + 1]
        node[-1].next = node[entry]
        return node


class Solution:
    @exeTime
    def EntryNodeOfLoop(self, pHead):
        '''
        1.快慢指针找到节点
        2.固定距离指针找到节点入口
        '''
        if not pHead: return None
        slow, fast = pHead, pHead
        hasFlag = False
        count = 1
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                hasFlag = True
                slow = slow.next
                while slow != fast:
                    slow = slow.next
                    count += 1
                break
        if not hasFlag: return None
        rear, front = pHead, pHead
        while count:
            front = front.next
            count -= 1
        while front.next:
            if front == rear: return front.val
            front = front.next
            rear = rear.next
        return None


if __name__ == "__main__":
    li = ListNode(0)
    so = Solution()
    s = [1, 2, 3, 4, 5, 6]
    entry = 2
    node = li.go(s, entry)
    print(so.EntryNodeOfLoop(node[0]))
