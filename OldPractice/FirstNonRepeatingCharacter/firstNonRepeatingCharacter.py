# https://www.algoexpert.io/questions/First%20Non-Repeating%20Character
def firstNonRepeatingCharacter(string):
    hm = {} # Creating an empty hashmap
    for i in string: # Traverse though our string
        if i in hm: # Checking if the character is in the map
            hm[i] += 1 # If it is, we add to our key value
        else: 
            hm[i] = 1 # If it's not we just add a 1 value to it

    i = 0 # Create a new variable set to 0 to represent the element we're at 
    for letter in string: # Traversing through the string
        if hm[letter] == 1: # Checking if the hm value is equal to one
            return i # If it is, we return the value which represne the element
        i += 1 # If it's not, we add 1 to our new variable and continue
    return -1 # If we reach the end, we return -1
    