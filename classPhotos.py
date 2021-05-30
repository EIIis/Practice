# https://www.algoexpert.io/questions/Class%20Photos
def classPhotos(redShirtHeights, blueShirtHeights):
	blueShirtHeights.sort()
	redShirtHeights.sort()
	
	if redShirtHeights[0] > blueShirtHeights[0]:
		for i in range(len(redShirtHeights)):
			if redShirtHeights[i] <= blueShirtHeights[i]:
				return False
		return True
	else:
		for i in range(len(blueShirtHeights)):
			if blueShirtHeights[i] <= redShirtHeights[i]:
				return False
		return True