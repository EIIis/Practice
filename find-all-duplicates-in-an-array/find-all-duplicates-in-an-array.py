class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set() 
        results = []
        
        for numbers in nums:
            if numbers not in seen:
                seen.add(numbers)
            else:
                results.append(numbers)
                
        return results
    
    
        