# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Checking if root is null/none
        if root is None:
            return root
        else:
            temp = root.right # temporarliy hold our right
            root.right = root.left # switch right -> left
            root.left = temp # switch left -> right (held in our temp)
        # Using depth for search
        self.invertTree(root.right) # do it for recursively for the right side
        self.invertTree(root.left) #do it for recursively for the left side
        return root
        
        