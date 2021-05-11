def sockMerchant(n, ar):
    count = 0
    hashmap = {}
    for i in ar:
        hashmap[i] = hashmap.get(i, 0) + 1
    for i in hashmap.keys():
        count += hashmap[i]//2
        
    return count 
