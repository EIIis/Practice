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
            for i in nums:
                if i == nextVal:
                    nextVal += 1
                else:
                    return nextVal
            length = len(nums) - 1
            last = nums[length] + 1
            return last
