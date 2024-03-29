# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        seen = set()
        
        while head != None:
            if head in seen:
                return head
            else:
                seen.add(head)
                head = head.next
        return None
            
            