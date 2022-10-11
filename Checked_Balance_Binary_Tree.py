class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def height(root):
    if root is None:
        return 0
    lheight=height(root.left)
    rheight=height(root.right)
    if(lheight>rheight):
        return lheight+1
    else:
        return rheight+1
def balanced_binary_tree(root):
    if root == None:
        return True
    lheight = height(root.left)
    rheight = height(root.right)
    if(((lheight-rheight))>1):
        return False
    lleft=balanced_binary_tree(root.left)
    rright=balanced_binary_tree(root.right)
    if lleft==True and rright==True:
        return True
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.right.right=Node(4)
root.left.right=Node(58)
root.left.left=Node(8)
root.left.left.right=Node(7)
print(balanced_binary_tree(root))