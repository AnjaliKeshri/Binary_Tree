class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val,end=' ')
    inorder(root.right)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.right.right=Node(4)
root.left.left=Node(58)
root.left.left.left=Node(8)
root.left.left.right=Node(7)
(inorder(root))