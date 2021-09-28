class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        myArr = s.split()
        stringBuilder = ''
        
        for i in range(len(myArr) - 1, -1, -1):
            if i == 0:
                stringBuilder += myArr[i]
            else:
                stringBuilder += myArr[i] + " "
            
        return stringBuilder
        