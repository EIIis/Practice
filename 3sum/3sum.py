class Solution(object):
    def threeSum(self, array):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        array.sort()
        results = []
        for i in range(len(array) - 2):
            left = i + 1
            right = len(array) - 1
            while left < right:
                current = array[i] + array[left] + array[right]
                if current == 0:
                    if [array[i], array[left], array[right]] in results:
                        left += 1
                        right -= 1
                        continue
                    else:
                        results.append([array[i], array[left], array[right]])
                        left += 1
                        right -= 1
                elif current < 0:
                    left += 1
                elif current > 0:
                    right -= 1
        return results
        