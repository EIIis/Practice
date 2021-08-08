class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        index = 0
        for i in range(len(nums)):
            if count < 2:
                nums[index] = nums[i]
                index += 1
            if i == (len(nums) - 1) or nums[i] != nums[i+1]:
                count=0
            elif nums[i] == nums[i+1]:
                count += 1
        return index
    
        """
        hm = {}
        
        for i in nums:
            if i in hm:
                hm[i] += 1
                if hm.get(i) > 2:
                    nums.pop(i)
            else:
                hm[i] = 1
              
        return len(nums)   
        """
        