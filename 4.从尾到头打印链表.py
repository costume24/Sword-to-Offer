from exeTime import exeTime
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
@exeTime
def printListFromTailToHead(listNode):
        res=[]
        while True:
            res.append(listNode.val)
            listNode=listNode.next
            if listNode.next==None:
                res.append(listNode.val)
                return res[::-1]
        return []

@exeTime
def printListFromTailToHead2(listNode):
    res=[]
    head=listNode
    while head:
        res.insert(0,head.val)
        head=head.next
    return res

if __name__ == "__main__":
    node=ListNode(1)
    node2=ListNode(2)
    node3=ListNode(3)
    node.next=node2
    node2.next=node3
    print(printListFromTailToHead(node))
    print(printListFromTailToHead2(node))