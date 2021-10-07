# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Appending values of linked list to array
        results = []
        
        current = head
        
        while current != None:
            results.append(current.val)
            current = current.next
        
        left = 0
        right = len(results) - 1
        
        # Is Palindrome, with two pointers
        while left < right:
            if results[left] == results[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
        