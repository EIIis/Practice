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
                if nums[left] + nums[right] + nums[i] == target:
                    return target
                if abs(target - (nums[left] + nums[right] + nums[i])) < abs(target - closest):
                    closest = nums[left] + nums[right] + nums[i]
                if nums[left] + nums[right] + nums[i] < target:
                    left += 1
                else:
                    right -= 1   
                    
        return closest