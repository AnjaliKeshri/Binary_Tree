class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def maximum_depth(root):
    if root==None:
        return 0
    lheight=maximum_depth(root.left)
    rheight=maximum_depth(root.right)
    if(lheight>rheight):
        return lheight+1
    else:
        return rheight+1
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.right.right=Node(4)
root.left.left=Node(58)
root.left.left.left=Node(8)
root.left.left.right=Node(7)
print(maximum_depth(root))