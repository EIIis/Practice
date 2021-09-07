class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] != target:
                    continue
                else:
                    return [i, j]
            
                    
        
        """
        hashmap = {}
        
        for index, num in enumerate(nums):
            sol = target - num
            if sol in hashmap:
                return [index, hashmap[sol]]
            else:
                hashmap[num] = index
        return []
        """