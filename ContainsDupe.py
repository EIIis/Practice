# https://leetcode.com/problems/contains-duplicate/
def containsDuplicate(nums): # Array Parameter
# Sorting the array and checking if the array next to it is the same
        nums.sort() # Sorting in array

        if len(nums) > 1: # Checking if the length of the array > 1, then we'll run the if statement. A corner case
            for i in range(0, len(nums)-1): # We'll iterate though the 0 - (length of the array - 1)
                if nums[i] == nums[i+1]: # We'll check if the element of the array equals to the element of the array next to it, essentially checking if they're equal or not
                    return True
        else: # If the main if statement is invalid, then we'll just return false
            return False