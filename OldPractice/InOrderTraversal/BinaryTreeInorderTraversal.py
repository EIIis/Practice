# https://leetcode.com/problems/binary-tree-inorder-traversal/
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
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

        self.traversalHelper(root.left, output)
        output.append(root.val)
        self.traversalHelper(root.right, output)