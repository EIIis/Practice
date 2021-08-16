class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        myset = set()
        
        for i in range(len(nums)):
            if not nums[i] in myset:
                myset.add(nums[i])
            else:
                return True
        return False
        