class Solution(object):
    def removeVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        newStr = ""
        
        for letters in s:
            if letters not in vowels:
                newStr += letters
        
        return newStr
        