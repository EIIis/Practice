class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num = set(nums)
        missing = []
        for i in range(len(nums)):
            if i + 1 not in num:
                missing.append(i + 1)
        return missing
        
        
        """
        missingNums = []
        
        nums.sort()
        count = 1
        
        for _ in range(len(nums)):
            if count not in nums:
                missingNums.append(count)
                count += 1
            else:
                count += 1
        return missingNums
        """