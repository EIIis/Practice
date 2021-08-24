class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        pointer1 = m - 1
        pointer2 = n - 1
        
        for p in range(n + m - 1, -1, -1):
            if pointer2 < 0:
                break
            if pointer1 >= 0 and nums1[pointer1] > nums2[pointer2]:
                nums1[p] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[p] = nums2[pointer2]
                pointer2 -= 1
            
            
        