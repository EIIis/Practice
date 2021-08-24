class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hashmap = {}
        
        for index, num in enumerate(nums):
            sol = target - num
            if sol in hashmap:
                return [index, hashmap[sol]]
            else:
                hashmap[num] = index
        return []