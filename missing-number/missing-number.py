class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        nextVal = nums[0]
        
        if nextVal != 0:
            return 0
        else:
            for num in nums:
                if num == nextVal:
                    nextVal += 1
                else:
                    return nextVal
                
            last = nums[len(nums) - 1] + 1
            
            return last
