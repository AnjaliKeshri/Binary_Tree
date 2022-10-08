class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
        
def level_order_traversal(root):
    if root is None:
        return []
    result, current = [], [root]
    while current:
        next_level, vals = [], []
        for node in current:
            vals.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        current = next_level
        result.append(vals)
    return result

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.right.right=Node(4)
root.left.left=Node(58)
root.left.left.left=Node(8)
root.left.left.right=Node(7)
print(level_order_traversal(root))
