# https://www.algoexpert.io/questions/First%20Duplicate%20Value
def firstDuplicateValue(array):
    hset = set() # We create an empty set
    for i in array: # We traverse though given array
        if i in hset: # We check if the element in array is in h set
            return i # If i is in h set then we return i, as that would be the first duplicate
        hset.add(i) # If i is not in h set then we add it inside h set

    return -1 # If we traverse though the entire array/set and no dupe, we return -1
