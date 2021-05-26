# O(nlogn) Time, ;-;. I'll try and learn to do it a faster way later.
def sortedSquaredArray(array):
	sqArr = []
	for i in range(len(array)):
		sqNum = array[i]**2
		sqArr.append(sqNum)
		++i
	sqArr.sort()
    return sqArr
