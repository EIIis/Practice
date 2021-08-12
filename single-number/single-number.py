class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        if len(nums) == 1:
            return nums[0]
        else:
            for i in nums:
                if i in seen:
                    seen[i] += 1
                else:
                    seen[i] = 1
        
          
        for key, value in seen.items() :
            if value == 1:
                return key

    

                
        
        