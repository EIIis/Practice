# https://www.algoexpert.io/questions/Invert%20Binary%20Tree
def invertBinaryTree(tree):
    if tree is None: # If the root is none, then just return the tree
        return tree
    childSwap(tree) # Call out helper function
    invertBinaryTree(tree.left) # Recursively call it for the left
    invertBinaryTree(tree.right) # Recvursively call it for the right
    
def childSwap(tree):
    childStore = tree.left # Stores the left child in a variable
    tree.left = tree.right # Makes the left equal to the right
    tree.right = childStore # Makes the right equal the saved left


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        