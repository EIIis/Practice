# https://www.hackerrank.com/challenges/sock-merchant/problem
def sockMerchant(n, arr):
    count = 0
    hashmap = {}
    for i in arr:
        hashmap[i] = hashmap.get(i, 0) + 1
    for i in hashmap.keys():
        count += hashmap[i]//2
        
    return count 
