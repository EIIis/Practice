class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hm = {}
        for words in strs:
            sort = "".join(sorted(words))
            if sort in hm:
                hm[sort].append(words)
            else:
                hm[sort] = [words]

        return list(hm.values())
    