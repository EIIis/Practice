class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hmap = {}
        
        if len(s) != len(t):
            return False
    
        for letter in s:
            if not letter in hmap:
                hmap[letter] = 1
            else:
                hmap[letter] += 1
                
        for letter in t:
            if not letter in hmap:
                return False
            else:
                hmap[letter] -= 1
                if hmap[letter] == 0:
                    del hmap[letter]
                    
                
        return True