class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def height(node):
    if node is None:
        return 0
    return (1+max(height(node.left),height(node.right)))
def diameter(root):
    if root is None:
        return 0
    lheight=height(root.left)
    rheight=height(root.right)
    ldiameter=diameter(root.left)
    rdiameter=diameter(root.right)
    return(max(lheight+rheight+1,max(ldiameter,rdiameter)))
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.right.right=Node(4)
root.left.left=Node(58)
root.left.left.left=Node(8)
root.left.left.right=Node(7)
print(diameter(root))