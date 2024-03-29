# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # O(n) runtime, o(n) time comp
        seen = set()
        while head != None:
            if head in seen:
                return True
            else:
                seen.add(head)
                head = head.next
        return False
        
