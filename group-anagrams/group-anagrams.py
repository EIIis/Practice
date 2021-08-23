class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hm = {}
        for i in strs:
            sort = "".join(sorted(i))
            if sort in hm:
                hm[sort].append(i)
            else:
                hm[sort] = [i]

        return list(hm.values())
    