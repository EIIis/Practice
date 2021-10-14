class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 0

        while idx < len(nums):
            correct = nums[idx]
            if nums[idx] < len(nums) and nums[idx] != nums[correct]:
                nums[idx], nums[correct] = nums[correct], nums[idx]
            else:
                idx += 1
  
        for i in range(len(nums)):
            if nums[i] != i:
                return i
  
        return len(nums)
