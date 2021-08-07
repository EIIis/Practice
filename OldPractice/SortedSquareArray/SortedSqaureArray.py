# O(nlogn) Time, ;-;. I'll try and learn to do it a faster way later.
# https://www.algoexpert.io/questions/Sorted%20Squared%20Array
def sortedSquaredArray(array):
    sqArr = [] # Creating an empty list
    for i in range(len(array)): # Traversing through the array
        sqNum = array[i]**2 # Making a temp array and making it equal to squaring the element of array
        sqArr.append(sqNum) # Adding our variable to our list
        ++i # Going to the next element in our given array
    sqArr.sort() # Once all squared, we sort it
    return sqArr # Returning our sorted sqaured array
