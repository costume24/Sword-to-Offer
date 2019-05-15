from exeTime import exeTime
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

def generateTree(node):
    node0=TreeLinkNode('a')
    node1=TreeLinkNode('b')
    node2=TreeLinkNode('c')
    node3=TreeLinkNode('d')
    node4=TreeLinkNode('e')
    node5=TreeLinkNode('f')
    node6=TreeLinkNode('g')
    node7=TreeLinkNode('h')
    node8=TreeLinkNode('i')
    node0.left=node1
    node0.right=node2
    node1.left=node3
    node1.right=node4
    node4.left=node7
    node4.right=node8
    node2.left=node5
    node2.right=node6

    node1.next=node0
    node2.next=node0
    node3.next=node1
    node4.next=node1
    node5.next=node2
    node6.next=node2
    node7.next=node4
    node8.next=node4
    return eval(node)
@exeTime
def GetNext(pNode):
    if pNode.next!=None:                       # 若结点不是根节点
        if pNode.next.left==pNode:             # 若结点是父节点的左子节点
            if pNode.right==None:              # 若结点没有右子结点，返回父节点
                return pNode.next.val
            else:                              # 若有，则一路向左
                rNode=pNode.right
                while rNode.left!=None:
                    rNode=rNode.left
                return rNode.val
        elif pNode.next.right==pNode:          # 若结点是父节点的右子节点
            if pNode.right!=None:              # 若结点有右子树，则一路向左
                rNode=pNode.right
                while rNode.left!=None:
                    rNode=rNode.left
                return rNode.val
            else:                              # 若没有右子树，则向上寻找到以其父系结点作为左子结点的结点
                parent=pNode.next
                while parent.next:
                    if parent.next.left==parent:return parent.next.val
                    parent=parent.next
                return None
    else:                                       # 若结点是根节点
        if pNode.right==None:return None        # 若没有右子树，说明是最后一个
        else:                                   # 有右子树，则一路向左
            rNode=pNode.right
            while rNode.left!=None:
                rNode=rNode.left
            return rNode.val

@exeTime
def GetNext2(pNode):
    if not pNode:return None                
    if pNode.right != None:                     # 直接考虑有没有右子树
        rNode=pNode.right
        while rNode.left:
            rNode=rNode.left
        return rNode.val
    parent=pNode                                # 若没有，则向上寻找
    while parent.next:
        if parent.next.left==parent:return parent.next.val  # 实际上包含了结点是左子结点且无右子树的情况
        parent=parent.next
    return None
    

if __name__ == "__main__":
    for i in range(9):
        node='node'+str(i)
        pNode=generateTree(node)
        print(pNode.val,':',GetNext2(pNode))


