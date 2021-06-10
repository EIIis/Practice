# https://www.algoexpert.io/questions/Generate%20Document
def generateDocument(characters, document):
    cHash = {} # Creating an empty hashmap

    for l in characters: # we're iterating through the letters of our string 'characters'
        if not l in cHash: # If the letter isnt in the hashmap
            cHash[l] = 1 # We set the value to 1
        else:
            cHash[l] += 1 # If it is, we increase the value by +1

    for l in document: # We're iterating through the letters of our string 'document'
        if l in cHash: # We're going to iterate through our hashmap checking if l is inside hashmap
            cHash[l] -= 1 # If l in document is inside our hashmap, we'll decrease the value by -1
            if cHash[l] == 0: # If the value it 0,
                del cHash[l] # We delete the key from the hashmap
        else:
            return False # If l isn't in document, we return false because we cant recreate the string

    return True # Return true if we have enough characters to recreate document!
