# https://www.algoexpert.io/questions/Node%20Depths
def nodeDepths(root):
    return nodeHelper(root, 0)

def nodeHelper(node, depth):
    if node is None: # Corner case to check if root is null
        return 0
    left = nodeHelper(node.left, depth + 1) # Checks for left children
    right = nodeHelper(node.right, depth + 1) # Checks for right children
    return depth + left + right 
        
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
