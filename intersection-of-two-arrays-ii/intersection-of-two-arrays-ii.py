class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hashmap = {}
        results = []
        
        for num in nums1:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
                
        for num in nums2:
            if num in hashmap:
                results.append(num)
                hashmap[num] -= 1
                if hashmap.get(num) == 0:
                    del hashmap[num]
                    
        return results
        