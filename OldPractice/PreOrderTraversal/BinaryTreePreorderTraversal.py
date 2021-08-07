# https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/

class TreeNode(object):
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        self.traversalHelper(root, output)
        return output

    def traversalHelper(self, root, output):
        if root is None:
            return
        output.append(root.val)
        self.traversalHelper(root.left, output)
        self.traversalHelper(root.right, output)
