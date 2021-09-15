class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        results = [0] * len(nums)
        
        left = 0
        right = len(nums) - 1
        
        
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                results[i] = nums[right] ** 2
                right -= 1
            else:
                results[i] = nums[left] ** 2
                left += 1
                
        return results    
            
        
        """
        arr = []
        
        for i in nums:
            sqrNum = i ** 2
            arr.append(sqrNum)
            
        arr.sort()
        
        return arr
        """