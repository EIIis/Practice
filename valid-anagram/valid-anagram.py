class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        else:
            return False
        '''
        if len(s) != len(t):
            return False
        allLetter = {}
        
        for letter in s:
            if letter not in allLetter:
                allLetter[letter] = 1
            else:
                allLetter[letter] += 1
        
        for letter in t:
            if letter not in allLetter:
                return False
            else:
                allLetter[letter] -= 1
                if allLetter[letter] == 0:
                    del allLetter[letter]
                    
        return True
        '''