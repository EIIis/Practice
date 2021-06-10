# https://www.algoexpert.io/questions/Class%20Photos
def classPhotos(redShirtHeights, blueShirtHeights):
    blueShirtHeights.sort() # Sorts our array
    redShirtHeights.sort() # Sorts our array

# Because one row has to be bigger than the other we check the first element and go from there
# If it were vice-verse then our for-loops would be reveresed
    if redShirtHeights[0] > blueShirtHeights[0]:
        for i in range(len(redShirtHeights)): # We're going to iterate through the redshirt heights
            if redShirtHeights[i] <= blueShirtHeights[i]: # Checking the other shirt is greater or equal
                return False # If it is we say false
        return True # If it's not then we say true!
    else: # The same code as the other for-loop but it only runs if blueShirt is bigger at the start. Same logic!
        for i in range(len(blueShirtHeights)):
            if blueShirtHeights[i] <= redShirtHeights[i]:
                return False
        return True