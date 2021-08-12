class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for i in nums:
            sqrNum = i ** 2
            arr.append(sqrNum)
            
        arr.sort()
        
        return arr
            
        