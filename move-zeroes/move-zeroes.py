class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        first = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            else:
                nums[i], nums[first] = nums[first], nums[i]
                first += 1
        