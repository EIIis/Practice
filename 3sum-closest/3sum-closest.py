class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = float('inf')
        
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                close = nums[left] + nums[right] + nums[i]
                if close == target:
                    return close
                elif abs(target - close) < abs(target - closest):
                    closest = close
                elif close < target:
                    left += 1
                else:
                    right -= 1   
                    
        return closest