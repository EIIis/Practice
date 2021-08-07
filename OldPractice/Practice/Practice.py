"""
def findMaxConsecutiveOnes(nums):
     
        :type nums: List[int]
        :rtype: int
    
        counter = 0
        counter2 = 0
        for i in nums:
            if nums[i] == 1:
                counter += 1
            elif counter <= counter2:
                counter2 = counter
        
        return counter2

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
"""
