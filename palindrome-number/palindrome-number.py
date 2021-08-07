class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x) # Converting the int to a str
        right = len(x) - 1 # Creating an end pointer
        left = 0 # Creating a starting pointer
        
        while left < right: # Creating a while loop to contiuiously run
            for i in x: # iterating through the string
                if x[left] != x[right]: # Checking to see if the elements are the same, when on opposite sides
                    return False # If they're not, return False
                else: # If they are we increase/decrease the pointers by one
                    left += 1
                    right -= 1
        return True # If it continues until the while loop is statified we return True
        
        