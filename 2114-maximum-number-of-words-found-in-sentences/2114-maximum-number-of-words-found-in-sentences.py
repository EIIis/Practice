class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        count = 0
        
        for i in range(len(sentences)):
            listV = sentences[i].split()
            words = len(listV)
            if words >= count:
                count = words
        return count
            