class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        result = max(nums)
        currMin = 1
        currMax = 1
        
        for n in nums:
            if n == 0:
                currMin = 1
                currMax = 1
                continue
            tmp = currMax * n
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(tmp, n * currMin, n)
            result = max(result, currMax)
            
        return result
            
        