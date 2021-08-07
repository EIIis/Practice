# https://www.algoexpert.io/questions/Group%20Anagrams

def groupAnagrams(words):
    if len(words) == 0:
        return []
    
    hm = {}
    for i in words:
        sort = "".join(sorted(i))
        if sort in hm:
            hm[sort].append(i)
        else:
            hm[sort] = [i]

    return list(hm.values())