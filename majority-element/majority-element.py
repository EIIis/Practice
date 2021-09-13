class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1
        
        return max(seen, key=seen.get)