class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(height) - 1
        
        count = 0
        
        while left < right:
            count = max(count, count, min(height[left], height[right]) * (right-left))
            if (height[left] < height[right]):
                left += 1
            else:
                right -= 1
        
        return count
        
        
        """
        # Count to keep max count so far
        count = 0
        
        # Iterating throughout the array
        for i in range(len(height)):
            # Iterate through the array from where i is, to the end of the array
            for j in range(i + 1, len(height)):
                # Calculating count, will assign count to the value of whichever is greater, current count OR height[i] or height[j] (whichever is minimum) multiplied by (j - 1) 
                count = max(count, min(height[i], height[j]) * (j-i))
        return count
        """