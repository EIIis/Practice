class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSub = nums[0]
        currentSum = 0
        
        for i in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += i
            maxSub = max(maxSub, currentSum)
                
        return maxSub
        