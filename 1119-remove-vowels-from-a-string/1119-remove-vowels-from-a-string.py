class Solution(object):
    def removeVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Creating new string w/ no vowels
        newStr = []
        for letters in s:
            if letters not in vowels:
                newStr.append(letters)

        s = "".join(newStr)
        return s
            
        