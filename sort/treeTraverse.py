class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

# 前序遍历
def preTraverse(root):
    if root == None:
        return
    print(root.value)
    preTraverse(root.left)
    preTraverse(root.right)
# 中序遍历
def midTraverse(root):
    if root == None:
        return
    midTraverse(root.left)
    print(root.value)
    midTraverse(root.right)
# 后序遍历
def afterTraverse(root):
    if root == None:
        return
    afterTraverse(root.left)
    afterTraverse(root.right)
    print(root.value)

# Node初始化
root = Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))


# 已知前序和中序遍历，求后序遍历
preList = list('12473568')
midList = list('47215386')
afterList = []

def findTree(preList, midList, afterList):
    if len(preList) == 0:
        return
    if len(preList) == 1:
        afterList.append(preList[0])
        return
    root = preList[0]
    n = midList.index(root)
    findTree(preList[1:n + 1], midList[:n], afterList)
    findTree(preList[n + 1:], midList[n + 1:], afterList)
    afterList.append(root)